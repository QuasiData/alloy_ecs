cmake_minimum_required(VERSION 3.28)
# Can be configured separately, without fetching any C++ dependencies.
if(CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_SOURCE_DIR)
    project(alloy_ecs_docs LANGUAGES NONE)
endif()

find_package(Doxygen 1.9.5 REQUIRED)
include(FetchContent)
FetchContent_Declare(doxygen_awesome_css
    GIT_REPOSITORY https://github.com/jothepro/doxygen-awesome-css.git
    GIT_TAG v2.3.4
    SOURCE_SUBDIR __alloy_theme_only__
)
FetchContent_MakeAvailable(doxygen_awesome_css)

set(ALLOY_DOCS_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/..")
set(ALLOY_DOCS_OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/site")
set(ALLOY_DOCS_THEME "${doxygen_awesome_css_SOURCE_DIR}")
configure_file(Doxyfile.in Doxyfile @ONLY)
add_custom_target(alloy_ecs_docs
    COMMAND "${CMAKE_COMMAND}" -E make_directory "${ALLOY_DOCS_OUTPUT}"
    COMMAND Doxygen::doxygen "${CMAKE_CURRENT_BINARY_DIR}/Doxyfile"
    WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    COMMENT "Generating alloy_ecs documentation"
    VERBATIM
)
