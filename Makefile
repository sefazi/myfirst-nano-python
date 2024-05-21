
clean:
	@rm -vfr ./service/proto

protoc: clean
	@mkdir -p service/proto
	@python3 -m grpc_tools.protoc -I ./proto --python_out=./service/proto --grpc_python_out=./service/proto ./proto/getlist.proto