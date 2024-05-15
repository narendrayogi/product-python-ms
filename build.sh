# Take pull from common module
git submodule update --remote dummy-ms-common

# Building proto files
BUILD_PATH="."

# Deleting the build folder
# rm -rf $BUILD_PATH

# Creating the build folder
# mkdir $BUILD_PATH

# Building the proto files
# python3 -m grpc_tools.protoc --proto_path=./dummy-ms-common/proto ./dummy-ms-common/proto/product.proto --python_out=$BUILD_PATH --grpc_python_out=$BUILD_PATH


python3 -m grpc_tools.protoc -I./dummy-ms-common/proto --python_out=$BUILD_PATH --grpc_python_out=$BUILD_PATH ./dummy-ms-common/proto/product.proto