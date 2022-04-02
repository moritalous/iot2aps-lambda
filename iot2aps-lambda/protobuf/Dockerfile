FROM ubuntu:20.04

RUN apt update && apt install -y protobuf-compiler git curl

RUN mkdir /work && \
    cd /work && \
    git clone --depth 1 https://github.com/prometheus/prometheus.git && \
    cd prometheus/prompb && \
    curl -L --create-dirs https://raw.githubusercontent.com/gogo/protobuf/master/gogoproto/gogo.proto -o gogoproto/gogo.proto

WORKDIR /work/prometheus/prompb

ENTRYPOINT ["sh", "-c", "protoc --python_out=/workspace ./*.proto gogoproto/*.proto"]
