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

#ifndef INCLUDED_ISL_OQPSK_COHERRENT_DEMOD_IMPL_H
#define INCLUDED_ISL_OQPSK_COHERRENT_DEMOD_IMPL_H

#include <isl/oqpsk_coherrent_demod.h>

namespace gr {
  namespace isl {

    class oqpsk_coherrent_demod_impl : public oqpsk_coherrent_demod
    {
     private:
		int d_samples_per_symbol;
		std::vector<gr_complex> d_taps;
		int d_opt_point;
		int d_pll;
		float d_pll_loop_bw;
		float d_pll_damping;
		float d_freq_max;
		float d_freq_min;
		int d_dttl;
		float d_dttl_loop_bw;
		float d_dttl_damping;
		float d_max_rate_deviation;

		gr_complex *d_mix_out;
		gr_complex *d_mf_out;
		float d_alpha;
		float d_beta;
		float d_sample_in_symbol;
		float d_freq;
		float d_phase;

		uint8_t d_init;

     public:
      oqpsk_coherrent_demod_impl(int samples_per_symbol, const std::vector<gr_complex> &taps, int opt_point, int pll, float pll_loop_bw, float pll_damping, float freq_max, float freq_min, int dttl, float dttl_loop_bw, float dttl_damping, float max_rate_deviation);
      ~oqpsk_coherrent_demod_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace isl
} // namespace gr

#endif /* INCLUDED_ISL_OQPSK_COHERRENT_DEMOD_IMPL_H */

