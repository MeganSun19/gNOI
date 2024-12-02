# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from github.com.openconfig.gnsi.certz import certz_pb2 as github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2

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
        + f' but the generated code in github.com/openconfig/gnsi/certz/certz_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CertzStub(object):
    """The Certificate Management Service exported by targets.

    This service exports multiple RPCs. Three of them are used to manage SSL
    profiles, one to check if the target has the capability to create a CSR and
    one, Rotate(), which is used to rotate (i.e. update or replace) an existing
    certificate, an existing trust bundle and/or an existing certificate
    revocation list bundle that are part of a SSL profile on a target.

    Note that for the sake of data consistency and API simplicity, only one RPC
    may be in progress at a time. An attempt to initiate another RPC while
    one is already in progress will be rejected with an error.

    The service makes an assumption that the credentials it manages are
    organized in the following _logical_ topology.

    Target (as seen from gNSI.certificate microservice point of view)
    |
    +-+ SSL profile for gNXI; always present and immutable;
    | ssl_profile_id := "system_default_profile"
    | |
    | +-+ certificate
    | | +- certificate (with public key)
    | | +- private key
    | |
    | +-+ trust bundle (Certificate Authority certificates)
    | | +- CA Root certificate
    | | +- CA Intermediate Certificate
    | |
    | +-+ Certificate Revocation List bundle
    | | +-+ Certificate Revocation List A
    | | +-+ Certificate Revocation List B
    | |
    | +- authentication policy
    |
    +-+ Another SSL profile used by another service
    |
    +-+ certificate
    | +- certificate (with public key)
    | +- private key
    |
    +-+ trust bundle (Certificate Authority certificates)
    | +- CA Root certificate
    | +- CA Intermediate Certificate
    |
    +-+ Certificate Revocation List bundle
    | +-+ Certificate Revocation List A
    | +-+ Certificate Revocation List B
    |
    +- authentication policy

    As shown above the gNSI.certz manages certificates (public and private keys),
    trust bundles (Certificate Authority chain of certificates) and Certificate
    Revocation List (CRL) bundles grouped into SSL profiles.
    Each profile has a unique ID and consists of exactly one certificate, one
    CA trust bundle and one CRL bundle.
    There is at least one SSL profile present on the target, the one that is used
    by all gNxI microservices. It is created during the bootstrap phase and
    cannot be removed.
    Other services that require credentials _can_ use the same SSL profile as
    the gNxI server or they can use a SSL profiles that is created using
    the `AddProfile()` RPC. In any case, the assignment of a SSL profile to
    a service is done by modifying the `/oc-sys:system/
    oc-sys-grpc:grpc-servers/oc-sys-grpc:grpc-server/oc-sys-grpc:config/
    oc-sys-grpc:certificate-id` OpenConfig leaf.

    Note that this architecture implies that every operation performed
    on a credential that is part of a SSL profile specified in the request
    changes the credential at the same time for all services configured to use
    this particular SSL profile.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Rotate = channel.stream_stream(
                '/gnsi.certz.v1.Certz/Rotate',
                request_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.RotateCertificateRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.RotateCertificateResponse.FromString,
                _registered_method=True)
        self.AddProfile = channel.unary_unary(
                '/gnsi.certz.v1.Certz/AddProfile',
                request_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.AddProfileRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.AddProfileResponse.FromString,
                _registered_method=True)
        self.DeleteProfile = channel.unary_unary(
                '/gnsi.certz.v1.Certz/DeleteProfile',
                request_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.DeleteProfileRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.DeleteProfileResponse.FromString,
                _registered_method=True)
        self.GetProfileList = channel.unary_unary(
                '/gnsi.certz.v1.Certz/GetProfileList',
                request_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.GetProfileListRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.GetProfileListResponse.FromString,
                _registered_method=True)
        self.CanGenerateCSR = channel.unary_unary(
                '/gnsi.certz.v1.Certz/CanGenerateCSR',
                request_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.CanGenerateCSRRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.CanGenerateCSRResponse.FromString,
                _registered_method=True)


class CertzServicer(object):
    """The Certificate Management Service exported by targets.

    This service exports multiple RPCs. Three of them are used to manage SSL
    profiles, one to check if the target has the capability to create a CSR and
    one, Rotate(), which is used to rotate (i.e. update or replace) an existing
    certificate, an existing trust bundle and/or an existing certificate
    revocation list bundle that are part of a SSL profile on a target.

    Note that for the sake of data consistency and API simplicity, only one RPC
    may be in progress at a time. An attempt to initiate another RPC while
    one is already in progress will be rejected with an error.

    The service makes an assumption that the credentials it manages are
    organized in the following _logical_ topology.

    Target (as seen from gNSI.certificate microservice point of view)
    |
    +-+ SSL profile for gNXI; always present and immutable;
    | ssl_profile_id := "system_default_profile"
    | |
    | +-+ certificate
    | | +- certificate (with public key)
    | | +- private key
    | |
    | +-+ trust bundle (Certificate Authority certificates)
    | | +- CA Root certificate
    | | +- CA Intermediate Certificate
    | |
    | +-+ Certificate Revocation List bundle
    | | +-+ Certificate Revocation List A
    | | +-+ Certificate Revocation List B
    | |
    | +- authentication policy
    |
    +-+ Another SSL profile used by another service
    |
    +-+ certificate
    | +- certificate (with public key)
    | +- private key
    |
    +-+ trust bundle (Certificate Authority certificates)
    | +- CA Root certificate
    | +- CA Intermediate Certificate
    |
    +-+ Certificate Revocation List bundle
    | +-+ Certificate Revocation List A
    | +-+ Certificate Revocation List B
    |
    +- authentication policy

    As shown above the gNSI.certz manages certificates (public and private keys),
    trust bundles (Certificate Authority chain of certificates) and Certificate
    Revocation List (CRL) bundles grouped into SSL profiles.
    Each profile has a unique ID and consists of exactly one certificate, one
    CA trust bundle and one CRL bundle.
    There is at least one SSL profile present on the target, the one that is used
    by all gNxI microservices. It is created during the bootstrap phase and
    cannot be removed.
    Other services that require credentials _can_ use the same SSL profile as
    the gNxI server or they can use a SSL profiles that is created using
    the `AddProfile()` RPC. In any case, the assignment of a SSL profile to
    a service is done by modifying the `/oc-sys:system/
    oc-sys-grpc:grpc-servers/oc-sys-grpc:grpc-server/oc-sys-grpc:config/
    oc-sys-grpc:certificate-id` OpenConfig leaf.

    Note that this architecture implies that every operation performed
    on a credential that is part of a SSL profile specified in the request
    changes the credential at the same time for all services configured to use
    this particular SSL profile.

    """

    def Rotate(self, request_iterator, context):
        """Rotate will replace an existing device certificate and/or CA certificates
        (trust bundle) or/and a certificate revocation list bundle on the target.
        The new device certificate can be created from a target-generated or
        client-generated CSR. In the latter case the client has to provide
        corresponding private key with the signed certificate.
        If the stream is broken or any of the steps fail the target must rollback
        to the original state, i.e. revert any changes to the certificate,
        CA certificates and the Certificate Revocation List bundle.

        The following describes a number of use cases each presenting the expected
        sequence of message exchange.

        Case 1: Client generates the CSR, gets it signed and then uploads it.

        Step 1: Start the stream
        Client <---- Rotate() RPC stream begin ------> Target

        Step 2: CSR Generation and certificate signing
        Client generates the CSR and gets the certificate signed by the CA.

        Step 3: Send Certificate and optional content to the Target.
        mandatory: signed certificate with private key
        optional: trust bundle - Certificate Authority certificate chain
        optional: certificate revocation list bundle
        optional: authentication policy
        Client --> UploadRequest(certificate, [trust_bundle],
        [certificate_revocation_list],
        [authentication_policy]) ----> Target
        Client <-- UploadResponse <--- Target

        Step 4 (optional): Test/Validation by the client.
        During this step client attempts to create a new connection to
        the target using the new certificates and validates that
        the certificates "work".
        If the new connection cannot be completed the client will cancel the
        RPC thereby forcing the target to rollback all the certificates.
        If new certificate revocation list bundle has been uploaded in step 3,
        during this step the client also attempts to establish a new connection
        to the target using revoked certificate(s) - the attempt must fail
        proving that the certificates have been revoked.
        Once verified, the client then proceeds to finalize the rotation.

        Step 5: Final commit.
        Client ---> FinalizeRequest ----> Target

        Case 2: Target generates the CSR, client gets it signed and uploads it.

        Step 1: Start the stream
        Client <---- Rotate() RPC stream begin ------> Target

        Step 2: CSR
        Client -----> GenerateCSRRequest----> Target
        Client <----- GenerateCSRResponse <--- Target

        Step 3: Certificate Signing
        Client gets the certificate signed by the CA.

        Step 4: Send Certificate and optional content to the Target.
        mandatory: signed certificate without private key
        optional: trust bundle - Certificate Authority certificate chain
        optional: certificate revocation list bundle
        optional: authentication policy
        Client --> UploadRequest(certificate, [trust_bundle],
        [certificate_revocation_list],
        [authentication_policy]) ----> Target
        Client <-- UploadResponse <--- Target

        Step 5: Test/Validation by the client.
        During this step client attempts to create a new connection to
        the target using the new certificates and validates that
        the certificates "work".
        If the new connection cannot be completed the client will cancel the
        RPC thereby forcing the target to rollback all the certificates.
        If new certificate revocation list bundle has been uploaded in step 4,
        during this step the client also attempts to establish a new connection
        to the target using revoked certificate(s) - the attempt must fail
        proving that the certificates have been revoked.
        Once verified, the client then proceeds to finalize the rotation.

        Step 6: Final commit.
        Client ---> FinalizeRequest ----> Target

        Case 3: Client changes only trust bundle on the Target.

        Step 1: Start the stream
        Client <---- Rotate() RPC stream begin ------> Target

        Step 2: Send CA Certificate Bundle to the Target.
        mandatory: trust bundle - Certificate Authority chain
        Client --> UploadRequest(trust_bundle) ----> Target
        Client <-- UploadResponse <--- Target

        Step 3 (optional): Test/Validation by the client.
        During this step client attempts to create a new connection to
        the target using a new certificate that can be validated using the new
        trust bundle and validates that the CA certificates "work".
        If the new connection cannot be completed the client will cancel the
        RPC thereby forcing the target to rollback all the certificates.
        If new certificate revocation list bundle has been uploaded in step 2,
        during this step the client also attempts to establish a new connection
        to the target using revoked certificate(s) - the attempt must fail
        proving that the certificates have been revoked.
        Once verified, the client then proceeds to finalize the rotation.

        Step 4: Final commit.
        Client ---> FinalizeRequest ----> Target

        Case 4: Client provides certificate revocation list bundle to the Target.

        Step 1: Start the stream
        Client <---- Rotate() RPC stream begin ------> Target

        Step 2: Send certificate revocation list bundle to the target.
        mandatory: certificate revocation list bundle
        Client --> UploadRequest(certificate_revocation_list) ----> Target
        Client <-- UploadResponse <--- Target

        Step 3 (optional): Test/Validation by the client.
        During this step the client attempts to establish a new connection
        to the target using revoked certificate(s) - the attempt must fail
        proving that the certificates have been revoked.
        If the new connection can be completed the client will cancel the
        RPC thereby forcing the target to rollback all the certificates.
        Once verified, the client then proceeds to finalize the rotation.

        Step 4: Final commit.
        Client ---> FinalizeRequest ----> Target

        Case 5: Client provides authentication policy to the Target.

        Step 1: Start the stream
        Client <---- Rotate() RPC stream begin ------> Target

        Step 2: Send authentication policy to the target.
        mandatory: authentication policy
        Client --> UploadRequest(authentication_policy) ----> Target
        Client <-- UploadResponse <--- Target

        Step 3 (optional): Test/Validation by the client.
        During this step the client attempts to establish a new connection
        to the target using certificate(s) signed with incorrect CA -
        the attempt must fail proving that the authentication policy works.
        If the new connection can be completed the client will cancel the
        RPC thereby forcing the target to rollback the authentication policy.
        Once verified, the client then proceeds to finalize the rotation.

        Step 4: Final commit.
        Client ---> FinalizeRequest ----> Target

        A `Rotate` RPC has a context of a single `profile` -- it is not
        permitted to multiplex operations for multiple profiles within the
        context of the same RPC (i.e., requesting a CSR for profile A, followed
        by requesting a CSR for profile B using the same `Rotate` RPC). In the
        case that such multiplexing is observed, the server should respond with
        an error specifying `InvalidArgument` as the status code.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddProfile(self, request, context):
        """AddProfile is part of SSL profile management and allows for adding new
        SSL profile.
        When a SSL profile is added all its elements, i.e. certificate, CA trust
        bundle and a set of certificate revocation lists are created and they are
        empty, so before they can be used they have to be 'rotated' using
        the `Rotate()` RPC.
        Note that an attempt to add an already existing profile will be rejected
        with an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProfile(self, request, context):
        """DeleteProfile is part of SSL profile management and allows for removing
        an existing SSL profile.
        Note that an attempt to remove a not existing profile will result
        in an error.
        Not also that the profile used by the gNxI server cannot be deleted and an
        attempt to remove it will rejected with an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProfileList(self, request, context):
        """GetProfileList is part of SSL profile management and allows for
        retrieving a list of IDs of SSL profiles present on the target.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CanGenerateCSR(self, request, context):
        """An RPC to ask a target if it can generate a Certificate Signing Request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CertzServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Rotate': grpc.stream_stream_rpc_method_handler(
                    servicer.Rotate,
                    request_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.RotateCertificateRequest.FromString,
                    response_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.RotateCertificateResponse.SerializeToString,
            ),
            'AddProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.AddProfile,
                    request_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.AddProfileRequest.FromString,
                    response_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.AddProfileResponse.SerializeToString,
            ),
            'DeleteProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProfile,
                    request_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.DeleteProfileRequest.FromString,
                    response_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.DeleteProfileResponse.SerializeToString,
            ),
            'GetProfileList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProfileList,
                    request_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.GetProfileListRequest.FromString,
                    response_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.GetProfileListResponse.SerializeToString,
            ),
            'CanGenerateCSR': grpc.unary_unary_rpc_method_handler(
                    servicer.CanGenerateCSR,
                    request_deserializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.CanGenerateCSRRequest.FromString,
                    response_serializer=github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.CanGenerateCSRResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gnsi.certz.v1.Certz', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gnsi.certz.v1.Certz', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Certz(object):
    """The Certificate Management Service exported by targets.

    This service exports multiple RPCs. Three of them are used to manage SSL
    profiles, one to check if the target has the capability to create a CSR and
    one, Rotate(), which is used to rotate (i.e. update or replace) an existing
    certificate, an existing trust bundle and/or an existing certificate
    revocation list bundle that are part of a SSL profile on a target.

    Note that for the sake of data consistency and API simplicity, only one RPC
    may be in progress at a time. An attempt to initiate another RPC while
    one is already in progress will be rejected with an error.

    The service makes an assumption that the credentials it manages are
    organized in the following _logical_ topology.

    Target (as seen from gNSI.certificate microservice point of view)
    |
    +-+ SSL profile for gNXI; always present and immutable;
    | ssl_profile_id := "system_default_profile"
    | |
    | +-+ certificate
    | | +- certificate (with public key)
    | | +- private key
    | |
    | +-+ trust bundle (Certificate Authority certificates)
    | | +- CA Root certificate
    | | +- CA Intermediate Certificate
    | |
    | +-+ Certificate Revocation List bundle
    | | +-+ Certificate Revocation List A
    | | +-+ Certificate Revocation List B
    | |
    | +- authentication policy
    |
    +-+ Another SSL profile used by another service
    |
    +-+ certificate
    | +- certificate (with public key)
    | +- private key
    |
    +-+ trust bundle (Certificate Authority certificates)
    | +- CA Root certificate
    | +- CA Intermediate Certificate
    |
    +-+ Certificate Revocation List bundle
    | +-+ Certificate Revocation List A
    | +-+ Certificate Revocation List B
    |
    +- authentication policy

    As shown above the gNSI.certz manages certificates (public and private keys),
    trust bundles (Certificate Authority chain of certificates) and Certificate
    Revocation List (CRL) bundles grouped into SSL profiles.
    Each profile has a unique ID and consists of exactly one certificate, one
    CA trust bundle and one CRL bundle.
    There is at least one SSL profile present on the target, the one that is used
    by all gNxI microservices. It is created during the bootstrap phase and
    cannot be removed.
    Other services that require credentials _can_ use the same SSL profile as
    the gNxI server or they can use a SSL profiles that is created using
    the `AddProfile()` RPC. In any case, the assignment of a SSL profile to
    a service is done by modifying the `/oc-sys:system/
    oc-sys-grpc:grpc-servers/oc-sys-grpc:grpc-server/oc-sys-grpc:config/
    oc-sys-grpc:certificate-id` OpenConfig leaf.

    Note that this architecture implies that every operation performed
    on a credential that is part of a SSL profile specified in the request
    changes the credential at the same time for all services configured to use
    this particular SSL profile.

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
            '/gnsi.certz.v1.Certz/Rotate',
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.RotateCertificateRequest.SerializeToString,
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.RotateCertificateResponse.FromString,
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
    def AddProfile(request,
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
            '/gnsi.certz.v1.Certz/AddProfile',
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.AddProfileRequest.SerializeToString,
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.AddProfileResponse.FromString,
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
    def DeleteProfile(request,
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
            '/gnsi.certz.v1.Certz/DeleteProfile',
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.DeleteProfileRequest.SerializeToString,
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.DeleteProfileResponse.FromString,
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
    def GetProfileList(request,
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
            '/gnsi.certz.v1.Certz/GetProfileList',
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.GetProfileListRequest.SerializeToString,
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.GetProfileListResponse.FromString,
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
    def CanGenerateCSR(request,
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
            '/gnsi.certz.v1.Certz/CanGenerateCSR',
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.CanGenerateCSRRequest.SerializeToString,
            github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2.CanGenerateCSRResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
