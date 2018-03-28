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
#include "qpsk_decimator_cc_impl.h"

namespace gr {
  namespace isl {

    qpsk_decimator_cc::sptr
    qpsk_decimator_cc::make()
    {
      return gnuradio::get_initial_sptr
        (new qpsk_decimator_cc_impl());
    }

    /*
     * The private constructor
     */
    qpsk_decimator_cc_impl::qpsk_decimator_cc_impl()
      : gr::block("qpsk_decimator_cc",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(2, 2, sizeof(gr_complex)))
    {}

    /*
     * Our virtual destructor.
     */
    qpsk_decimator_cc_impl::~qpsk_decimator_cc_impl()
    {
    }

    void
    qpsk_decimator_cc_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }

    int
    qpsk_decimator_cc_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      gr_complex *out = (gr_complex *) output_items[0];
      gr_complex *out1 = (gr_complex *) output_items[1];
      int i_output = 0;
    
      for(int i=0; i<ninput_items[0]; i++)
      {
		std::vector<tag_t> tags;
		get_tags_in_window(tags, 0, i, i+1);

		for(int j=0; j<tags.size(); j++)
		{
			out1[i_output] = in[i];
			if(tags[j].key == pmt::mp("opt_point"))
			{
				if (in[i].real() < 0)
				{
					out[i_output].real() = -1;
				}
				else
				{
					out[i_output].real() = 1;
				}

				if (in[i].imag() < 0)
				{
					out[i_output].imag() = -1;
				}
				else
				{
					out[i_output].imag() = 1;
				}

				i_output++;
			}
		}
      }

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (ninput_items[0]);

      // Tell runtime system how many output items we produced.
      return i_output;
    }

  } /* namespace isl */
} /* namespace gr */

