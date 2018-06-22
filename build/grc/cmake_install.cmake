# Install script for directory: /home/lilac/gr-isl/grc

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/lilac/gr-isl/grc/isl_pn_generate_i.xml"
    "/home/lilac/gr-isl/grc/isl_pmod.xml"
    "/home/lilac/gr-isl/grc/isl_oqpsk_coherrent_demod.xml"
    "/home/lilac/gr-isl/grc/isl_qpsk_decimator_cc.xml"
    "/home/lilac/gr-isl/grc/isl_c1_sys.xml"
    "/home/lilac/gr-isl/grc/isl_pn_decimator_FI.xml"
    "/home/lilac/gr-isl/grc/isl_PN_correlation.xml"
    "/home/lilac/gr-isl/grc/isl_PN_Location.xml"
    "/home/lilac/gr-isl/grc/isl_PN_Acquisition.xml"
    "/home/lilac/gr-isl/grc/isl_pn_correlator.xml"
    "/home/lilac/gr-isl/grc/isl_gmsk_demod.xml"
    "/home/lilac/gr-isl/grc/isl_qpsk_recover_cc.xml"
    "/home/lilac/gr-isl/grc/isl_fir_interpolator_ff.xml"
    "/home/lilac/gr-isl/grc/isl_vector_get_element_ff.xml"
    )
endif()

