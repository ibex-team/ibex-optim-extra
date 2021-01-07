add_executable (optimizer04 bin/optimizer04.cpp
                            ibex_Optimizer04Config_Affine.cpp
                            ibex_Optimizer04Config_Affine.h)
target_include_directories (optimizer04 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries (optimizer04 PUBLIC Ibex::ibex-affine)

# install the binary
install (TARGETS optimizer04 DESTINATION ${CMAKE_INSTALL_BINDIR})
