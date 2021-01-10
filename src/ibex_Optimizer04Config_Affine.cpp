//============================================================================
//                                  I B E X                                   
// File        : ibex_Optimizer04Config.cpp
// Author      : Bertrand Neveu, Gilles Chabert
// Copyright   : IMT Atlantique (France)
// License     : See the LICENSE file
// Created     : Dec 11, 2014
// Last Update : Oct 15, 2019
//============================================================================

#include "ibex_Optimizer04Config_Affine.h"
#include "ibex_LinearizerAffine2.h"
#include "ibex_LinearizerCompo.h"
#include "ibex_LinearizerXTaylor.h"
#include "ibex_LinearizerAffine2.h"

#ifdef _IBEX_WITH_AMPL_
#include "ibex_AmplInterface.h"
#endif

namespace ibex {

Optimizer04Config_Affine::Optimizer04Config_Affine(int argc, char** argv) : Optimizer04Config(argc, argv) {

}

void Optimizer04Config_Affine::load_sys(const char* filename) {
#ifdef _IBEX_WITH_AMPL_
	std::size_t found = string(filename).find(".nl");

	if (found!=std::string::npos) {
		AmplInterface interface (filename);
		sys = &rec(new System(interface));
	} else
		sys = &rec(new System(filename));
#else
	std::cerr << "\n\033[31mAMPL files needs ibex-ampl plugin.\n\n";
	exit(0);
#endif
}

Linearizer* Optimizer04Config_Affine::get_linear_relax() {
	Linearizer* lr;

	if (linearrelaxation=="art")
		lr = &rec(new LinearizerAffine2(*ext_sys));
	else if (linearrelaxation=="compo")
		lr = &rec(new LinearizerCompo(
				rec(new LinearizerXTaylor(*ext_sys)),
				rec(new LinearizerAffine2(*ext_sys))));
	else if (linearrelaxation=="xn")
		lr = &rec(new LinearizerXTaylor(*ext_sys));
/*	else {
			stringstream ss;
			ss << "[optimizer04] " << linearrelaxation << " is not an implemented relaxation mode ";
			ibex_error(ss.str().c_str());
		}
*/

	return lr;
}

} // namespace ibex
