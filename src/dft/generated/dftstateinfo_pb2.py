# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dftstateinfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import dft.generated.dft_pb2 as dft__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dftstateinfo.proto',
  package='dft',
  syntax='proto3',
  serialized_pb=_b('\n\x12dftstateinfo.proto\x12\x03dft\x1a\tdft.proto\"e\n\x13TransactionMetadata\x12%\n\x0btransaction\x18\x01 \x01(\x0b\x32\x10.dft.Transaction\x12\x14\n\x0c\x62lock_number\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\"A\n\x10LastTransactions\x12-\n\x0btx_metadata\x18\x01 \x03(\x0b\x32\x18.dft.TransactionMetadata\"\x8a\x01\n\tForkState\x12\x1c\n\x14initiator_headerhash\x18\x01 \x01(\x0c\x12\x1d\n\x15\x66ork_point_headerhash\x18\x02 \x01(\x0c\x12\x1f\n\x17old_mainchain_hash_path\x18\x03 \x03(\x0c\x12\x1f\n\x17new_mainchain_hash_path\x18\x04 \x03(\x0c\x62\x06proto3')
  ,
  dependencies=[dft__pb2.DESCRIPTOR,])




_TRANSACTIONMETADATA = _descriptor.Descriptor(
  name='TransactionMetadata',
  full_name='dft.TransactionMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='dft.TransactionMetadata.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_number', full_name='dft.TransactionMetadata.block_number', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='dft.TransactionMetadata.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=139,
)


_LASTTRANSACTIONS = _descriptor.Descriptor(
  name='LastTransactions',
  full_name='dft.LastTransactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_metadata', full_name='dft.LastTransactions.tx_metadata', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=206,
)


_FORKSTATE = _descriptor.Descriptor(
  name='ForkState',
  full_name='dft.ForkState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initiator_headerhash', full_name='dft.ForkState.initiator_headerhash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fork_point_headerhash', full_name='dft.ForkState.fork_point_headerhash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='old_mainchain_hash_path', full_name='dft.ForkState.old_mainchain_hash_path', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_mainchain_hash_path', full_name='dft.ForkState.new_mainchain_hash_path', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=347,
)

_TRANSACTIONMETADATA.fields_by_name['transaction'].message_type = dft__pb2._TRANSACTION
_LASTTRANSACTIONS.fields_by_name['tx_metadata'].message_type = _TRANSACTIONMETADATA
DESCRIPTOR.message_types_by_name['TransactionMetadata'] = _TRANSACTIONMETADATA
DESCRIPTOR.message_types_by_name['LastTransactions'] = _LASTTRANSACTIONS
DESCRIPTOR.message_types_by_name['ForkState'] = _FORKSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionMetadata = _reflection.GeneratedProtocolMessageType('TransactionMetadata', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONMETADATA,
  __module__ = 'dftstateinfo_pb2'
  # @@protoc_insertion_point(class_scope:dft.TransactionMetadata)
  ))
_sym_db.RegisterMessage(TransactionMetadata)

LastTransactions = _reflection.GeneratedProtocolMessageType('LastTransactions', (_message.Message,), dict(
  DESCRIPTOR = _LASTTRANSACTIONS,
  __module__ = 'dftstateinfo_pb2'
  # @@protoc_insertion_point(class_scope:dft.LastTransactions)
  ))
_sym_db.RegisterMessage(LastTransactions)

ForkState = _reflection.GeneratedProtocolMessageType('ForkState', (_message.Message,), dict(
  DESCRIPTOR = _FORKSTATE,
  __module__ = 'dftstateinfo_pb2'
  # @@protoc_insertion_point(class_scope:dft.ForkState)
  ))
_sym_db.RegisterMessage(ForkState)


# @@protoc_insertion_point(module_scope)
