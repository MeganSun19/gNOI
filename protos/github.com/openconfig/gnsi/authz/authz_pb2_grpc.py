# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from github.com.openconfig.gnsi.authz import authz_pb2 as github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in github.com/openconfig/gnsi/authz/authz_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AuthzStub(object):
    """The gRPC-level Authorization Policy Management Service exported by targets.


    Authorization Policy defines which principals are permitted to access which
    resource(s). Resources are individual RPC methods scoped by their path(s).
    The policy is expressed in JSON format, following the schema in
    https://github.com/grpc/proposal/blob/master/A43-grpc-authorization-api.md
    and the protobuf in the
    README(https://github.com/openconfig/gnsi/blob/main/authz/README.md).

    Example UploadRequest with policy:

    {
    "version": "version-1",
    "created_on": "1632779276520673693",
    "name": "gNSI.ssh policy",
    "policy": {
    "allow_rules": [{
    "name": "admin-access",
    "source": {
    "principals": [
    "spiffe://company.com/sa/alice",
    "spiffe://company.com/sa/bob"
    ]
    },
    "request": {
    "paths": [
    "/gnsi.ssh.Ssh/MutateAccountCredentials",
    "/gnsi.ssh.Ssh/MutateHostCredentials"
    ]
    }
    }],
    "deny_rules": [{
    "name": "sales-access",
    "source": {
    "principals": [
    "spiffe://company.com/sa/marge",
    "spiffe://company.com/sa/don"
    ]
    },
    "request": {
    "paths": [
    "/gnsi.ssh.Ssh/MutateAccountCredentials",
    "/gnsi.ssh.Ssh/MutateHostCredentials"
    ]
    }
    }]
    }
    }

    This example would authorize "alice" and "bob" to call
    "MutateHostCredentials" and "MutateAccountCredentials" of "gnsi.ssh.Ssh"
    service.

    The default policy is to permit `gNSI.authz` RPCs.  The authorization of
    all other RPCs is implementation dependent.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Rotate = channel.stream_stream(
                '/gnsi.authz.v1.Authz/Rotate',
                request_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.RotateAuthzRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.RotateAuthzResponse.FromString,
                _registered_method=True)
        self.Probe = channel.unary_unary(
                '/gnsi.authz.v1.Authz/Probe',
                request_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.ProbeRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.ProbeResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/gnsi.authz.v1.Authz/Get',
                request_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.GetRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.GetResponse.FromString,
                _registered_method=True)


class AuthzServicer(object):
    """The gRPC-level Authorization Policy Management Service exported by targets.


    Authorization Policy defines which principals are permitted to access which
    resource(s). Resources are individual RPC methods scoped by their path(s).
    The policy is expressed in JSON format, following the schema in
    https://github.com/grpc/proposal/blob/master/A43-grpc-authorization-api.md
    and the protobuf in the
    README(https://github.com/openconfig/gnsi/blob/main/authz/README.md).

    Example UploadRequest with policy:

    {
    "version": "version-1",
    "created_on": "1632779276520673693",
    "name": "gNSI.ssh policy",
    "policy": {
    "allow_rules": [{
    "name": "admin-access",
    "source": {
    "principals": [
    "spiffe://company.com/sa/alice",
    "spiffe://company.com/sa/bob"
    ]
    },
    "request": {
    "paths": [
    "/gnsi.ssh.Ssh/MutateAccountCredentials",
    "/gnsi.ssh.Ssh/MutateHostCredentials"
    ]
    }
    }],
    "deny_rules": [{
    "name": "sales-access",
    "source": {
    "principals": [
    "spiffe://company.com/sa/marge",
    "spiffe://company.com/sa/don"
    ]
    },
    "request": {
    "paths": [
    "/gnsi.ssh.Ssh/MutateAccountCredentials",
    "/gnsi.ssh.Ssh/MutateHostCredentials"
    ]
    }
    }]
    }
    }

    This example would authorize "alice" and "bob" to call
    "MutateHostCredentials" and "MutateAccountCredentials" of "gnsi.ssh.Ssh"
    service.

    The default policy is to permit `gNSI.authz` RPCs.  The authorization of
    all other RPCs is implementation dependent.

    """

    def Rotate(self, request_iterator, context):
        """Rotate will replace an existing gRPC-level Authorization Policy on the
        target.

        If the stream is broken or any of the steps fail the
        target must rollback to the original state, i.e. revert any changes to
        the gRPC-level Authorization Policy made during this RPC.

        Note that only one such RPC can be in progress. An attempt to call this
        RPC while another is already in progress will be rejected with the
        `UNAVAILABLE` gRPC error.

        The following describes the sequence of messages that must be exchanged
        in the Rotate() RPC.

        Sequence of expected messages:
        Step 1: Start the stream
        Client ----> Rotate() RPC stream begin ------> Target

        Step 2: Send gRPC-level Authorization Policy to Target.
        Client --> UploadRequest(authz_policy) ----> Target
        Client <-- UploadResponse <--- Target

        Step 3 (optional): Test/Validation by the client.
        During this step client attempts to call a RPC that is allowed
        in the new policy and validates that the new policy "works".
        Additionally the client should call a RPC that is not allowed and
        the attempt must fail proving that the gRPC-level Authorization Policy
        "works".
        Once verified, the client then proceeds to finalize the rotation.
        If the new verification did not succeed the client will cancel the
        RPC thereby forcing the target to rollback of the new gRPC-level
        Authorization Policy.

        Step 4: Final commit.
        Client ---> FinalizeRequest ----> Target

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Probe(self, request, context):
        """Probe allows for evaluation of the gRPC-level Authorization Policy engine
        response to a gRPC call performed by a user.
        The response is based on the instance of policy specified in the request
        and is evaluated without actually performing the gRPC call.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get returns current instance of the gRPC-level Authorization Policy
        together with its version and created-on information.
        If no policy has been set, Get() returns FAILED_PRECONDITION.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthzServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Rotate': grpc.stream_stream_rpc_method_handler(
                    servicer.Rotate,
                    request_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.RotateAuthzRequest.FromString,
                    response_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.RotateAuthzResponse.SerializeToString,
            ),
            'Probe': grpc.unary_unary_rpc_method_handler(
                    servicer.Probe,
                    request_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.ProbeRequest.FromString,
                    response_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.ProbeResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.GetRequest.FromString,
                    response_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.GetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gnsi.authz.v1.Authz', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gnsi.authz.v1.Authz', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Authz(object):
    """The gRPC-level Authorization Policy Management Service exported by targets.


    Authorization Policy defines which principals are permitted to access which
    resource(s). Resources are individual RPC methods scoped by their path(s).
    The policy is expressed in JSON format, following the schema in
    https://github.com/grpc/proposal/blob/master/A43-grpc-authorization-api.md
    and the protobuf in the
    README(https://github.com/openconfig/gnsi/blob/main/authz/README.md).

    Example UploadRequest with policy:

    {
    "version": "version-1",
    "created_on": "1632779276520673693",
    "name": "gNSI.ssh policy",
    "policy": {
    "allow_rules": [{
    "name": "admin-access",
    "source": {
    "principals": [
    "spiffe://company.com/sa/alice",
    "spiffe://company.com/sa/bob"
    ]
    },
    "request": {
    "paths": [
    "/gnsi.ssh.Ssh/MutateAccountCredentials",
    "/gnsi.ssh.Ssh/MutateHostCredentials"
    ]
    }
    }],
    "deny_rules": [{
    "name": "sales-access",
    "source": {
    "principals": [
    "spiffe://company.com/sa/marge",
    "spiffe://company.com/sa/don"
    ]
    },
    "request": {
    "paths": [
    "/gnsi.ssh.Ssh/MutateAccountCredentials",
    "/gnsi.ssh.Ssh/MutateHostCredentials"
    ]
    }
    }]
    }
    }

    This example would authorize "alice" and "bob" to call
    "MutateHostCredentials" and "MutateAccountCredentials" of "gnsi.ssh.Ssh"
    service.

    The default policy is to permit `gNSI.authz` RPCs.  The authorization of
    all other RPCs is implementation dependent.

    """

    @staticmethod
    def Rotate(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/gnsi.authz.v1.Authz/Rotate',
            github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.RotateAuthzRequest.SerializeToString,
            github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.RotateAuthzResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Probe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gnsi.authz.v1.Authz/Probe',
            github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.ProbeRequest.SerializeToString,
            github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.ProbeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gnsi.authz.v1.Authz/Get',
            github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.GetRequest.SerializeToString,
            github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2.GetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
