/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "pn_generate_i_impl.h"

namespace gr {
  namespace isl {

    pn_generate_i::sptr
    pn_generate_i::make()
    {
      return gnuradio::get_initial_sptr
        (new pn_generate_i_impl());
    }

    /*
     * The private constructor
     */
    pn_generate_i_impl::pn_generate_i_impl()
      : gr::sync_block("pn_generate_i",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(2, 2, sizeof(int)))
    {
	d_i_pn = 0;
    }

    /*
     * Our virtual destructor.
     */
    pn_generate_i_impl::~pn_generate_i_impl()
    {
    }

    int
    pn_generate_i_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
	int *out0 = (int *) output_items[0];
	int *out1 = (int *) output_items[1];

	// Do <+signal processing+>
	short int c1[2] = {1,-1};
	short int c2[7] = {1,1,1,-1,-1,1,-1};
	short int c3[11] = {1,1,1,-1,-1,-1,1,-1,1,1,-1};
	short int c4[15] = {1,1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1};
	short int c5[19] = {1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1};
	short int c6[23] = {1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1};

	short int t[6] = {2,7,11,15,19,23};
	int out;

	for (int i = 0; i < noutput_items; i++)
	{	
		out = 4*c1[d_i_pn%t[0]]+c2[d_i_pn%t[1]]-c3[d_i_pn%t[2]]-c4[d_i_pn%t[3]]+c5[d_i_pn%t[4]]-c6[d_i_pn%t[5]];

		if (out > 0)
		{
			out0[i] = 1;
		}
		if (out < 0)
		{
			out0[i] = -1;
		}

		out1[i] = d_i_pn;

		d_i_pn++;
		if(d_i_pn==1009470) d_i_pn = 0;
	}
      

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace isl */
} /* namespace gr */

