# gRPC and Protocol Buffers Generation

This project uses Protocol Buffers and gRPC for communication between services. The `Makefile` included in this project helps automate the generation of Protocol Buffers code and gRPC code from `.proto` files.

## Prerequisites

Before using the Makefile, ensure you have the following installed:

- Protocol Buffers Compiler (`protoc`)
- gRPC Python plugin (`grpcio-tools`)
- MySQL Connector for Python (`mysql-connector-python`)

You can install `grpcio-tools` and `mysql-connector-python` using pip:

```bash
pip install grpcio-tools mysql-connector-python
