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
#include "fir_interpolator_ff_impl.h"

namespace gr {
  namespace isl {

    fir_interpolator_ff::sptr
    fir_interpolator_ff::make(int interpolation, const std::vector<float> &taps)
    {
      return gnuradio::get_initial_sptr
        (new fir_interpolator_ff_impl(interpolation, taps));
    }

    /*
     * The private constructor
     */
    fir_interpolator_ff_impl::fir_interpolator_ff_impl(int interpolation, const std::vector<float> &taps)
      : gr::sync_interpolator("fir_interpolator_ff",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)), interpolation), d_interpolation(interpolation), d_taps(taps)
    {
	//set_history(taps.size());
	set_output_multiple(interpolation);
	//[5]={0, 0.5878, 0.9511, 0.9511, 0.5878};
    }

    /*
     * Our virtual destructor.
     */
    fir_interpolator_ff_impl::~fir_interpolator_ff_impl()
    {
    }

    int
    fir_interpolator_ff_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];
      for (int i=0; i<noutput_items/d_interpolation; i++)
      {
	      for (int j=0; j<d_interpolation; j++)
	      {
		out[i*d_interpolation+j] = in[i]*d_taps[j];
	      }
      }
      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace isl */
} /* namespace gr */

