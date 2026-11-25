function(alloy_ecs_example name)
    add_executable(alloy_ecs_example_${name} ${ARGN})
    target_link_libraries(alloy_ecs_example_${name} PRIVATE alloy::ecs alloy_ecs_compile_options)
    set_target_properties(alloy_ecs_example_${name} PROPERTIES CXX_EXTENSIONS OFF CXX_SCAN_FOR_MODULES OFF)
endfunction()

alloy_ecs_example(hello hello.cpp)
