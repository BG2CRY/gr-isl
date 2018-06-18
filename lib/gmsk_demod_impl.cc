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
#include "gmsk_demod_impl.h"

#include <math.h>
#include <stdio.h>

#define PI 3.1415926535898

const static float c0[] = 
{
	0.000000000001168, 0.000000000057287, 0.000000001737112, 0.000000035118153, 0.000000489262761, 0.000004841111362,
	0.000034979271684, 0.000189364697486, 0.000786904564822, 0.002568939747048, 0.006745702917174, 0.014617762117921,
	0.026867938235103, 0.043017856489330, 0.061430743390125, 0.079856489426364, 0.096160319102963, 0.108823509741902,
	0.117144453511504, 0.121156619833890, 0.121156619836080, 0.117144453517990, 0.108823509752435, 0.096160319117138,
	0.079856489443636, 0.061430743409831, 0.043017856510713, 0.026867938257340, 0.014617762140158, 0.006745702938557,
	0.002568939766761, 0.000786904582129, 0.000189364711802, 0.000034979282676, 0.000004841119054, 0.000000489267564,
	0.000000035120767, 0.000000001738318, 0.000000000057746, 0.000000000001309, 0.000000000000034
};

namespace gr {
  namespace isl {

    gmsk_demod::sptr
    gmsk_demod::make(float dtll_gain, int pd_N_avg, float pd_k1, float pd_k2, float vco_gain)
    {
      return gnuradio::get_initial_sptr
        (new gmsk_demod_impl(dtll_gain, pd_N_avg, pd_k1, pd_k2, vco_gain));
    }

    /*
     * The private constructor
     */
    gmsk_demod_impl::gmsk_demod_impl(float dtll_gain, int pd_N_avg, float pd_k1, float pd_k2, float vco_gain)
      : gr::block("gmsk_demod",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(2, 2, sizeof(gr_complex))),
              d_dtll_gain(dtll_gain),
              d_pd_N_avg(pd_N_avg),
              d_pd_k1(pd_k1),
              d_pd_k2(pd_k2),
              d_vco_gain(vco_gain)
    {
			int i;

			d_vco_phase = 0;

			for(i=0; i<41; i++)
			{
				d_buf_match_real[i] = 0;
				d_buf_match_imag[i] = 0;
			}

			d_state_match_real.numTaps = 41;
			d_state_match_real.pState = d_buf_match_real;
			d_state_match_real.pCoeffs = (float *)c0;

			d_state_match_imag.numTaps = 41;
			d_state_match_imag.pState = d_buf_match_imag;
			d_state_match_imag.pCoeffs = (float *)c0;

			for(i=0; i<(Tb+2); i++)
			{
				d_buf_delay_real[i] = 0;
				d_buf_delay_imag[i] = 0;
			}

			d_dtll_phase = 0;

			for(i=0; i<50; i++)
			{
				d_buf_avg[i] = 0;
			}

			d_lf_out = 0;

			d_mean_out_last = 0;
    }

    /*
     * Our virtual destructor.
     */
    gmsk_demod_impl::~gmsk_demod_impl()
    {
    }

    void
    gmsk_demod_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }

    void gmsk_demod_impl::fir_filt_f(fir_instance_f *instance, float *pSrc, float *pDst, uint32_t len)
    {
			uint32_t i, j;
			float acc;

			for(i=0; i<len; i++)
			{
				for(j=instance->numTaps-1; j>0; j--)
				{
					instance->pState[j] = instance->pState[j-1];
				}
				instance->pState[0] = pSrc[i];
		
				acc = 0;
				for(j=0; j<instance->numTaps; j++)
				{
					acc = acc + instance->pState[j] * instance->pCoeffs[j];
				}
				pDst[i] = acc;
			}
    }

