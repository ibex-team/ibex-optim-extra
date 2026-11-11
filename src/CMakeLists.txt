add_executable(optimizer04
    bin/optimizer04.cpp
    ibex_Optimizer04Config.cpp
    ibex_Optimizer04Config_Affine.cpp
)

target_include_directories(optimizer04 PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}
)

target_link_libraries(optimizer04 PRIVATE Ibex::ibex-affine)

# Optional AMPL support
if(IBEX_AMPL_FOUND)
    target_compile_definitions(optimizer04 PRIVATE _IBEX_WITH_AMPL_)
    target_link_libraries(optimizer04 PRIVATE Ibex::ibex-ampl)
endif()

# Install the executable
install(TARGETS optimizer04 DESTINATION ${CMAKE_INSTALL_BINDIR})
