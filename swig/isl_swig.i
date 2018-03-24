/* -*- c++ -*- */

#define ISL_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "isl_swig_doc.i"

%{
#include "isl/pn_generate_i.h"
%}


%include "isl/pn_generate_i.h"
GR_SWIG_BLOCK_MAGIC2(isl, pn_generate_i);
