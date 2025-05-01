# Install

## install lm-evaluation-harness on Windows
1. git clone --depth 1 https://github.com/EleutherAI/lm-evaluation-harness
2. cd lm-evaluation-harness
3. pip install -e .

## install llama.cpp on Linux
1. git clone https://github.com/ggml-org/llama.cpp
2. cd llama.cpp
3. cmake -B build 
4. cmake --build build --config Release

## install llama.cpp on Windows
1. git clone https://github.com/ggml-org/llama.cpp
2. cd llama.cpp
3. cmake -B build -DLLAMA_CURL=OFF
4. cmake --build build --config Release

## install llama.cpp on WSL2
1. git clone https://github.com/ggml-org/llama.cpp
2. cd llama.cpp
3. sudo apt update
4. sudo apt install cmake
5. sudo apt install g++
6. sudo apt install libcurl4-openssl-dev
7. cmake -B build
8. cmake --build build --config Release

## install llama.cpp on Windows for llama-quantize
- To run llama-quantize, do the following:
1. cd llama.cpp
2. rmdir /s /q build
3. mkdir build
4. cd build
5. cmake -DCMAKE_BUILD_TYPE=Release .. -DLLAMA_CURL=OFF
6. cmake --build . --config Release
7. dir .\bin



