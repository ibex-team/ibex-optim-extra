cmake_minimum_required (VERSION 3.5.1)

project (IBEX_OPTIM_EXTRA VERSION 1.0 LANGUAGES CXX)

message (STATUS "Found Ibex version ${IBEX_VERSION}")

find_package (IBEX_AFFINE 1.0 REQUIRED)

find_package (IBEX_AFFINE 1.0 CONFIG REQUIRED)

find_package(IBEX_AMPL CONFIG QUIET)

if(IBEX_AMPL_FOUND)
    message(STATUS "IBEX_AMPL found: enabling AMPL support")
else()
    message(STATUS "IBEX_AMPL not found: AMPL support disabled")
endif()

ibex_init_common () # Ibex should have installed this function

# Interval and linear programming names and versions are available
message (STATUS "Ibex was compiled with interval library "
                "${IBEX_INTERVAL_LIB_NAME} ${IBEX_INTERVAL_LIB_VERSION}")

if (IBEX_LP_LIB_NAME) # Was Ibex compiled with a linear programming library ?
  message (STATUS "Ibex was compiled with Linear Programming library "
                  "${IBEX_LP_LIB_NAME} ${IBEX_LP_LIB_VERSION}")
else ()
  message (STATUS "Ibex was compiled without any Linear Programming library")
endif ()

################################################################################
# Compile sources
################################################################################
add_subdirectory (src)
