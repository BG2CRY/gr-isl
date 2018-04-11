/* -*- c++ -*- */

#define ISL_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "isl_swig_doc.i"

%{
#include "isl/pn_generate_i.h"
#include "isl/pmod.h"
#include "isl/oqpsk_coherrent_demod.h"
#include "isl/qpsk_decimator_cc.h"
#include "isl/c1_sys.h"
#include "isl/pn_decimator_FI.h"
#include "isl/PN_correlation.h"
#include "isl/PN_Location.h"
#include "isl/PN_Acquisition.h"
%}


%include "isl/pn_generate_i.h"
GR_SWIG_BLOCK_MAGIC2(isl, pn_generate_i);
%include "isl/pmod.h"
GR_SWIG_BLOCK_MAGIC2(isl, pmod);
%include "isl/oqpsk_coherrent_demod.h"
GR_SWIG_BLOCK_MAGIC2(isl, oqpsk_coherrent_demod);
%include "isl/qpsk_decimator_cc.h"
GR_SWIG_BLOCK_MAGIC2(isl, qpsk_decimator_cc);
%include "isl/c1_sys.h"
GR_SWIG_BLOCK_MAGIC2(isl, c1_sys);
%include "isl/pn_decimator_FI.h"
GR_SWIG_BLOCK_MAGIC2(isl, pn_decimator_FI);
%include "isl/PN_correlation.h"
GR_SWIG_BLOCK_MAGIC2(isl, PN_correlation);
%include "isl/PN_Location.h"
GR_SWIG_BLOCK_MAGIC2(isl, PN_Location);
%include "isl/PN_Acquisition.h"
GR_SWIG_BLOCK_MAGIC2(isl, PN_Acquisition);
