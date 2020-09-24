#!/usr/bin/env bash
pushd . > /dev/null
cd $( dirname "${BASH_SOURCE[0]}" )
cd ..

python -m grpc_tools.protoc -I=dft/protos --python_out=dft/generated --grpc_python_out=dft/generated dft/protos/dft.proto
python -m grpc_tools.protoc -I=dft/protos/dft.proto -I=dft/protos --python_out=dft/generated --grpc_python_out=dft/generated dft/protos/dftlegacy.proto
python -m grpc_tools.protoc -I=dft/protos --python_out=dft/generated --grpc_python_out=dft/generated dft/protos/dftbase.proto
python -m grpc_tools.protoc -I=dft/protos --python_out=dft/generated --grpc_python_out=dft/generated dft/protos/dftmining.proto

# Patch import problem in generated code
sed -i 's|import dft_pb2 as dft__pb2|import dft.generated.dft_pb2 as dft__pb2|g' dft/generated/dft_pb2_grpc.py
sed -i 's|import dft_pb2 as dft__pb2|import dft.generated.dft_pb2 as dft__pb2|g' dft/generated/dftlegacy_pb2.py
sed -i 's|import dft_pb2 as dft__pb2|import dft.generated.dft_pb2 as dft__pb2|g' dft/generated/dftmining_pb2.py

sed -i 's|import dftlegacy_pb2 as dftlegacy__pb2|import dft.generated.dftlegacy_pb2 as dftlegacy__pb2|g' dft/generated/dftlegacy_pb2_grpc.py
sed -i 's|import dftbase_pb2 as dftbase__pb2|import dft.generated.dftbase_pb2 as dftbase__pb2|g' dft/generated/dftbase_pb2_grpc.py
sed -i 's|import dftmining_pb2 as dftmining__pb2|import dft.generated.dftmining_pb2 as dftmining__pb2|g' dft/generated/dftmining_pb2_grpc.py

find dft/generated -name '*.py'|grep -v migrations|xargs autoflake --in-place

#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/dft/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=markdown,proto.md
#
#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/dft/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=html,index.html

popd > /dev/null
