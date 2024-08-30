#!/bin/zsh
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

BUILD_DIR="$SCRIPT_DIR/build"

mkdir -p "$BUILD_DIR"

cd "$BUILD_DIR" || { echo "Failed to navigate to build directory"; exit 1; }

cmake .. > /dev/null 2>&1

make > /dev/null

./DSAL