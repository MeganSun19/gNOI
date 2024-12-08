# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: github.com/openconfig/gnoi/file/file.proto
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
    'github.com/openconfig/gnoi/file/file.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.openconfig.gnoi.common import common_pb2 as github_dot_com_dot_openconfig_dot_gnoi_dot_common_dot_common__pb2
from github.com.openconfig.gnoi.types import types_pb2 as github_dot_com_dot_openconfig_dot_gnoi_dot_types_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*github.com/openconfig/gnoi/file/file.proto\x12\tgnoi.file\x1a.github.com/openconfig/gnoi/common/common.proto\x1a,github.com/openconfig/gnoi/types/types.proto\"\xb5\x01\n\nPutRequest\x12-\n\x04open\x18\x01 \x01(\x0b\x32\x1d.gnoi.file.PutRequest.DetailsH\x00\x12\x12\n\x08\x63ontents\x18\x02 \x01(\x0cH\x00\x12$\n\x04hash\x18\x03 \x01(\x0b\x32\x14.gnoi.types.HashTypeH\x00\x1a\x33\n\x07\x44\x65tails\x12\x13\n\x0bremote_file\x18\x01 \x01(\t\x12\x13\n\x0bpermissions\x18\x02 \x01(\rB\t\n\x07request\"\r\n\x0bPutResponse\"!\n\nGetRequest\x12\x13\n\x0bremote_file\x18\x01 \x01(\t\"S\n\x0bGetResponse\x12\x12\n\x08\x63ontents\x18\x01 \x01(\x0cH\x00\x12$\n\x04hash\x18\x02 \x01(\x0b\x32\x14.gnoi.types.HashTypeH\x00\x42\n\n\x08response\"c\n\x17TransferToRemoteRequest\x12\x12\n\nlocal_path\x18\x01 \x01(\t\x12\x34\n\x0fremote_download\x18\x02 \x01(\x0b\x32\x1b.gnoi.common.RemoteDownload\">\n\x18TransferToRemoteResponse\x12\"\n\x04hash\x18\x01 \x01(\x0b\x32\x14.gnoi.types.HashType\"\x1b\n\x0bStatRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"2\n\x0cStatResponse\x12\"\n\x05stats\x18\x01 \x03(\x0b\x32\x13.gnoi.file.StatInfo\"a\n\x08StatInfo\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x15\n\rlast_modified\x18\x02 \x01(\x04\x12\x13\n\x0bpermissions\x18\x03 \x01(\r\x12\x0c\n\x04size\x18\x04 \x01(\x04\x12\r\n\x05umask\x18\x05 \x01(\r\"$\n\rRemoveRequest\x12\x13\n\x0bremote_file\x18\x01 \x01(\t\"\x10\n\x0eRemoveResponse2\xd5\x02\n\x04\x46ile\x12\x38\n\x03Get\x12\x15.gnoi.file.GetRequest\x1a\x16.gnoi.file.GetResponse\"\x00\x30\x01\x12]\n\x10TransferToRemote\x12\".gnoi.file.TransferToRemoteRequest\x1a#.gnoi.file.TransferToRemoteResponse\"\x00\x12\x38\n\x03Put\x12\x15.gnoi.file.PutRequest\x1a\x16.gnoi.file.PutResponse\"\x00(\x01\x12\x39\n\x04Stat\x12\x16.gnoi.file.StatRequest\x1a\x17.gnoi.file.StatResponse\"\x00\x12?\n\x06Remove\x12\x18.gnoi.file.RemoveRequest\x1a\x19.gnoi.file.RemoveResponse\"\x00\x42)Z\x1fgithub.com/openconfig/gnoi/file\xd2>\x05\x30.1.0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'github.com.openconfig.gnoi.file.file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\037github.com/openconfig/gnoi/file\322>\0050.1.0'
  _globals['_PUTREQUEST']._serialized_start=152
  _globals['_PUTREQUEST']._serialized_end=333
  _globals['_PUTREQUEST_DETAILS']._serialized_start=271
  _globals['_PUTREQUEST_DETAILS']._serialized_end=322
  _globals['_PUTRESPONSE']._serialized_start=335
  _globals['_PUTRESPONSE']._serialized_end=348
  _globals['_GETREQUEST']._serialized_start=350
  _globals['_GETREQUEST']._serialized_end=383
  _globals['_GETRESPONSE']._serialized_start=385
  _globals['_GETRESPONSE']._serialized_end=468
  _globals['_TRANSFERTOREMOTEREQUEST']._serialized_start=470
  _globals['_TRANSFERTOREMOTEREQUEST']._serialized_end=569
  _globals['_TRANSFERTOREMOTERESPONSE']._serialized_start=571
  _globals['_TRANSFERTOREMOTERESPONSE']._serialized_end=633
  _globals['_STATREQUEST']._serialized_start=635
  _globals['_STATREQUEST']._serialized_end=662
  _globals['_STATRESPONSE']._serialized_start=664
  _globals['_STATRESPONSE']._serialized_end=714
  _globals['_STATINFO']._serialized_start=716
  _globals['_STATINFO']._serialized_end=813
  _globals['_REMOVEREQUEST']._serialized_start=815
  _globals['_REMOVEREQUEST']._serialized_end=851
  _globals['_REMOVERESPONSE']._serialized_start=853
  _globals['_REMOVERESPONSE']._serialized_end=869
  _globals['_FILE']._serialized_start=872
  _globals['_FILE']._serialized_end=1213
# @@protoc_insertion_point(module_scope)
