include(FetchContent)

if(NOT TARGET benchmark::benchmark_main)
    set(BENCHMARK_ENABLE_TESTING OFF CACHE BOOL "Build Google Benchmark tests" FORCE)
    set(BENCHMARK_ENABLE_GTEST_TESTS OFF CACHE BOOL "Build its GoogleTest tests" FORCE)
    set(BENCHMARK_ENABLE_INSTALL OFF CACHE BOOL "Install Google Benchmark" FORCE)
    set(BENCHMARK_ENABLE_WERROR OFF CACHE BOOL "Disable Werror in Google Benchmark" FORCE)
    FetchContent_Declare(benchmark
        GIT_REPOSITORY https://github.com/google/benchmark.git
        GIT_TAG v1.9.5
    )
    FetchContent_MakeAvailable(benchmark)
endif()

add_executable(alloy_ecs_benchmarks bench.cpp)
target_link_libraries(alloy_ecs_benchmarks PRIVATE alloy::ecs alloy_ecs_compile_options benchmark::benchmark_main)
set_target_properties(alloy_ecs_benchmarks PROPERTIES CXX_EXTENSIONS OFF CXX_SCAN_FOR_MODULES OFF)
