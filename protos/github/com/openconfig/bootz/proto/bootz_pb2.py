# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: github.com/openconfig/bootz/proto/bootz.proto
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
    'github.com/openconfig/bootz/proto/bootz.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from github.com.openconfig.gnsi.authz import authz_pb2 as github_dot_com_dot_openconfig_dot_gnsi_dot_authz_dot_authz__pb2
from github.com.openconfig.gnsi.certz import certz_pb2 as github_dot_com_dot_openconfig_dot_gnsi_dot_certz_dot_certz__pb2
from github.com.openconfig.gnsi.credentialz import credentialz_pb2 as github_dot_com_dot_openconfig_dot_gnsi_dot_credentialz_dot_credentialz__pb2
from github.com.openconfig.gnsi.pathz import pathz_pb2 as github_dot_com_dot_openconfig_dot_gnsi_dot_pathz_dot_pathz__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-github.com/openconfig/bootz/proto/bootz.proto\x12\x05\x62ootz\x1a\x1cgoogle/protobuf/struct.proto\x1a,github.com/openconfig/gnsi/authz/authz.proto\x1a,github.com/openconfig/gnsi/certz/certz.proto\x1a\x38github.com/openconfig/gnsi/credentialz/credentialz.proto\x1a,github.com/openconfig/gnsi/pathz/pathz.proto\"\x94\x01\n\x17GetBootstrapDataRequest\x12\x34\n\x12\x63hassis_descriptor\x18\x01 \x01(\x0b\x32\x18.bootz.ChassisDescriptor\x12\x33\n\x12\x63ontrol_card_state\x18\x02 \x01(\x0b\x32\x17.bootz.ControlCardState\x12\x0e\n\x05nonce\x18\xe9\x07 \x01(\t\"\x80\x01\n\x11\x43hassisDescriptor\x12\x14\n\x0cmanufacturer\x18\x01 \x01(\t\x12\x13\n\x0bpart_number\x18\x02 \x01(\t\x12\x15\n\rserial_number\x18\x03 \x01(\t\x12)\n\rcontrol_cards\x18\x04 \x03(\x0b\x32\x12.bootz.ControlCard\"\\\n\x0b\x43ontrolCard\x12\x13\n\x0bpart_number\x18\x01 \x01(\t\x12\x15\n\rserial_number\x18\x02 \x01(\t\x12\x10\n\x04slot\x18\x03 \x01(\x05\x42\x02\x18\x01\x12\x0f\n\x07slot_id\x18\x04 \x01(\t\"\xed\x01\n\x10\x43ontrolCardState\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x39\n\x06status\x18\x02 \x01(\x0e\x32).bootz.ControlCardState.ControlCardStatus\"\x86\x01\n\x11\x43ontrolCardStatus\x12#\n\x1f\x43ONTROL_CARD_STATUS_UNSPECIFIED\x10\x00\x12\'\n#CONTROL_CARD_STATUS_NOT_INITIALIZED\x10\x01\x12#\n\x1f\x43ONTROL_CARD_STATUS_INITIALIZED\x10\x02\"\xa1\x03\n\x15\x42ootstrapDataResponse\x12\x12\n\nserial_num\x18\x01 \x01(\t\x12,\n\x0eintended_image\x18\x02 \x01(\x0b\x32\x14.bootz.SoftwareImage\x12\x1a\n\x12\x62oot_password_hash\x18\x03 \x01(\t\x12\x19\n\x11server_trust_cert\x18\x04 \x01(\t\x12&\n\x0b\x62oot_config\x18\x05 \x01(\x0b\x32\x11.bootz.BootConfig\x12\'\n\x0b\x63redentials\x18\x06 \x01(\x0b\x32\x12.bootz.Credentials\x12+\n\x05pathz\x18\x07 \x01(\x0b\x32\x1c.gnsi.pathz.v1.UploadRequest\x12+\n\x05\x61uthz\x18\x08 \x01(\x0b\x32\x1c.gnsi.authz.v1.UploadRequest\x12\x36\n\x0c\x63\x65rtificates\x18\t \x01(\x0b\x32\x1c.gnsi.certz.v1.UploadRequestB\x02\x18\x01\x12,\n\x0e\x63\x65rtz_profiles\x18\n \x01(\x0b\x32\x14.bootz.CertzProfiles\"6\n\rCertzProfiles\x12%\n\x08profiles\x18\x01 \x03(\x0b\x32\x13.bootz.CertzProfile\"S\n\x0c\x43\x65rtzProfile\x12\x16\n\x0essl_profile_id\x18\x01 \x01(\t\x12+\n\x05\x63\x65rtz\x18\x02 \x01(\x0b\x32\x1c.gnsi.certz.v1.UploadRequest\"U\n\x13\x42ootstrapDataSigned\x12/\n\tresponses\x18\x01 \x03(\x0b\x32\x1c.bootz.BootstrapDataResponse\x12\r\n\x05nonce\x18\x02 \x01(\t\"\xcc\x01\n\x18GetBootstrapDataResponse\x12\x37\n\x0fsigned_response\x18\x01 \x01(\x0b\x32\x1a.bootz.BootstrapDataSignedB\x02\x18\x01\x12\x19\n\x11ownership_voucher\x18\x65 \x01(\x0c\x12\x1d\n\x15ownership_certificate\x18\x66 \x01(\x0c\x12\x1a\n\x12response_signature\x18g \x01(\t\x12!\n\x19serialized_bootstrap_data\x18h \x01(\x0c\"j\n\rSoftwareImage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x15\n\ros_image_hash\x18\x04 \x01(\t\x12\x16\n\x0ehash_algorithm\x18\x05 \x01(\t\"\xc3\x01\n\x0b\x43redentials\x12?\n\x0b\x63redentials\x18\x01 \x03(\x0b\x32*.gnsi.credentialz.v1.AuthorizedKeysRequest\x12:\n\x05users\x18\x02 \x03(\x0b\x32+.gnsi.credentialz.v1.AuthorizedUsersRequest\x12\x37\n\tpasswords\x18\x03 \x03(\x0b\x32$.gnsi.credentialz.v1.PasswordRequest\"\x95\x01\n\nBootConfig\x12)\n\x08metadata\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x15\n\rvendor_config\x18\x02 \x01(\x0c\x12\x11\n\toc_config\x18\x03 \x01(\x0c\x12\x32\n\x11\x62ootloader_config\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xa4\x02\n\x13ReportStatusRequest\x12:\n\x06status\x18\x01 \x01(\x0e\x32*.bootz.ReportStatusRequest.BootstrapStatus\x12\x16\n\x0estatus_message\x18\x02 \x01(\t\x12\'\n\x06states\x18\x03 \x03(\x0b\x32\x17.bootz.ControlCardState\"\x8f\x01\n\x0f\x42ootstrapStatus\x12 \n\x1c\x42OOTSTRAP_STATUS_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x42OOTSTRAP_STATUS_SUCCESS\x10\x01\x12\x1c\n\x18\x42OOTSTRAP_STATUS_FAILURE\x10\x02\x12\x1e\n\x1a\x42OOTSTRAP_STATUS_INITIATED\x10\x03\"\x0f\n\rEmptyResponse*S\n\x08\x42ootMode\x12\x19\n\x15\x42OOT_MODE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x42OOT_MODE_INSECURE\x10\x01\x12\x14\n\x10\x42OOT_MODE_SECURE\x10\x02\x32\xa6\x01\n\tBootstrap\x12U\n\x10GetBootstrapData\x12\x1e.bootz.GetBootstrapDataRequest\x1a\x1f.bootz.GetBootstrapDataResponse\"\x00\x12\x42\n\x0cReportStatus\x12\x1a.bootz.ReportStatusRequest\x1a\x14.bootz.EmptyResponse\"\x00\x42)Z\'github.com/openconfig/bootz/proto/bootzb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'github.com.openconfig.bootz.proto.bootz_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/openconfig/bootz/proto/bootz'
  _globals['_CONTROLCARD'].fields_by_name['slot']._loaded_options = None
  _globals['_CONTROLCARD'].fields_by_name['slot']._serialized_options = b'\030\001'
  _globals['_BOOTSTRAPDATARESPONSE'].fields_by_name['certificates']._loaded_options = None
  _globals['_BOOTSTRAPDATARESPONSE'].fields_by_name['certificates']._serialized_options = b'\030\001'
  _globals['_GETBOOTSTRAPDATARESPONSE'].fields_by_name['signed_response']._loaded_options = None
  _globals['_GETBOOTSTRAPDATARESPONSE'].fields_by_name['signed_response']._serialized_options = b'\030\001'
  _globals['_BOOTMODE']._serialized_start=2523
  _globals['_BOOTMODE']._serialized_end=2606
  _globals['_GETBOOTSTRAPDATAREQUEST']._serialized_start=283
  _globals['_GETBOOTSTRAPDATAREQUEST']._serialized_end=431
  _globals['_CHASSISDESCRIPTOR']._serialized_start=434
  _globals['_CHASSISDESCRIPTOR']._serialized_end=562
  _globals['_CONTROLCARD']._serialized_start=564
  _globals['_CONTROLCARD']._serialized_end=656
  _globals['_CONTROLCARDSTATE']._serialized_start=659
  _globals['_CONTROLCARDSTATE']._serialized_end=896
  _globals['_CONTROLCARDSTATE_CONTROLCARDSTATUS']._serialized_start=762
  _globals['_CONTROLCARDSTATE_CONTROLCARDSTATUS']._serialized_end=896
  _globals['_BOOTSTRAPDATARESPONSE']._serialized_start=899
  _globals['_BOOTSTRAPDATARESPONSE']._serialized_end=1316
  _globals['_CERTZPROFILES']._serialized_start=1318
  _globals['_CERTZPROFILES']._serialized_end=1372
  _globals['_CERTZPROFILE']._serialized_start=1374
  _globals['_CERTZPROFILE']._serialized_end=1457
  _globals['_BOOTSTRAPDATASIGNED']._serialized_start=1459
  _globals['_BOOTSTRAPDATASIGNED']._serialized_end=1544
  _globals['_GETBOOTSTRAPDATARESPONSE']._serialized_start=1547
  _globals['_GETBOOTSTRAPDATARESPONSE']._serialized_end=1751
  _globals['_SOFTWAREIMAGE']._serialized_start=1753
  _globals['_SOFTWAREIMAGE']._serialized_end=1859
  _globals['_CREDENTIALS']._serialized_start=1862
  _globals['_CREDENTIALS']._serialized_end=2057
  _globals['_BOOTCONFIG']._serialized_start=2060
  _globals['_BOOTCONFIG']._serialized_end=2209
  _globals['_REPORTSTATUSREQUEST']._serialized_start=2212
  _globals['_REPORTSTATUSREQUEST']._serialized_end=2504
  _globals['_REPORTSTATUSREQUEST_BOOTSTRAPSTATUS']._serialized_start=2361
  _globals['_REPORTSTATUSREQUEST_BOOTSTRAPSTATUS']._serialized_end=2504
  _globals['_EMPTYRESPONSE']._serialized_start=2506
  _globals['_EMPTYRESPONSE']._serialized_end=2521
  _globals['_BOOTSTRAP']._serialized_start=2609
  _globals['_BOOTSTRAP']._serialized_end=2775
# @@protoc_insertion_point(module_scope)
