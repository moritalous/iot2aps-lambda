# iot2aps-lambda

# Compile protobufs

(in this directory)

```shell
docker build -t protobuf-build protobuf
docker run -v $(pwd)/iot2aps:/workspace protobuf-build
```

Generate bellow files

```shell
iot2aps/
├── gogoproto
│   └── gogo_pb2.py
├── remote_pb2.py
└── types_pb2.py
```

