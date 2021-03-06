# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lastpage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lastpage.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0elastpage.proto\"\x11\n\x0fLastPageRequest\"\x18\n\x08LastPage\x12\x0c\n\x04page\x18\x01 \x01(\x05\"%\n\x10LastPageResponse\x12\x11\n\tlast_page\x18\x01 \x01(\x05\x32\x46\n\x10PS4StoreLastPage\x12\x32\n\x0bGetLastPage\x12\x10.LastPageRequest\x1a\x11.LastPageResponseb\x06proto3'
)




_LASTPAGEREQUEST = _descriptor.Descriptor(
  name='LastPageRequest',
  full_name='LastPageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=35,
)


_LASTPAGE = _descriptor.Descriptor(
  name='LastPage',
  full_name='LastPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='LastPage.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=61,
)


_LASTPAGERESPONSE = _descriptor.Descriptor(
  name='LastPageResponse',
  full_name='LastPageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_page', full_name='LastPageResponse.last_page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['LastPageRequest'] = _LASTPAGEREQUEST
DESCRIPTOR.message_types_by_name['LastPage'] = _LASTPAGE
DESCRIPTOR.message_types_by_name['LastPageResponse'] = _LASTPAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LastPageRequest = _reflection.GeneratedProtocolMessageType('LastPageRequest', (_message.Message,), {
  'DESCRIPTOR' : _LASTPAGEREQUEST,
  '__module__' : 'lastpage_pb2'
  # @@protoc_insertion_point(class_scope:LastPageRequest)
  })
_sym_db.RegisterMessage(LastPageRequest)

LastPage = _reflection.GeneratedProtocolMessageType('LastPage', (_message.Message,), {
  'DESCRIPTOR' : _LASTPAGE,
  '__module__' : 'lastpage_pb2'
  # @@protoc_insertion_point(class_scope:LastPage)
  })
_sym_db.RegisterMessage(LastPage)

LastPageResponse = _reflection.GeneratedProtocolMessageType('LastPageResponse', (_message.Message,), {
  'DESCRIPTOR' : _LASTPAGERESPONSE,
  '__module__' : 'lastpage_pb2'
  # @@protoc_insertion_point(class_scope:LastPageResponse)
  })
_sym_db.RegisterMessage(LastPageResponse)



_PS4STORELASTPAGE = _descriptor.ServiceDescriptor(
  name='PS4StoreLastPage',
  full_name='PS4StoreLastPage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=102,
  serialized_end=172,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLastPage',
    full_name='PS4StoreLastPage.GetLastPage',
    index=0,
    containing_service=None,
    input_type=_LASTPAGEREQUEST,
    output_type=_LASTPAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PS4STORELASTPAGE)

DESCRIPTOR.services_by_name['PS4StoreLastPage'] = _PS4STORELASTPAGE

# @@protoc_insertion_point(module_scope)
