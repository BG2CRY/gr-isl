INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_ISL isl)

FIND_PATH(
    ISL_INCLUDE_DIRS
    NAMES isl/api.h
    HINTS $ENV{ISL_DIR}/include
        ${PC_ISL_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    ISL_LIBRARIES
    NAMES gnuradio-isl
    HINTS $ENV{ISL_DIR}/lib
        ${PC_ISL_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ISL DEFAULT_MSG ISL_LIBRARIES ISL_INCLUDE_DIRS)
MARK_AS_ADVANCED(ISL_LIBRARIES ISL_INCLUDE_DIRS)

