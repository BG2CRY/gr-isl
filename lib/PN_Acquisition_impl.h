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

#ifndef INCLUDED_ISL_PN_ACQUISITION_IMPL_H
#define INCLUDED_ISL_PN_ACQUISITION_IMPL_H

#include <isl/PN_Acquisition.h>

namespace gr {
  namespace isl {

    class PN_Acquisition_impl : public PN_Acquisition
    {
     private:
      // Nothing to declare in this block.
	int L0[214],L1[86261],L2[91619],L3[94005],L4[95475],L5[96347];
	int buf_rx[96347],buf_cor0[2],buf_cor1[7],buf_cor2[11],buf_cor3[15],buf_cor4[19],buf_cor5[23];
	int PN_code[1009471];

	void max(int *data,int len,int *max_value,int *max_index);
	void Correlator(int *C_data,int C_len,int *buf_cor, int t, int buf_rx[96347]);
	int lock;

     public:
      PN_Acquisition_impl();
      ~PN_Acquisition_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace isl
} // namespace gr

#endif /* INCLUDED_ISL_PN_ACQUISITION_IMPL_H */

