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
#include "PN_correlation_impl.h"

#include <stdio.h>

namespace gr {
  namespace isl {

    PN_correlation::sptr
    PN_correlation::make()
    {
      return gnuradio::get_initial_sptr
        (new PN_correlation_impl());
    }

    /*
     * The private constructor
     */
    PN_correlation_impl::PN_correlation_impl()
      : gr::block("PN_correlation",
              gr::io_signature::make(1, 1, sizeof(int)),
              gr::io_signature::make(6, 6, sizeof(int)))
    {
fprintf(stdout, "Hello I am BG2CRY\n");

	int c1[2] = {1,-1};
	int c2[7] = {1,1,1,-1,-1,1,-1};
	int c3[11] = {1,1,1,-1,-1,-1,1,-1,1,1,-1};
	int c4[15] = {1,1,1,1,-1,-1,-1,1,-1,-1,1,1,-1,1,-1};
	int c5[19] = {1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1};
	int c6[23] = {1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1};

	int L[6] = { 214, 86261, 91619, 94005, 95475, 96347 };
	int t[6] = {2,7,11,15,19,23};


	for (int i=0;i<L[0];i++)	
	{
		L0[i] = c1[i%t[0]];
	}
	for (int i=0;i<L[1];i++)	
	{
		L1[i] = c2[i%t[1]];
	}
	for (int i=0;i<L[2];i++)	
	{
		L2[i] = c3[i%t[2]];
	}
	for (int i=0;i<L[3];i++)	
	{
		L3[i] = c4[i%t[3]];
	}
	for (int i=0;i<L[4];i++)	
	{
		L4[i] = c5[i%t[4]];
	}
	for (int i=0;i<L[5];i++)	
	{
		L5[i] = c6[i%t[5]];
	}

	for (int i=0;i<96347;i++)	
	{
		buf_rx[i] = 0;
	}

	for (int i=0;i<t[0];i++)	
	{
		buf_cor0[i] = 0;
	}
	for (int i=0;i<t[1];i++)	
	{
		buf_cor1[i] = 0;
	}
	for (int i=0;i<t[2];i++)	
	{
		buf_cor2[i] = 0;
	}
	for (int i=0;i<t[3];i++)	
	{
		buf_cor3[i] = 0;
	}
	for (int i=0;i<t[4];i++)
	{
		buf_cor4[i] = 0;
	}
	for (int i=0;i<t[5];i++)	
	{
		buf_cor5[i] = 0;
	}
     }

    /*
     * Our virtual destructor.
     */
    PN_correlation_impl::~PN_correlation_impl()
    {
    }

    void
    PN_correlation_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }
    void PN_correlation_impl::max(int *data,int len,int *max_value,int *max_index)
    {
	*max_value = data[0];
	*max_index = 0;
	for(int i=1;i<len;i++)
	{
		if(data[i] > *max_value)
		{
			*max_value = data[i];
			*max_index = i;
		}
	}
    }

   /* void PN_correlation_impl::Correlator(int *C_data,int C_len ,int t, int *buf_rx,int *buf_cor)
    {
	int mark=0;	
	for (int j = 0; j<C_len;j++)
	{
		mark = mark + C_data[j]*buf_rx[j];
	}
	for(int j=t-1; j>0; j--) 
	{
		buf_cor[j] = buf_cor[j-1];
	}
	buf_cor[0] = mark;
    }*/



    int
    PN_correlation_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const int *in = (const int *) input_items[0];
      int *out0 = (int *) output_items[0];
      int *out1 = (int *) output_items[1];
      int *out2 = (int *) output_items[2];
      int *out3 = (int *) output_items[3];
      int *out4 = (int *) output_items[4];
      int *out5 = (int *) output_items[5];


      
      int mark=0;
      int max_value,max_index;

      int L[6] = { 214, 86261, 91619, 94005, 95475, 96347 };
      int t[6] = {2,7,11,15,19,23};


     
      for(int i=0; i<noutput_items; i++)
	{
	   
		for(int j=0; j< L[5]-1; j++) 
		{
			buf_rx[j] = buf_rx[j+1];
		}
		buf_rx[L[5]-1] = in[i];

	//corralate with C1	
		mark=0;	
		for (int j = 0; j<L[0];j++)
		{
			mark = mark + L0[j]*buf_rx[j];
		}
		for(int j=t[0]-1; j>0; j--) 
		{
			buf_cor0[j] = buf_cor0[j-1];
		}
		buf_cor0[0] = mark;


		//PN_correlation_impl::Correlator(L0,L[0], t[0], buf_rx, buf_cor0);
		
		PN_correlation_impl::max(buf_cor0,t[0], &max_value, &max_index);
		//out0[i] = max_index;
		out0[i] = buf_cor0[0];

/////////C2
		mark = 0;
		for (int j = 0; j<L[1];j++)
		{
			mark = mark + L1[j]*buf_rx[j];
		}
		for(int j=t[1]-1; j>0; j--) 
		{
			buf_cor1[j] = buf_cor1[j-1];
		}
		buf_cor1[0] = mark;
		
		//PN_correlation_impl::Correlator(L1,L[1], t[1], buf_rx, buf_cor1);
		PN_correlation_impl::max(buf_cor1,t[1], &max_value, &max_index);
		//out1[i] = max_index;
		out1[i] = buf_cor1[0];

/////////
		mark = 0;
		for (int j = 0; j<L[2];j++)
		{
			mark = mark -L2[j]*buf_rx[j];
		}
		for(int j=t[2]-1; j>0; j--) 
		{
			buf_cor2[j] = buf_cor2[j-1];
		}
		buf_cor2[0] = mark;
		//PN_correlation_impl::Correlator(L2,L[2], t[2], buf_rx, buf_cor2);
		PN_correlation_impl::max(buf_cor2,t[2], &max_value, &max_index);
		//out2[i] = max_index;
		out2[i] = buf_cor2[0];

/////////
		mark = 0;
		for (int j = 0; j<L[3];j++)
		{
			mark = mark -L3[j]*buf_rx[j];
		}
		for(int j=t[3]-1; j>0; j--) 
		{
			buf_cor3[j] = buf_cor3[j-1];
		}
		buf_cor3[0] = mark;
		//PN_correlation_impl::Correlator(L3,L[3], t[3], buf_rx, buf_cor3);
		PN_correlation_impl::max(buf_cor3,t[3], &max_value, &max_index);
	//	out3[i] = max_index;
		out3[i] = buf_cor3[0];

/////////
		mark = 0;
		for (int j = 0; j<L[4];j++)
		{
			mark = mark + L4[j]*buf_rx[j];
		}
		for(int j=t[4]-1; j>0; j--) 
		{
			buf_cor4[j] = buf_cor4[j-1];
		}
		buf_cor4[0] = mark;

		//PN_correlation_impl::Correlator(L4,L[4], t[4], buf_rx, buf_cor4);
		PN_correlation_impl::max(buf_cor4,t[4], &max_value, &max_index);
		//out4[i] = max_index;
		out4[i] = buf_cor4[0];

/////////
		mark = 0;
		for (int j = 0; j<L[5];j++)
		{
			mark = mark - L5[j]*buf_rx[j];
		}
		for(int j=t[5]-1; j>0; j--) 
		{
			buf_cor5[j] = buf_cor5[j-1];
		}
		buf_cor5[0] = mark;

		//PN_correlation_impl::Correlator(L5,L[5], t[5], buf_rx, buf_cor5);
		PN_correlation_impl::max(buf_cor5,t[5], &max_value, &max_index);
		//out5[i] = max_index;
		out5[i] = buf_cor5[0];

	    
/////////
		

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

