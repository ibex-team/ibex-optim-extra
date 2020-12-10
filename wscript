#! /usr/bin/env python
# encoding: utf-8

######################
###### options #######
######################
def options (opt):
	opt.add_option ("--with-optim-extra", action="store_true", dest="WITH_OPTIM_EXTRA",
			help = "Use Affine Arithmetic plugin")
			
	opt.plugins["optim-extra"] = "WITH_OPTIM_EXTRA"
	opt.plugins_dependencies["WITH_OPTIM_EXTRA"]=("affine","ampl")

######################
##### configure ######
######################
def configure (conf):

	# The optim-extra plugin is enabled if --with-optim-extra or --with-optim-extra-extended
	# options are used.
	if conf.options.WITH_OPTIM_EXTRA:
		conf.env.WITH_OPTIM_EXTRA = True

	conf.start_msg ("plugin optim_extra (extended features for ibexopt)")
	if not conf.env.WITH_OPTIM_EXTRA: 
		conf.end_msg ("not used")
		return

	conf.end_msg ("enabled")

	
	conf.env.append_unique ("IBEX_PLUGIN_USE_LIST", "OPTIM_EXTRA")

	# Add information in ibex_Setting
	conf.setting_define ("WITH_OPTIM_EXTRA", 1)

	# add OPTIM_EXTRA plugin include directory
	for f in conf.path.ant_glob ("src/** src", dir = True, src = False):
		conf.env.append_unique("INCLUDES_OPTIM_EXTRA", f.abspath())

	# The build and install steps will be run from the main src/wscript script so
	# we need to give path relative to the main src directory
	mainsrc = conf.srcnode.make_node ("src")

	# add OPTIM_EXTRA headers
	for f in conf.path.ant_glob ("src/**/ibex_*.h"):
		conf.env.append_unique ("IBEX_HDR", f.path_from (mainsrc))

	# add OPTIM_EXTRA source files
	for f in conf.path.ant_glob ("src/**/ibex_*.cpp"):
		conf.env.append_unique ("IBEX_SRC", f.path_from (mainsrc))

	# The utest step will be run from the main tests/wscript script so we need to
	# give path relative to the main tests directory
	maintests = conf.srcnode.make_node ("tests")

	# add OPTIM_EXTRA test files
	for f in conf.path.ant_glob ("tests/**/*.cpp"):
		conf.env.append_unique ('TEST_SRC', f.path_from (maintests))

	# Add optim-extra/tests directory to list of INCLUDES for TESTS
	testsnode = conf.path.make_node ("tests")
	conf.env.append_unique ("INCLUDES_TESTS", testsnode.abspath ())
	
######################
####### build ########
######################
def build (bld):
	if bld.env.WITH_OPTIM_EXTRA:
		# build optimizer04
		bld.program (
			target = "optimizer04",
			use = [ "ibex" ],
			source = bld.path.ant_glob ("src/bin/optimizer04.cpp"),
			install_path = bld.env.BINDIR,
		)
