cmake_minimum_required (VERSION 3.5.1)

project (IBEX_OPTIM_EXTRA VERSION 1.0 LANGUAGES CXX)

# If IBEX_AFFINE_DIR was given on the command-line and not in the environment,
# set it as an environment variable.
# Enable the usage of 'cmake -DIBEX_AFFINE_DIR=<path> ...'
if (NOT DEFINED ENV{IBEX_AFFINE_DIR} AND DEFINED IBEX_AFFINE_DIR)
  set (ENV{IBEX_AFFINE_DIR} "${IBEX_AFFINE_DIR}")
endif ()
find_package (IBEX_AFFINE 1.0 REQUIRED)
message (STATUS "Found Ibex version ${IBEX_VERSION}")
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
