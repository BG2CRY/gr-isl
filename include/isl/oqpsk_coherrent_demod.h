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


#ifndef INCLUDED_ISL_OQPSK_COHERRENT_DEMOD_H
#define INCLUDED_ISL_OQPSK_COHERRENT_DEMOD_H

#include <isl/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace isl {

    /*!
     * \brief <+description of block+>
     * \ingroup isl
     *
     */
    class ISL_API oqpsk_coherrent_demod : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<oqpsk_coherrent_demod> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of isl::oqpsk_coherrent_demod.
       *
       * To avoid accidental use of raw pointers, isl::oqpsk_coherrent_demod's
       * constructor is in a private implementation
       * class. isl::oqpsk_coherrent_demod::make is the public interface for
       * creating new instances.
       */
      static sptr make(int samples_per_symbol, const std::vector<gr_complex> &taps, int opt_point, int pll, float pll_loop_bw, float pll_damping, float freq_max, float freq_min, int dttl, float dttl_loop_bw, float dttl_damping, float max_rate_deviation);
    };

  } // namespace isl
} // namespace gr

#endif /* INCLUDED_ISL_OQPSK_COHERRENT_DEMOD_H */

