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
#include "qpsk_recover_cc_impl.h"

namespace gr {
  namespace isl {

    qpsk_recover_cc::sptr
    qpsk_recover_cc::make()
    {
      return gnuradio::get_initial_sptr
        (new qpsk_recover_cc_impl());
    }

    /*
     * The private constructor
     */
    qpsk_recover_cc_impl::qpsk_recover_cc_impl()
      : gr::sync_block("qpsk_recover_cc",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex)))
    {}

    /*
     * Our virtual destructor.
     */
    qpsk_recover_cc_impl::~qpsk_recover_cc_impl()
    {
    }

    int
    qpsk_recover_cc_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      gr_complex *out = (gr_complex *) output_items[0];
			int i;
			float out_i=1, out_q=1;
			
      // Do <+signal processing+>
      for(int i=0; i<noutput_items; i++)
      {
				std::vector<tag_t> tags;
				get_tags_in_window(tags, 0, i, i+1);

/*				for(int j=0; j<tags.size(); j++)
				{
			
					if(tags[j].key == pmt::mp("opt_point"))
					{
						if (in[i].real() < 0)
						{
							out_i = -1;
						}
						else
						{
							out_i = 1;
						}

						if (in[i].imag() < 0)
						{
							out_q = -1;
						}
						else
						{
							out_q = 1;
						}
					}
				}

				out[i].real() = out_i;
				out[i].imag() = out_q;
*/

				out[i].real() = 0;
				out[i].imag() = 0;

				for(int j=0; j<tags.size(); j++)
				{
			
					if(tags[j].key == pmt::mp("opt_point"))
					{
						if (in[i].real() < 0)
						{
							out[i].real() = -1;
						}
						else
						{
							out[i].real() = 1;
						}

						if (in[i].imag() < 0)
						{
							out[i].imag() = -1;
						}
						else
						{
							out[i].imag() = 1;
						}
					}
				}
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace isl */
} /* namespace gr */

