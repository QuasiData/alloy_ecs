include(FetchContent)

function(alloy_declare_dependency dependency)
    string(TOUPPER "${dependency}" upper)
    set(vendor_dir "${CMAKE_CURRENT_SOURCE_DIR}/vendor/${dependency}")
    set(repository "${${upper}_GIT_REPOSITORY}")
    set(revision "${${upper}_GIT_TAG}")

    if(EXISTS "${vendor_dir}/CMakeLists.txt")
        FetchContent_Declare(${dependency} SOURCE_DIR "${vendor_dir}")
    elseif(NOT repository STREQUAL "" AND NOT revision STREQUAL "")
        FetchContent_Declare(${dependency}
            GIT_REPOSITORY "${repository}"
            GIT_TAG "${revision}"
        )
    else()
        FetchContent_Declare(${dependency}
            DOWNLOAD_COMMAND "${CMAKE_COMMAND}"
                "-DDEPENDENCY=${dependency}"
                -P "${CMAKE_CURRENT_FUNCTION_LIST_DIR}/MissingDependency.cmake"
        )
    endif()
endfunction()
