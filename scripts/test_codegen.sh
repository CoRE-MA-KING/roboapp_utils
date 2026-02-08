#!/bin/bash
set -e

# Create a temporary directory for output
OUT_DIR=$(mktemp -d)

# Ensure cleanup on exit
cleanup() {
    rm -rf "$OUT_DIR"
}
trap cleanup EXIT

echo "Starting Protobuf code generation test..."

# Find all .proto files
PROTO_FILES=$(find proto -name "*.proto")

if [ -z "$PROTO_FILES" ]; then
    echo "Error: No .proto files found."
    exit 1
fi

echo "Found proto files:"
echo "$PROTO_FILES"

# Generate Python code using protoc
# This validates syntax and inter-dependencies
protoc --python_out="$OUT_DIR" --proto_path=proto $PROTO_FILES

echo "----------------------------------------"
echo "SUCCESS: Protobuf code generation passed."
echo "----------------------------------------"