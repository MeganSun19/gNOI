# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: github.com/openconfig/gnsi/certz/certz.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'github.com/openconfig/gnsi/certz/certz.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,github.com/openconfig/gnsi/certz/certz.proto\x12\rgnsi.certz.v1\x1a\x19google/protobuf/any.proto\"\x8b\x02\n\x18RotateCertificateRequest\x12\x17\n\x0f\x66orce_overwrite\x18\x01 \x01(\x08\x12\x16\n\x0essl_profile_id\x18\x02 \x01(\t\x12\x39\n\x0cgenerate_csr\x18\x03 \x01(\x0b\x32!.gnsi.certz.v1.GenerateCSRRequestH\x00\x12\x34\n\x0c\x63\x65rtificates\x18\x04 \x01(\x0b\x32\x1c.gnsi.certz.v1.UploadRequestH\x00\x12;\n\x11\x66inalize_rotation\x18\x05 \x01(\x0b\x32\x1e.gnsi.certz.v1.FinalizeRequestH\x00\x42\x10\n\x0erotate_request\"\xa2\x01\n\x19RotateCertificateResponse\x12;\n\rgenerated_csr\x18\x01 \x01(\x0b\x32\".gnsi.certz.v1.GenerateCSRResponseH\x00\x12\x35\n\x0c\x63\x65rtificates\x18\x02 \x01(\x0b\x32\x1d.gnsi.certz.v1.UploadResponseH\x00\x42\x11\n\x0frotate_response\"\x11\n\x0f\x46inalizeRequest\"+\n\x11\x41\x64\x64ProfileRequest\x12\x16\n\x0essl_profile_id\x18\x01 \x01(\t\"\x14\n\x12\x41\x64\x64ProfileResponse\".\n\x14\x44\x65leteProfileRequest\x12\x16\n\x0essl_profile_id\x18\x01 \x01(\t\"\x17\n\x15\x44\x65leteProfileResponse\"\x17\n\x15GetProfileListRequest\"1\n\x16GetProfileListResponse\x12\x17\n\x0fssl_profile_ids\x18\x01 \x03(\t\"H\n\x0eV3ExtensionSAN\x12\x0b\n\x03\x64ns\x18\x01 \x03(\t\x12\x0e\n\x06\x65mails\x18\x02 \x03(\t\x12\x0b\n\x03ips\x18\x03 \x03(\t\x12\x0c\n\x04uris\x18\x04 \x03(\t\"\xff\x01\n\tCSRParams\x12*\n\tcsr_suite\x18\x01 \x01(\x0e\x32\x17.gnsi.certz.v1.CSRSuite\x12\x13\n\x0b\x63ommon_name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\x12\x14\n\x0corganization\x18\x06 \x01(\t\x12\x1b\n\x13organizational_unit\x18\x07 \x01(\t\x12\x12\n\nip_address\x18\x08 \x01(\t\x12\x10\n\x08\x65mail_id\x18\t \x01(\t\x12*\n\x03san\x18\n \x01(\x0b\x32\x1d.gnsi.certz.v1.V3ExtensionSAN\"A\n\x15\x43\x61nGenerateCSRRequest\x12(\n\x06params\x18\x01 \x01(\x0b\x32\x18.gnsi.certz.v1.CSRParams\".\n\x16\x43\x61nGenerateCSRResponse\x12\x14\n\x0c\x63\x61n_generate\x18\x04 \x01(\x08\"t\n\x10\x43\x65rtificateChain\x12/\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0b\x32\x1a.gnsi.certz.v1.Certificate\x12/\n\x06parent\x18\x02 \x01(\x0b\x32\x1f.gnsi.certz.v1.CertificateChain\"\"\n\x0bTrustBundle\x12\x13\n\x0bpkcs7_block\x18\x01 \x01(\t\"\xb5\x04\n\x0b\x43\x65rtificate\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.gnsi.certz.v1.CertificateType\x12\x34\n\x08\x65ncoding\x18\x02 \x01(\x0e\x32\".gnsi.certz.v1.CertificateEncoding\x12\x17\n\x0b\x63\x65rtificate\x18\x03 \x01(\x0c\x42\x02\x18\x01\x12\x17\n\x0bprivate_key\x18\x04 \x01(\x0c\x42\x02\x18\x01\x12\x19\n\x0fraw_certificate\x18\x05 \x01(\x0cH\x00\x12<\n\x0b\x63\x65rt_source\x18\x06 \x01(\x0e\x32%.gnsi.certz.v1.Certificate.CertSourceH\x00\x12\x19\n\x0fraw_private_key\x18\x07 \x01(\x0cH\x01\x12:\n\nkey_source\x18\x08 \x01(\x0e\x32$.gnsi.certz.v1.Certificate.KeySourceH\x01\"Z\n\nCertSource\x12\x1b\n\x17\x43\x45RT_SOURCE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x43\x45RT_SOURCE_OIDEVID\x10\x01\x12\x16\n\x12\x43\x45RT_SOURCE_IDEVID\x10\x02\"\\\n\tKeySource\x12\x1a\n\x16KEY_SOURCE_UNSPECIFIED\x10\x00\x12\x19\n\x15KEY_SOURCE_IDEVID_TPM\x10\x01\x12\x18\n\x14KEY_SOURCE_GENERATED\x10\x02\x42\x12\n\x10\x63\x65rtificate_typeB\x12\n\x10private_key_type\"\xb0\x01\n\x19\x43\x65rtificateRevocationList\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.gnsi.certz.v1.CertificateType\x12\x34\n\x08\x65ncoding\x18\x02 \x01(\x0e\x32\".gnsi.certz.v1.CertificateEncoding\x12#\n\x1b\x63\x65rtificate_revocation_list\x18\x03 \x01(\x0c\x12\n\n\x02id\x18\x04 \x01(\t\"q\n\x1f\x43\x65rtificateRevocationListBundle\x12N\n\x1c\x63\x65rtificate_revocation_lists\x18\x01 \x03(\x0b\x32(.gnsi.certz.v1.CertificateRevocationList\"L\n\x14\x41uthenticationPolicy\x12*\n\nserialized\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06policy\"\x84\x04\n\x06\x45ntity\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x12\n\ncreated_on\x18\x02 \x01(\x04\x12<\n\x11\x63\x65rtificate_chain\x18\x03 \x01(\x0b\x32\x1f.gnsi.certz.v1.CertificateChainH\x00\x12\x37\n\x0ctrust_bundle\x18\x04 \x01(\x0b\x32\x1f.gnsi.certz.v1.CertificateChainH\x00\x12\\\n\"certificate_revocation_list_bundle\x18\x05 \x01(\x0b\x32..gnsi.certz.v1.CertificateRevocationListBundleH\x00\x12\x44\n\x15\x61uthentication_policy\x18\x06 \x01(\x0b\x32#.gnsi.certz.v1.AuthenticationPolicyH\x00\x12\x38\n\x0f\x65xisting_entity\x18\x07 \x01(\x0b\x32\x1d.gnsi.certz.v1.ExistingEntityH\x00\x12<\n\x12trust_bundle_pcks7\x18\x08 \x01(\x0b\x32\x1a.gnsi.certz.v1.TrustBundleB\x02\x18\x01H\x00\x12\x38\n\x12trust_bundle_pkcs7\x18\t \x01(\x0b\x32\x1a.gnsi.certz.v1.TrustBundleH\x00\x42\x08\n\x06\x65ntity\"\xaf\x02\n\x0e\x45xistingEntity\x12\x16\n\x0essl_profile_id\x18\x01 \x01(\t\x12=\n\x0b\x65ntity_type\x18\x02 \x01(\x0e\x32(.gnsi.certz.v1.ExistingEntity.EntityType\"\xc5\x01\n\nEntityType\x12\x1b\n\x17\x45NTITY_TYPE_UNSPECIFIED\x10\x00\x12!\n\x1d\x45NTITY_TYPE_CERTIFICATE_CHAIN\x10\x01\x12\x1c\n\x18\x45NTITY_TYPE_TRUST_BUNDLE\x10\x02\x12\x32\n.ENTITY_TYPE_CERTIFICATE_REVOCATION_LIST_BUNDLE\x10\x03\x12%\n!ENTITY_TYPE_AUTHENTICATION_POLICY\x10\x04\"8\n\rUploadRequest\x12\'\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x15.gnsi.certz.v1.Entity\"\x10\n\x0eUploadResponse\"\xa4\x01\n\x19\x43\x65rtificateSigningRequest\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.gnsi.certz.v1.CertificateType\x12\x34\n\x08\x65ncoding\x18\x02 \x01(\x0e\x32\".gnsi.certz.v1.CertificateEncoding\x12#\n\x1b\x63\x65rtificate_signing_request\x18\x03 \x01(\x0c\">\n\x12GenerateCSRRequest\x12(\n\x06params\x18\x01 \x01(\x0b\x32\x18.gnsi.certz.v1.CSRParams\"d\n\x13GenerateCSRResponse\x12M\n\x1b\x63\x65rtificate_signing_request\x18\x01 \x01(\x0b\x32(.gnsi.certz.v1.CertificateSigningRequest*\xcd\n\n\x08\x43SRSuite\x12\x1f\n\x1b\x43SRSUITE_CIPHER_UNSPECIFIED\x10\x00\x12\x41\n=CSRSUITE_X509_KEY_TYPE_RSA_2048_SIGNATURE_ALGORITHM_SHA_2_256\x10\x01\x12\x41\n=CSRSUITE_X509_KEY_TYPE_RSA_2048_SIGNATURE_ALGORITHM_SHA_2_384\x10\x02\x12\x41\n=CSRSUITE_X509_KEY_TYPE_RSA_2048_SIGNATURE_ALGORITHM_SHA_2_512\x10\x03\x12\x41\n=CSRSUITE_X509_KEY_TYPE_RSA_3072_SIGNATURE_ALGORITHM_SHA_2_256\x10\x04\x12\x41\n=CSRSUITE_X509_KEY_TYPE_RSA_3072_SIGNATURE_ALGORITHM_SHA_2_384\x10\x05\x12\x41\n=CSRSUITE_X509_KEY_TYPE_RSA_3072_SIGNATURE_ALGORITHM_SHA_2_512\x10\x06\x12\x41\n=CSRSUITE_X509_KEY_TYPE_RSA_4096_SIGNATURE_ALGORITHM_SHA_2_256\x10\x07\x12\x41\n=CSRSUITE_X509_KEY_TYPE_RSA_4096_SIGNATURE_ALGORITHM_SHA_2_384\x10\x08\x12\x41\n=CSRSUITE_X509_KEY_TYPE_RSA_4096_SIGNATURE_ALGORITHM_SHA_2_512\x10\t\x12I\nECSRSUITE_X509_KEY_TYPE_ECDSA_PRIME256V1_SIGNATURE_ALGORITHM_SHA_2_256\x10\n\x12I\nECSRSUITE_X509_KEY_TYPE_ECDSA_PRIME256V1_SIGNATURE_ALGORITHM_SHA_2_384\x10\x0b\x12I\nECSRSUITE_X509_KEY_TYPE_ECDSA_PRIME256V1_SIGNATURE_ALGORITHM_SHA_2_512\x10\x0c\x12H\nDCSRSUITE_X509_KEY_TYPE_ECDSA_SECP384R1_SIGNATURE_ALGORITHM_SHA_2_256\x10\r\x12H\nDCSRSUITE_X509_KEY_TYPE_ECDSA_SECP384R1_SIGNATURE_ALGORITHM_SHA_2_384\x10\x0e\x12H\nDCSRSUITE_X509_KEY_TYPE_ECDSA_SECP384R1_SIGNATURE_ALGORITHM_SHA_2_512\x10\x0f\x12H\nDCSRSUITE_X509_KEY_TYPE_ECDSA_SECP521R1_SIGNATURE_ALGORITHM_SHA_2_256\x10\x10\x12H\nDCSRSUITE_X509_KEY_TYPE_ECDSA_SECP521R1_SIGNATURE_ALGORITHM_SHA_2_384\x10\x11\x12H\nDCSRSUITE_X509_KEY_TYPE_ECDSA_SECP521R1_SIGNATURE_ALGORITHM_SHA_2_512\x10\x12\x12(\n$CSRSUITE_X509_KEY_TYPE_EDDSA_ED25519\x10\x13*N\n\x0f\x43\x65rtificateType\x12 \n\x1c\x43\x45RTIFICATE_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43\x45RTIFICATE_TYPE_X509\x10\x01*\x95\x01\n\x13\x43\x65rtificateEncoding\x12$\n CERTIFICATE_ENCODING_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x43\x45RTIFICATE_ENCODING_PEM\x10\x01\x12\x1c\n\x18\x43\x45RTIFICATE_ENCODING_DER\x10\x02\x12\x1c\n\x18\x43\x45RTIFICATE_ENCODING_CRT\x10\x03\x32\xd5\x03\n\x05\x43\x65rtz\x12_\n\x06Rotate\x12\'.gnsi.certz.v1.RotateCertificateRequest\x1a(.gnsi.certz.v1.RotateCertificateResponse(\x01\x30\x01\x12Q\n\nAddProfile\x12 .gnsi.certz.v1.AddProfileRequest\x1a!.gnsi.certz.v1.AddProfileResponse\x12Z\n\rDeleteProfile\x12#.gnsi.certz.v1.DeleteProfileRequest\x1a$.gnsi.certz.v1.DeleteProfileResponse\x12]\n\x0eGetProfileList\x12$.gnsi.certz.v1.GetProfileListRequest\x1a%.gnsi.certz.v1.GetProfileListResponse\x12]\n\x0e\x43\x61nGenerateCSR\x12$.gnsi.certz.v1.CanGenerateCSRRequest\x1a%.gnsi.certz.v1.CanGenerateCSRResponseB!Z\x1fgithub.com/openconfig/gnsi/certb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'github.com.openconfig.gnsi.certz.certz_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\037github.com/openconfig/gnsi/cert'
  _globals['_CERTIFICATE'].fields_by_name['certificate']._loaded_options = None
  _globals['_CERTIFICATE'].fields_by_name['certificate']._serialized_options = b'\030\001'
  _globals['_CERTIFICATE'].fields_by_name['private_key']._loaded_options = None
  _globals['_CERTIFICATE'].fields_by_name['private_key']._serialized_options = b'\030\001'
  _globals['_ENTITY'].fields_by_name['trust_bundle_pcks7']._loaded_options = None
  _globals['_ENTITY'].fields_by_name['trust_bundle_pcks7']._serialized_options = b'\030\001'
  _globals['_CSRSUITE']._serialized_start=3536
  _globals['_CSRSUITE']._serialized_end=4893
  _globals['_CERTIFICATETYPE']._serialized_start=4895
  _globals['_CERTIFICATETYPE']._serialized_end=4973
  _globals['_CERTIFICATEENCODING']._serialized_start=4976
  _globals['_CERTIFICATEENCODING']._serialized_end=5125
  _globals['_ROTATECERTIFICATEREQUEST']._serialized_start=91
  _globals['_ROTATECERTIFICATEREQUEST']._serialized_end=358
  _globals['_ROTATECERTIFICATERESPONSE']._serialized_start=361
  _globals['_ROTATECERTIFICATERESPONSE']._serialized_end=523
  _globals['_FINALIZEREQUEST']._serialized_start=525
  _globals['_FINALIZEREQUEST']._serialized_end=542
  _globals['_ADDPROFILEREQUEST']._serialized_start=544
  _globals['_ADDPROFILEREQUEST']._serialized_end=587
  _globals['_ADDPROFILERESPONSE']._serialized_start=589
  _globals['_ADDPROFILERESPONSE']._serialized_end=609
  _globals['_DELETEPROFILEREQUEST']._serialized_start=611
  _globals['_DELETEPROFILEREQUEST']._serialized_end=657
  _globals['_DELETEPROFILERESPONSE']._serialized_start=659
  _globals['_DELETEPROFILERESPONSE']._serialized_end=682
  _globals['_GETPROFILELISTREQUEST']._serialized_start=684
  _globals['_GETPROFILELISTREQUEST']._serialized_end=707
  _globals['_GETPROFILELISTRESPONSE']._serialized_start=709
  _globals['_GETPROFILELISTRESPONSE']._serialized_end=758
  _globals['_V3EXTENSIONSAN']._serialized_start=760
  _globals['_V3EXTENSIONSAN']._serialized_end=832
  _globals['_CSRPARAMS']._serialized_start=835
  _globals['_CSRPARAMS']._serialized_end=1090
  _globals['_CANGENERATECSRREQUEST']._serialized_start=1092
  _globals['_CANGENERATECSRREQUEST']._serialized_end=1157
  _globals['_CANGENERATECSRRESPONSE']._serialized_start=1159
  _globals['_CANGENERATECSRRESPONSE']._serialized_end=1205
  _globals['_CERTIFICATECHAIN']._serialized_start=1207
  _globals['_CERTIFICATECHAIN']._serialized_end=1323
  _globals['_TRUSTBUNDLE']._serialized_start=1325
  _globals['_TRUSTBUNDLE']._serialized_end=1359
  _globals['_CERTIFICATE']._serialized_start=1362
  _globals['_CERTIFICATE']._serialized_end=1927
  _globals['_CERTIFICATE_CERTSOURCE']._serialized_start=1703
  _globals['_CERTIFICATE_CERTSOURCE']._serialized_end=1793
  _globals['_CERTIFICATE_KEYSOURCE']._serialized_start=1795
  _globals['_CERTIFICATE_KEYSOURCE']._serialized_end=1887
  _globals['_CERTIFICATEREVOCATIONLIST']._serialized_start=1930
  _globals['_CERTIFICATEREVOCATIONLIST']._serialized_end=2106
  _globals['_CERTIFICATEREVOCATIONLISTBUNDLE']._serialized_start=2108
  _globals['_CERTIFICATEREVOCATIONLISTBUNDLE']._serialized_end=2221
  _globals['_AUTHENTICATIONPOLICY']._serialized_start=2223
  _globals['_AUTHENTICATIONPOLICY']._serialized_end=2299
  _globals['_ENTITY']._serialized_start=2302
  _globals['_ENTITY']._serialized_end=2818
  _globals['_EXISTINGENTITY']._serialized_start=2821
  _globals['_EXISTINGENTITY']._serialized_end=3124
  _globals['_EXISTINGENTITY_ENTITYTYPE']._serialized_start=2927
  _globals['_EXISTINGENTITY_ENTITYTYPE']._serialized_end=3124
  _globals['_UPLOADREQUEST']._serialized_start=3126
  _globals['_UPLOADREQUEST']._serialized_end=3182
  _globals['_UPLOADRESPONSE']._serialized_start=3184
  _globals['_UPLOADRESPONSE']._serialized_end=3200
  _globals['_CERTIFICATESIGNINGREQUEST']._serialized_start=3203
  _globals['_CERTIFICATESIGNINGREQUEST']._serialized_end=3367
  _globals['_GENERATECSRREQUEST']._serialized_start=3369
  _globals['_GENERATECSRREQUEST']._serialized_end=3431
  _globals['_GENERATECSRRESPONSE']._serialized_start=3433
  _globals['_GENERATECSRRESPONSE']._serialized_end=3533
  _globals['_CERTZ']._serialized_start=5128
  _globals['_CERTZ']._serialized_end=5597
# @@protoc_insertion_point(module_scope)
