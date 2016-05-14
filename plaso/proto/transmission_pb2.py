# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plaso/proto/transmission.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='plaso/proto/transmission.proto',
  package='transmission',
  serialized_pb='\n\x1eplaso/proto/transmission.proto\x12\x0ctransmission\"\xcd\x03\n\x08PathSpec\x12&\n\x06parent\x18\x01 \x01(\x0b\x32\x16.transmission.PathSpec\x12\x16\n\x0etype_indicator\x18\x02 \x02(\t\x12\x1a\n\x12\x63ompression_method\x18\x03 \x01(\t\x12\x12\n\nidentifier\x18\x04 \x01(\t\x12\r\n\x05inode\x18\x05 \x01(\x04\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x12\n\npart_index\x18\x07 \x01(\x05\x12\x14\n\x0crange_offset\x18\x08 \x01(\x04\x12\x12\n\nrange_size\x18\t \x01(\x04\x12\x14\n\x0cstart_offset\x18\n \x01(\x04\x12\x13\n\x0bstore_index\x18\x0b \x01(\x05\x12\x12\n\ntable_name\x18\x0c \x01(\t\x12\x13\n\x0b\x63olumn_name\x18\r \x01(\t\x12\x31\n\rrow_condition\x18\x0e \x01(\x0b\x32\x1a.transmission.RowCondition\x12\x11\n\trow_index\x18\x0f \x01(\x05\x12\x13\n\x0b\x64\x61ta_stream\x18\x10 \x01(\t\x12\x15\n\rmft_attribute\x18\x11 \x01(\r\x12\x11\n\tmft_entry\x18\x12 \x01(\x04\x12\x19\n\x11\x65ncryption_method\x18\x13 \x01(\t\"M\n\x0cRowCondition\x12\x14\n\x0cleft_operand\x18\x01 \x02(\t\x12\x10\n\x08operator\x18\x02 \x02(\t\x12\x15\n\rright_operand\x18\x03 \x02(\t')




_PATHSPEC = _descriptor.Descriptor(
  name='PathSpec',
  full_name='transmission.PathSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='transmission.PathSpec.parent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_indicator', full_name='transmission.PathSpec.type_indicator', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compression_method', full_name='transmission.PathSpec.compression_method', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='transmission.PathSpec.identifier', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inode', full_name='transmission.PathSpec.inode', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='transmission.PathSpec.location', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='part_index', full_name='transmission.PathSpec.part_index', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range_offset', full_name='transmission.PathSpec.range_offset', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range_size', full_name='transmission.PathSpec.range_size', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_offset', full_name='transmission.PathSpec.start_offset', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='store_index', full_name='transmission.PathSpec.store_index', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='transmission.PathSpec.table_name', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='column_name', full_name='transmission.PathSpec.column_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row_condition', full_name='transmission.PathSpec.row_condition', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row_index', full_name='transmission.PathSpec.row_index', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_stream', full_name='transmission.PathSpec.data_stream', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mft_attribute', full_name='transmission.PathSpec.mft_attribute', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mft_entry', full_name='transmission.PathSpec.mft_entry', index=17,
      number=18, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encryption_method', full_name='transmission.PathSpec.encryption_method', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=49,
  serialized_end=510,
)


_ROWCONDITION = _descriptor.Descriptor(
  name='RowCondition',
  full_name='transmission.RowCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left_operand', full_name='transmission.RowCondition.left_operand', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator', full_name='transmission.RowCondition.operator', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_operand', full_name='transmission.RowCondition.right_operand', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=u"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=512,
  serialized_end=589,
)

_PATHSPEC.fields_by_name['parent'].message_type = _PATHSPEC
_PATHSPEC.fields_by_name['row_condition'].message_type = _ROWCONDITION
DESCRIPTOR.message_types_by_name['PathSpec'] = _PATHSPEC
DESCRIPTOR.message_types_by_name['RowCondition'] = _ROWCONDITION

class PathSpec(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PATHSPEC

  # @@protoc_insertion_point(class_scope:transmission.PathSpec)

class RowCondition(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROWCONDITION

  # @@protoc_insertion_point(class_scope:transmission.RowCondition)


# @@protoc_insertion_point(module_scope)