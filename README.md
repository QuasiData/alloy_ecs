# alloy_ecs

Requires C++20, CMake 3.28+, Ninja and Git.

## Build and test

```sh
cmake --preset linux-clang
cmake --build --preset linux-clang-debug
ctest --preset linux-clang-debug
```

Replace `linux-clang` with `linux-gcc`, `windows-clang` or `windows-msvc` as needed. List presets with `cmake --list-presets=all`.

Standalone builds require vendored dependencies or valid Git pins in `cmake/AlloyDependencyPins.cmake`.

## Local development

Clone all four repositories into the same directory:

```sh
mkdir alloy
cd alloy
git clone https://github.com/QuasiData/alloy_core.git
git clone https://github.com/QuasiData/alloy_alloc.git
git clone https://github.com/QuasiData/alloy_datastructures.git
git clone https://github.com/QuasiData/alloy_ecs.git
cd alloy_ecs
cmake --preset dev
cmake --build --preset dev-debug
ctest --preset dev-debug
```

Dev presets use local sibling checkouts. For explicit compiler selection, use e.g. `dev-windows-clang` and `dev-windows-clang-debug` instead.

## Run

```sh
./build/dev/examples/Debug/alloy_ecs_example_hello
cmake --build --preset dev-release
./build/dev/benchmarks/Release/alloy_ecs_benchmarks
```

Adjust `build/dev` to your configure preset; append `.exe` on Windows.

## Documentation

Requires Doxygen 1.9.5+ and Python (activate a virtual environment first).

```sh
python -m pip install -r docs/requirements.txt
python docs/build.py
python docs/build.py --serve --port 8000
```

<http://127.0.0.1:8000/>
