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
#include "c1_sys_impl.h"

namespace gr {
  namespace isl {

    c1_sys::sptr
    c1_sys::make()
    {
      return gnuradio::get_initial_sptr
        (new c1_sys_impl());
    }

    /*
     * The private constructor
     */
    c1_sys_impl::c1_sys_impl()
      : gr::block("c1_sys",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(2, 2, sizeof(float)))
    {
	float sin_shape[5] = {0, 0.5878, 0.9511, 0.9511, 0.5878};
	short int c1[2] = {1,-1};

	for (int i=0;i<1070;i++)	
	{
		for (int j = 0; j<5 ; j++)
		{
			filter_coeff[i] = c1[(i/5)%2]*sin_shape[j];
		}
	}
	

     }

    /*
     * Our virtual destructor.
     */
    c1_sys_impl::~c1_sys_impl()
    {
    }

    void
    c1_sys_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }

    int
    c1_sys_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];
      float *out1 = (float *) output_items[1];
      float i_output[3] = {0,0,0};
      float buf_output;
      int k1;
      float k2 = 0;
      float dd = 0.01;

      for(int i=0; i<ninput_items[0]; i++)
      {
		out1[i] = buf[0];		
		for(int j=0; j<1069; j++) 
		{
			buf[j] = buf[j+1];
		}
		buf[1069] = in[i];
		
		out[i] = 0;
		for(int j=0; j<1070; j++) 
		{
			out[i] = out[i] + buf[j] * filter_coeff[j];
		}

		i_output[0] = i_output[1];
		i_output[1] = i_output[2];
		i_output[2] = out[i];
		
		if (i_output[1] > 200)
		{
			if (i_output[1]>i_output[0] && i_output[1] > i_output[2])
			{
				
				k1 = (i-1)%5;	
				//out[i] = buf[2]
 			}
     		}

		if (k1 - k2 > 0.1)
		{
			k2 = k2+dd*(k1-k2);
			//k2 = k2 + dd;
		} 
		else if (k1 - k2 < -0.1)
		{
			k2 = k2-dd*(k2-k1);
			//k2 = k2 - dd;
		}
		
		if ((i-1)%5 == round(k2))
		{
			add_item_tag(1, nitems_written(1)+i, pmt::mp("pn"), pmt::from_double(0.0) );
			add_item_tag(0, nitems_written(0)+i-1, pmt::mp("cor"), pmt::from_double(0.0) );	
		}
      }
      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (ninput_items[0]);

      // Tell runtime system how many output items we produced.
      return ninput_items[0];
    }

  } /* namespace isl */
} /* namespace gr */

