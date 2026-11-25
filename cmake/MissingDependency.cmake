string(TOUPPER "${DEPENDENCY}" upper)
message(FATAL_ERROR
    "No source configured for ${DEPENDENCY}. Use a dev preset with sibling clones, "
    "set FETCHCONTENT_SOURCE_DIR_${upper}, add vendor/${DEPENDENCY}, or set "
    "${upper}_GIT_REPOSITORY and ${upper}_GIT_TAG in cmake/AlloyDependencyPins.cmake.")
