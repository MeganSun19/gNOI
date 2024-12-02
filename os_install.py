import grpc
from github.com.openconfig.gnoi.os import os_pb2, os_pb2_grpc
from github.com.openconfig.gnoi.bootconfig import bootconfig_pb2
from google.protobuf import empty_pb2
import sys
import os


# username,password authmetadata plugin
class UsernamePasswordCredentials(grpc.AuthMetadataPlugin):
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def __call__(self, context, callback):
        metadata = (
            ('username', self._username),
            ('password', self._password),
        )
        callback(metadata, None)

# perform install action
def os_install_activate(target, port, version, pkg, username, password):
    # auth,ssl
    auth_creds = grpc.metadata_call_credentials(UsernamePasswordCredentials(username, password))
    ca_cert = open('./CA.cer', 'rb').read()  # load CA cert
    channel_creds = grpc.ssl_channel_credentials(root_certificates=ca_cert)
    composite_creds = grpc.composite_channel_credentials(channel_creds, auth_creds)

    # target host's certificate (to match the server certificate)
    cert_cn = '{hostname}'
    options = (('grpc.ssl_target_name_override', cert_cn,),)

    # establish gRPC secure channel
    channel = grpc.secure_channel(f'{target}:{port}', composite_creds, options)
    stub = os_pb2_grpc.OSStub(channel)

    # Install request
    def generate_requests(pkg, version):
        # Send a version initialization request
        yield os_pb2.InstallRequest(
            transfer_request=os_pb2.TransferRequest(version=version)
        )

        # send file chunk
        with open(pkg, "rb") as f:
            while chunk := f.read(64 * 1024): 
                print(f"Sending chunk of size: {len(chunk)} bytes")
                yield os_pb2.InstallRequest(transfer_content=chunk)

        # transfer end
        yield os_pb2.InstallRequest(
            transfer_end=os_pb2.TransferEnd()
        )

    # perform Install request
    try:
        responses = stub.Install(generate_requests(pkg, version))
        for response in responses:
            print("Install response:", response)

    except grpc.RpcError as e:
        print(f"Failed to install: {e.details()}")
        print(f"Status code: {e.code().name}")
        print(f"Debug info: {e.debug_error_string()}")

if __name__ == "__main__":
    target = "{ip}"
    port = {port}
    version = "7.10.2"  #version can be verified on the router by os verify
    pkg = "/ncs5500-goldenk9-x-7.10.2.iso"  # local file path, not the router
    username = "{username}"
    password = "{password}"

    os_install_activate(target, port, version, pkg, username, password)
