# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Install public header files
########################################################################
install(FILES
    api.h
    pn_generate_i.h
    pmod.h
    oqpsk_coherrent_demod.h
    qpsk_decimator_cc.h
    c1_sys.h
    pn_decimator_FI.h
    PN_correlation.h
    PN_Location.h
    PN_Acquisition.h
    pn_correlator.h
    gmsk_demod.h
    qpsk_recover_cc.h
    fir_interpolator_ff.h
    vector_get_element_ff.h DESTINATION include/isl
)