    int
    gmsk_demod_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];
        gr_complex *out0 = (gr_complex *) output_items[0];
				gr_complex *out1 = (gr_complex *) output_items[1];

				int i, j, nout=0;
				float	vco_real, vco_imag, 
				mix_out_real, mix_out_imag, 
				match_out_real, match_out_imag,
				pd_out, mean_out, lf_out;

			  // Do <+signal processing+>
			  // Tell runtime system how many input items we consumed on
			  // each input stream.
				for(i=0; i<noutput_items; i++)
				{
					vco_real = cos(-d_vco_phase * PI);
					vco_imag = sin(-d_vco_phase * PI);

					mix_out_real = vco_real * in[i].real() - vco_imag * in[i].imag();
					mix_out_imag = vco_real * in[i].imag() + vco_imag * in[i].real();

					fir_filt_f(&d_state_match_real, &mix_out_real, &match_out_real, 1);
					fir_filt_f(&d_state_match_imag, &mix_out_imag, &match_out_imag, 1);

					for(j=0; j<Tb+1; j++)
					{
						d_buf_delay_real[j] = d_buf_delay_real[j+1];
						d_buf_delay_imag[j] = d_buf_delay_imag[j+1];
					}
					d_buf_delay_real[Tb+1] = match_out_real;
					d_buf_delay_imag[Tb+1] = match_out_imag;

					//20180612b
					nout++;
					out0->real() = d_buf_delay_imag[1];
					out0->imag() = d_buf_delay_real[Tb+1];
					out1->real() = mix_out_real;
					out1->imag() = mix_out_imag;
					out0++;
					out1++;

					if( ( (d_buf_delay_real[Tb]<0.0) && (d_buf_delay_real[Tb+1]>0.0) ) || ( (d_buf_delay_real[Tb]>0.0) && (d_buf_delay_real[Tb+1]<0.0) ) )
					{
						if( d_dtll_phase <= 8.0)
						{
							d_dtll_phase = d_dtll_phase - d_dtll_gain;
						}
						else
						{
							d_dtll_phase = d_dtll_phase + d_dtll_gain;
						}
					}

					if( ( (d_buf_delay_imag[0]<0.0) && (d_buf_delay_imag[1]>0.0) ) || ( (d_buf_delay_imag[0]>0.0) && (d_buf_delay_imag[1]<0.0) ) )
					{
						if( d_dtll_phase <= 8.0)
						{
							d_dtll_phase = d_dtll_phase - d_dtll_gain;
						}
						else
						{
							d_dtll_phase = d_dtll_phase + d_dtll_gain;
						}
					}

					d_dtll_phase = d_dtll_phase + 1.0;

					if( d_dtll_phase >= 16.0 )
					{
						d_dtll_phase = d_dtll_phase - 16.0;
					}

					if( d_dtll_phase < 0.0 )
					{
						d_dtll_phase = d_dtll_phase + 16.0;
					}

					// if( count%16 == 10 )
					if( round(d_dtll_phase) == 8.0 )
					{
						add_item_tag(0, nitems_written(0)+i, pmt::mp("opt_point"), pmt::from_double(0.0) );

						pd_out = -tanh(d_buf_delay_real[0]) * d_buf_delay_imag[0] + tanh(d_buf_delay_imag[Tb]) * d_buf_delay_real[Tb];

						mean_out = 0.0;
						for(j=(d_pd_N_avg-1); j>0; j--)
						{
							d_buf_avg[j] = d_buf_avg[j-1];
							mean_out = mean_out + d_buf_avg[j];
						}
						d_buf_avg[0] = pd_out;
						mean_out = mean_out + pd_out;

						mean_out = mean_out/(float)d_pd_N_avg;

						d_lf_out = d_lf_out + (double)(d_pd_k1 + d_pd_k2) * (double)mean_out - (double)d_pd_k1 * (double)d_mean_out_last;
						d_mean_out_last = mean_out;
			
/* //20180612 Delete
						nout++;
						*((float*)out) = d_buf_delay_real[Tb];
						*(((float*)out)+1) = d_buf_delay_imag[0];
						out++;
*/
					}

/*					//20180612a
					nout++;
					out0->real() = d_buf_delay_real[Tb];
					out0->imag() = d_buf_delay_imag[0];
					out0++;
*/
					//count++;

					d_vco_phase = d_vco_phase + d_lf_out * (double)d_vco_gain;

					if(d_vco_phase>=1.0)
					{
						d_vco_phase = d_vco_phase - 2.0;
					}
					if(d_vco_phase<-1.0)
					{
						d_vco_phase = d_vco_phase + 2.0;
					}
				}

				//fprintf(stdout, "%d, %d, %f, %f, %f\n", noutput_items, nout, mean_out, d_lf_out, d_vco_phase);

						  //consume(0, noutput_items);
				consume_each(noutput_items);

        // Tell runtime system how many output items we produced.
        return nout;
    }

  } /* namespace isl */
} /* namespace gr */

