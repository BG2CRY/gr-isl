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


#ifndef INCLUDED_ISL_PN_CORRELATOR_H
#define INCLUDED_ISL_PN_CORRELATOR_H

#include <isl/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace isl {

    /*!
     * \brief <+description of block+>
     * \ingroup isl
     *
     */
    class ISL_API pn_correlator : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<pn_correlator> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of isl::pn_correlator.
       *
       * To avoid accidental use of raw pointers, isl::pn_correlator's
       * constructor is in a private implementation
       * class. isl::pn_correlator::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace isl
} // namespace gr

#endif /* INCLUDED_ISL_PN_CORRELATOR_H */

