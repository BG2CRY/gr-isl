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


#ifndef INCLUDED_ISL_PN_LOCATION_H
#define INCLUDED_ISL_PN_LOCATION_H

#include <isl/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace isl {

    /*!
     * \brief <+description of block+>
     * \ingroup isl
     *
     */
    class ISL_API PN_Location : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<PN_Location> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of isl::PN_Location.
       *
       * To avoid accidental use of raw pointers, isl::PN_Location's
       * constructor is in a private implementation
       * class. isl::PN_Location::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace isl
} // namespace gr

#endif /* INCLUDED_ISL_PN_LOCATION_H */

