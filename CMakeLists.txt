cmake_minimum_required(VERSION 3.28)
project(alloy_ecs VERSION 0.1.0 LANGUAGES CXX)

option(ALLOY_ECS_BUILD_TESTS "Build unit tests" ${PROJECT_IS_TOP_LEVEL})
option(ALLOY_ECS_BUILD_BENCHMARKS "Build microbenchmarks" OFF)
option(ALLOY_ECS_BUILD_EXAMPLES "Build examples" ${PROJECT_IS_TOP_LEVEL})
option(ALLOY_ECS_BUILD_DOCS "Build API documentation target" OFF)

add_library(alloy_ecs_compile_options INTERFACE)

target_compile_features(
    alloy_ecs_compile_options INTERFACE cxx_std_23
)

if(CMAKE_CXX_COMPILER_FRONTEND_VARIANT STREQUAL "MSVC")
    target_compile_options(alloy_ecs_compile_options INTERFACE
        /W4
    )
elseif(CMAKE_CXX_COMPILER_FRONTEND_VARIANT STREQUAL "GNU")
    target_compile_options(alloy_ecs_compile_options INTERFACE
        -Wall
        -Wextra
        -Wpedantic
    )
endif()

include(cmake/AlloyDependencies.cmake)
include(cmake/AlloyDependencyPins.cmake)

alloy_declare_dependency(alloy_core)
alloy_declare_dependency(alloy_alloc)
alloy_declare_dependency(alloy_datastructures)
FetchContent_MakeAvailable(alloy_core alloy_alloc alloy_datastructures)

add_library(alloy_ecs STATIC src/ecs.cpp)
add_library(alloy::ecs ALIAS alloy_ecs)
target_compile_features(alloy_ecs PUBLIC cxx_std_23)
set_target_properties(alloy_ecs PROPERTIES CXX_EXTENSIONS OFF CXX_SCAN_FOR_MODULES OFF)
target_include_directories(alloy_ecs PUBLIC
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
)
target_link_libraries(alloy_ecs PUBLIC alloy::core alloy::alloc alloy::datastructures PRIVATE alloy_ecs_compile_options)

if(ALLOY_ECS_BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()
if(ALLOY_ECS_BUILD_BENCHMARKS)
    add_subdirectory(benchmarks)
endif()
if(ALLOY_ECS_BUILD_EXAMPLES)
    add_subdirectory(examples)
endif()
if(ALLOY_ECS_BUILD_DOCS)
    add_subdirectory(docs)
endif()

if(PROJECT_IS_TOP_LEVEL AND CMAKE_EXPORT_COMPILE_COMMANDS)
    add_custom_target(copy_compile_commands ALL
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
            "${CMAKE_BINARY_DIR}/compile_commands.json"
            "${PROJECT_SOURCE_DIR}/compile_commands.json"
        COMMENT "Updating compilation database"
        VERBATIM
    )
endif()