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
#include "PN_Location_impl.h"

namespace gr {
  namespace isl {

    PN_Location::sptr
    PN_Location::make()
    {
      return gnuradio::get_initial_sptr
        (new PN_Location_impl());
    }

    /*
     * The private constructor
     */
    PN_Location_impl::PN_Location_impl()
      : gr::block("PN_Location",
              gr::io_signature::make(6, 6, sizeof(int)),
              gr::io_signature::make(1, 1, sizeof(int)))
    {}

    /*
     * Our virtual destructor.
     */
    PN_Location_impl::~PN_Location_impl()
    {
    }

    void
    PN_Location_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }

    int
    PN_Location_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const int *in0 = (const int *) input_items[0];
      const int *in1 = (const int *) input_items[1];
      const int *in2 = (const int *) input_items[2];
      const int *in3 = (const int *) input_items[3];
      const int *in4 = (const int *) input_items[4];
      const int *in5 = (const int *) input_items[5];
      int *out = (int *) output_items[0];
	
      for (int i=0;i<noutput_items;i++)
      {
	for(int j=0;j<1009470;j++)
	{
		if ((j%2 == in0[i]) && (j%7 == in1[i]) && (j%11 == in2[i]) && (j%15 == in3[i]) && (j%19 == in4[i]) && (j%23 == in5[i]))
		{
			out[i] = j;
			break; 
		}
	}
      }

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace isl */
} /* namespace gr */

