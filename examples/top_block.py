#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Jun 15 23:03:27 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from fft_correlator_hier import fft_correlator_hier  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import dslwp
import isl
import math
import sip
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.ebn0_threshold = ebn0_threshold = 10
        self.ebn0 = ebn0 = 100
        self.sps_pn = sps_pn = 5
        self.snr_threshold = snr_threshold = 10.0**(ebn0_threshold/10.0)/sps
        self.snr = snr = 10.0**(ebn0/10.0)/sps
        self.samp_rate = samp_rate = 40000
        self.pll_loop_bw = pll_loop_bw = 50
        self.mrg = mrg = 0.3*3.14

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_2_0 = qtgui.time_sink_c(
        	800, #size
        	1000, #samp_rate
        	"pn_out", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_2_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2_0.enable_autoscale(True)
        self.qtgui_time_sink_x_2_0.enable_grid(False)
        self.qtgui_time_sink_x_2_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_2_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_2_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_2_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_0_win)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"origin", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"remod", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
        	160, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_win)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	160, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-4, 4)
        self.qtgui_const_sink_x_0.set_x_axis(-4, 4)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.3, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.isl_qpsk_recover_cc_0 = isl.qpsk_recover_cc()
        self.isl_qpsk_decimator_cc_0 = isl.qpsk_decimator_cc()
        self.isl_pn_generate_i_0 = isl.pn_generate_i()
        self.isl_pmod_0 = isl.pmod()
        self.isl_oqpsk_coherrent_demod_0 = isl.oqpsk_coherrent_demod(16, ([0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000005, 0.000035, 0.000189, 0.000787, 0.002569, 0.006746, 0.014618, 0.026868, 0.043018, 0.061431, 0.079856, 0.096160, 0.108824, 0.117144, 0.121157, 0.121157, 0.117144, 0.108824, 0.096160, 0.079856, 0.061431, 0.043018, 0.026868, 0.014618, 0.006746, 0.002569, 0.000787, 0.000189, 0.000035, 0.000005, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]), 4, 1, 2.0*math.pi*pll_loop_bw/samp_rate, 0.707, 3.14, -3.14, 1, 0.05, 0.707, 1.5)
        self.interp_fir_filter_xxx_1 = filter.interp_fir_filter_ccc(1, ([0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000005, 0.000035, 0.000189, 0.000787, 0.002569, 0.006746, 0.014618, 0.026868, 0.043018, 0.061431, 0.079856, 0.096160, 0.108824, 0.117144, 0.121157, 0.121157, 0.117144, 0.108824, 0.096160, 0.079856, 0.061431, 0.043018, 0.026868, 0.014618, 0.006746, 0.002569, 0.000787, 0.000189, 0.000035, 0.000005, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]))
        self.interp_fir_filter_xxx_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(1, (0, 0.5878, 0.9511, 0.9511, 0.5878))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(sps_pn, (0, 0.5878, 0.9511, 0.9511, 0.5878))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fft_correlator_hier_0 = fft_correlator_hier(
            fft_size=512,
            nthreads=1,
            tap_len=512,
            taps=[0.986752+0.162236j, 0.961165+0.275976j, 0.909253+0.416245j, 0.823810+0.566866j, 0.704089+0.710112j, 0.554654+0.832081j, 0.382467+0.923969j, 0.195052+0.980793j, 0.000006+1.000000j, -0.195011+0.980801j, -0.382250+0.924059j, -0.553737+0.832692j, -0.701059+0.713104j, -0.815998+0.578055j, -0.893407+0.449249j, -0.934886+0.354949j, -0.947363+0.320163j, -0.934914+0.354874j, -0.893617+0.448830j, -0.817269+0.576256j, -0.707107+0.707107j, -0.576256+0.817269j, -0.448830+0.893617j, -0.354872+0.934915j, -0.320152+0.947366j, -0.354872+0.934915j, -0.448830+0.893617j, -0.576256+0.817269j, -0.707107+0.707107j, -0.817269+0.576256j, -0.893617+0.448830j, -0.934915+0.354872j, -0.947366+0.320152j, -0.934915+0.354872j, -0.893617+0.448830j, -0.817269+0.576256j, -0.707107+0.707107j, -0.576256+0.817269j, -0.448830+0.893617j, -0.354874+0.934914j, -0.320163+0.947363j, -0.354949+0.934886j, -0.449249+0.893407j, -0.578055+0.815998j, -0.713104+0.701059j, -0.832692+0.553737j, -0.924059+0.382250j, -0.980801+0.195010j, -1.000000-0.000012j, -0.980785-0.195092j, -0.923879-0.382684j, -0.831470-0.555570j, -0.707107-0.707107j, -0.555570-0.831470j, -0.382683-0.923880j, -0.195090-0.980785j, -0.000000-1.000000j, 0.195090-0.980785j, 0.382683-0.923880j, 0.555570-0.831470j, 0.707107-0.707107j, 0.831470-0.555570j, 0.923879-0.382684j, 0.980785-0.195092j, 1.000000-0.000012j, 0.980801+0.195010j, 0.924059+0.382250j, 0.832692+0.553737j, 0.713104+0.701059j, 0.578055+0.815998j, 0.449249+0.893407j, 0.354949+0.934886j, 0.320163+0.947363j, 0.354874+0.934914j, 0.448830+0.893617j, 0.576256+0.817269j, 0.707107+0.707107j, 0.817269+0.576256j, 0.893617+0.448830j, 0.934914+0.354874j, 0.947363+0.320163j, 0.934886+0.354949j, 0.893407+0.449249j, 0.815998+0.578055j, 0.701059+0.713104j, 0.553737+0.832692j, 0.382250+0.924059j, 0.195012+0.980801j, 0.000000+1.000000j, -0.195012+0.980801j, -0.382250+0.924059j, -0.553737+0.832692j, -0.701059+0.713104j, -0.815998+0.578055j, -0.893407+0.449249j, -0.934885+0.354950j, -0.947359+0.320174j, -0.934885+0.354950j, -0.893407+0.449249j, -0.815998+0.578055j, -0.701059+0.713104j, -0.553737+0.832692j, -0.382250+0.924059j, -0.195010+0.980801j, 0.000012+1.000000j, 0.195092+0.980785j, 0.382684+0.923879j, 0.555570+0.831470j, 0.707107+0.707107j, 0.831470+0.555570j, 0.923879+0.382684j, 0.980785+0.195092j, 1.000000+0.000012j, 0.980801-0.195010j, 0.924059-0.382250j, 0.832692-0.553737j, 0.713104-0.701059j, 0.578055-0.815998j, 0.449249-0.893407j, 0.354950-0.934885j, 0.320174-0.947359j, 0.354950-0.934885j, 0.449249-0.893407j, 0.578055-0.815998j, 0.713104-0.701059j, 0.832692-0.553737j, 0.924059-0.382250j, 0.980801-0.195012j, 1.000000-0.000000j, 0.980801+0.195012j, 0.924059+0.382250j, 0.832692+0.553737j, 0.713104+0.701059j, 0.578055+0.815998j, 0.449249+0.893407j, 0.354950+0.934885j, 0.320174+0.947359j, 0.354950+0.934885j, 0.449249+0.893407j, 0.578055+0.815998j, 0.713104+0.701059j, 0.832692+0.553737j, 0.924059+0.382250j, 0.980801+0.195012j, 1.000000-0.000000j, 0.980801-0.195012j, 0.924059-0.382250j, 0.832692-0.553737j, 0.713104-0.701059j, 0.578055-0.815998j, 0.449249-0.893407j, 0.354950-0.934885j, 0.320174-0.947359j, 0.354950-0.934885j, 0.449249-0.893407j, 0.578055-0.815998j, 0.713104-0.701059j, 0.832692-0.553737j, 0.924059-0.382250j, 0.980801-0.195012j, 1.000000-0.000000j, 0.980801+0.195012j, 0.924059+0.382250j, 0.832692+0.553737j, 0.713104+0.701059j, 0.578055+0.815998j, 0.449249+0.893407j, 0.354950+0.934885j, 0.320174+0.947359j, 0.354950+0.934885j, 0.449249+0.893407j, 0.578055+0.815998j, 0.713104+0.701059j, 0.832692+0.553737j, 0.924059+0.382250j, 0.980801+0.195010j, 1.000000-0.000012j, 0.980785-0.195092j, 0.923879-0.382684j, 0.831470-0.555570j, 0.707107-0.707107j, 0.555570-0.831470j, 0.382684-0.923879j, 0.195092-0.980785j, 0.000012-1.000000j, -0.195010-0.980801j, -0.382250-0.924059j, -0.553737-0.832692j, -0.701059-0.713104j, -0.815998-0.578055j, -0.893407-0.449249j, -0.934885-0.354950j, -0.947359-0.320174j, -0.934885-0.354950j, -0.893407-0.449249j, -0.815998-0.578055j, -0.701059-0.713104j, -0.553737-0.832692j, -0.382250-0.924059j, -0.195010-0.980801j, 0.000012-1.000000j, 0.195092-0.980785j, 0.382684-0.923879j, 0.555570-0.831470j, 0.707107-0.707107j, 0.831470-0.555570j, 0.923880-0.382683j, 0.980785-0.195090j, 1.000000-0.000000j, 0.980785+0.195090j, 0.923880+0.382683j, 0.831470+0.555570j, 0.707107+0.707107j, 0.555570+0.831470j, 0.382684+0.923879j, 0.195092+0.980785j, 0.000012+1.000000j, -0.195010+0.980801j, -0.382250+0.924059j, -0.553737+0.832692j, -0.701059+0.713104j, -0.815998+0.578055j, -0.893407+0.449249j, -0.934885+0.354950j, -0.947359+0.320174j, -0.934885+0.354950j, -0.893407+0.449249j, -0.815998+0.578055j, -0.701059+0.713104j, -0.553737+0.832692j, -0.382250+0.924059j, -0.195010+0.980801j, 0.000012+1.000000j, 0.195092+0.980785j, 0.382684+0.923879j, 0.555570+0.831470j, 0.707107+0.707107j, 0.831470+0.555570j, 0.923879+0.382684j, 0.980785+0.195092j, 1.000000+0.000012j, 0.980801-0.195010j, 0.924059-0.382250j, 0.832692-0.553737j, 0.713104-0.701059j, 0.578055-0.815998j, 0.449249-0.893407j, 0.354950-0.934885j, 0.320174-0.947359j, 0.354950-0.934885j, 0.449249-0.893407j, 0.578055-0.815998j, 0.713104-0.701059j, 0.832692-0.553737j, 0.924059-0.382250j, 0.980801-0.195010j, 1.000000+0.000012j, 0.980785+0.195092j, 0.923879+0.382684j, 0.831470+0.555570j, 0.707107+0.707107j, 0.555570+0.831470j, 0.382683+0.923880j, 0.195090+0.980785j, 0.000000+1.000000j, -0.195090+0.980785j, -0.382683+0.923880j, -0.555570+0.831470j, -0.707107+0.707107j, -0.831470+0.555570j, -0.923879+0.382684j, -0.980785+0.195092j, -1.000000+0.000012j, -0.980801-0.195010j, -0.924059-0.382250j, -0.832692-0.553737j, -0.713104-0.701059j, -0.578055-0.815998j, -0.449249-0.893407j, -0.354950-0.934885j, -0.320174-0.947359j, -0.354950-0.934885j, -0.449249-0.893407j, -0.578055-0.815998j, -0.713104-0.701059j, -0.832692-0.553737j, -0.924059-0.382250j, -0.980801-0.195010j, -1.000000+0.000012j, -0.980785+0.195092j, -0.923879+0.382684j, -0.831470+0.555570j, -0.707107+0.707107j, -0.555570+0.831470j, -0.382683+0.923880j, -0.195090+0.980785j, 0.000000+1.000000j, 0.195090+0.980785j, 0.382683+0.923880j, 0.555570+0.831470j, 0.707107+0.707107j, 0.831470+0.555570j, 0.923879+0.382684j, 0.980785+0.195092j, 1.000000+0.000012j, 0.980801-0.195010j, 0.924059-0.382250j, 0.832692-0.553737j, 0.713104-0.701059j, 0.578055-0.815998j, 0.449249-0.893407j, 0.354950-0.934885j, 0.320174-0.947359j, 0.354950-0.934885j, 0.449249-0.893407j, 0.578055-0.815998j, 0.713104-0.701059j, 0.832692-0.553737j, 0.924059-0.382250j, 0.980801-0.195010j, 1.000000+0.000012j, 0.980785+0.195092j, 0.923879+0.382684j, 0.831470+0.555570j, 0.707107+0.707107j, 0.555570+0.831470j, 0.382683+0.923880j, 0.195090+0.980785j, 0.000000+1.000000j, -0.195090+0.980785j, -0.382683+0.923880j, -0.555570+0.831470j, -0.707107+0.707107j, -0.831470+0.555570j, -0.923879+0.382684j, -0.980785+0.195092j, -1.000000+0.000012j, -0.980801-0.195010j, -0.924059-0.382250j, -0.832692-0.553737j, -0.713104-0.701059j, -0.578055-0.815998j, -0.449249-0.893407j, -0.354949-0.934886j, -0.320163-0.947363j, -0.354874-0.934914j, -0.448830-0.893617j, -0.576256-0.817269j, -0.707107-0.707107j, -0.817269-0.576256j, -0.893617-0.448830j, -0.934915-0.354872j, -0.947366-0.320152j, -0.934915-0.354872j, -0.893617-0.448830j, -0.817269-0.576256j, -0.707107-0.707107j, -0.576256-0.817269j, -0.448830-0.893617j, -0.354874-0.934914j, -0.320163-0.947363j, -0.354949-0.934886j, -0.449249-0.893407j, -0.578055-0.815998j, -0.713104-0.701059j, -0.832692-0.553737j, -0.924059-0.382250j, -0.980801-0.195012j, -1.000000+0.000000j, -0.980801+0.195012j, -0.924059+0.382250j, -0.832692+0.553737j, -0.713104+0.701059j, -0.578055+0.815998j, -0.449249+0.893407j, -0.354950+0.934885j, -0.320174+0.947359j, -0.354950+0.934885j, -0.449249+0.893407j, -0.578055+0.815998j, -0.713104+0.701059j, -0.832692+0.553737j, -0.924059+0.382250j, -0.980801+0.195012j, -1.000000+0.000000j, -0.980801-0.195012j, -0.924059-0.382250j, -0.832692-0.553737j, -0.713104-0.701059j, -0.578055-0.815998j, -0.449249-0.893407j, -0.354950-0.934885j, -0.320174-0.947359j, -0.354950-0.934885j, -0.449249-0.893407j, -0.578055-0.815998j, -0.713104-0.701059j, -0.832692-0.553737j, -0.924059-0.382250j, -0.980801-0.195010j, -1.000000+0.000012j, -0.980785+0.195092j, -0.923879+0.382684j, -0.831470+0.555570j, -0.707107+0.707107j, -0.555570+0.831470j, -0.382684+0.923879j, -0.195092+0.980785j, -0.000012+1.000000j, 0.195010+0.980801j, 0.382250+0.924059j, 0.553737+0.832692j, 0.701059+0.713104j, 0.815998+0.578055j, 0.893407+0.449249j, 0.934886+0.354949j, 0.947363+0.320163j, 0.934914+0.354874j, 0.893617+0.448830j, 0.817269+0.576256j, 0.707107+0.707107j, 0.576256+0.817269j, 0.448830+0.893617j, 0.354872+0.934915j, 0.320152+0.947366j, 0.354872+0.934915j, 0.448830+0.893617j, 0.576256+0.817269j, 0.707107+0.707107j, 0.817269+0.576256j, 0.893617+0.448830j, 0.934915+0.354872j, 0.947366+0.320152j, 0.934915+0.354872j, 0.893617+0.448830j, 0.817269+0.576256j, 0.707107+0.707107j, 0.576256+0.817269j, 0.448830+0.893617j, 0.354874+0.934914j, 0.320163+0.947363j, 0.354949+0.934886j, 0.449249+0.893407j, 0.578055+0.815998j, 0.713104+0.701059j, 0.832692+0.553737j, 0.924059+0.382250j, 0.980801+0.195010j, 1.000000-0.000012j, 0.980785-0.195092j, 0.923879-0.382684j, 0.831470-0.555570j, 0.707107-0.707107j, 0.555570-0.831470j, 0.382684-0.923879j, 0.195092-0.980785j, 0.000012-1.000000j, -0.195010-0.980801j, -0.382250-0.924059j, -0.553737-0.832692j, -0.701059-0.713104j, -0.815998-0.578055j, -0.893407-0.449249j, -0.934885-0.354950j, -0.947359-0.320174j, -0.934885-0.354950j, -0.893407-0.449249j, -0.815998-0.578055j, -0.701059-0.713104j, -0.553737-0.832692j, -0.382250-0.924059j, -0.195010-0.980801j, 0.000012-1.000000j, 0.195092-0.980785j, 0.382684-0.923879j, 0.555570-0.831470j, 0.707107-0.707107j, 0.831470-0.555570j, 0.923880-0.382683j, 0.980785-0.195090j, 1.000000-0.000000j, 0.980785+0.195090j, 0.923880+0.382683j, 0.831470+0.555570j, 0.707107+0.707107j, 0.555570+0.831470j, 0.382684+0.923879j, 0.195092+0.980785j, 0.000012+1.000000j, -0.195010+0.980801j, -0.382250+0.924059j, -0.553737+0.832692j, -0.701059+0.713104j, -0.815998+0.578055j, -0.893407+0.449249j, -0.934886+0.354949j, -0.947363+0.320163j, -0.934914+0.354874j, -0.893617+0.448830j, -0.817269+0.576256j, -0.707107+0.707107j, -0.576256+0.817269j, -0.448830+0.893617j, -0.354873+0.934914j, -0.320157+0.947364j, -0.354911+0.934900j, -0.449039+0.893512j, -0.577156+0.816634j, -0.710112+0.704089j, -0.825057+0.565049j, -0.909448+0.415819j, -0.961187+0.275898j],
            threshold=snr_threshold,
        )
        self.top_layout.addWidget(self.fft_correlator_hier_0)
        self.dslwp_set_gain_by_tag_cc_0 = dslwp.set_gain_by_tag_cc(1024, 1)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=8,
        	bt=0.5,
        	verbose=False,
        	log=False,
        )
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(5, 0.25*0.175*0.175*0.25, 0.5, 0.175*0.5, 0.0005)
        self.digital_binary_slicer_fb_1 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_vector_source_x_1_0 = blocks.vector_source_f([1,-1], True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_b((0x03, 0x47, 0x76, 0xC7, 0x27, 0x28, 0x95, 0xB0,0xFF, 0x48, 0x0E, 0xC0, 0x9A, 0x0D, 0x70, 0xBC,0x8E, 0x2C, 0x93, 0xAD, 0xA7, 0xB7, 0x46, 0xCE,0x5A, 0x97, 0x7D, 0xCC, 0x32, 0xA2, 0xBF, 0x3E,0x0A, 0x10, 0xF1, 0x88, 0x94, 0xCD, 0xEA, 0xB1,0xFE, 0x90, 0x1D, 0x81, 0x34, 0x1A, 0xE1, 0x79,0x1C, 0x59, 0x27, 0x5B, 0x4F, 0x6E, 0x8D, 0x9C,0xB5, 0x2E, 0xFB, 0x98, 0x65, 0x45, 0x7E, 0x7C,0x14, 0x21, 0xE3, 0x11, 0x29, 0x9B, 0xD5, 0x63,0xFD, 0x20, 0x3B, 0x02, 0x68, 0x35, 0xC2, 0xF2,0x38, 0xB2, 0x4E, 0xB6, 0x9E, 0xDD, 0x1B, 0x39,0x6A, 0x5D, 0xF7, 0x30, 0xCA, 0x8A, 0xFC, 0xF8,0x28, 0x43, 0xC6, 0x22, 0x53, 0x37, 0xAA, 0xC7,0xFA, 0x40, 0x76, 0x04, 0xD0, 0x6B, 0x85, 0xE4,0x71, 0x64, 0x9D, 0x6D, 0x3D, 0xBA, 0x36, 0x72,0xD4, 0xBB, 0xEE, 0x61, 0x95, 0x15, 0xF9, 0xF0,0x50, 0x87, 0x8C, 0x44, 0xA6, 0x6F, 0x55, 0x8F,0xF4, 0x80, 0xEC, 0x09, 0xA0, 0xD7, 0x0B, 0xC8,0xE2, 0xC9, 0x3A, 0xDA, 0x7B, 0x74, 0x6C, 0xE5,0xA9, 0x77, 0xDC, 0xC3, 0x2A, 0x2B, 0xF3, 0xE0,0xA1, 0x0F, 0x18, 0x89, 0x4C, 0xDE, 0xAB, 0x1F,0xE9, 0x01, 0xD8, 0x13, 0x41, 0xAE, 0x17, 0x91,0xC5, 0x92, 0x75, 0xB4, 0xF6, 0xE8, 0xD9, 0xCB,0x52, 0xEF, 0xB9, 0x86, 0x54, 0x57, 0xE7, 0xC1,0x42, 0x1E, 0x31, 0x12, 0x99, 0xBD, 0x56, 0x3F,0xD2, 0x03, 0xB0, 0x26, 0x83, 0x5C, 0x2F, 0x23,0x8B, 0x24, 0xEB, 0x69, 0xED, 0xD1, 0xB3, 0x96,0xA5, 0xDF, 0x73, 0x0C, 0xA8, 0xAF, 0xCF, 0x82,0x84, 0x3C, 0x62, 0x25, 0x33, 0x7A, 0xAC, 0x7F,0xA4, 0x07, 0x60, 0x4D, 0x06, 0xB8, 0x5E, 0x47,0x16, 0x49, 0xD6, 0xD3, 0xDB, 0xA3, 0x67, 0x2D,0x4B, 0xBE, 0xE6, 0x19, 0x51, 0x5F, 0x9F, 0x05,0xFF, 0x48, 0x0E, 0xC0, 0x9A, 0x0D, 0x70, 0xBC,0x8E, 0x2C, 0x93, 0xAD, 0xA7, 0xB7, 0x46, 0xCE,0x5A, 0x97, 0x7D, 0xCC, 0x32, 0xA2, 0xBF, 0x3E,0x0A, 0x10, 0xF1, 0x88, 0x94, 0xCD, 0xEA, 0xB1,0xFE, 0x90, 0x1D, 0x81, 0x34, 0x1A, 0xE1, 0x79,0x1C, 0x59, 0x27, 0x5B, 0x4F, 0x6E, 0x8D, 0x9C,0xB5, 0x2E, 0xFB, 0x98, 0x65, 0x45, 0x7E, 0x7C,0x14, 0x21, 0xE3, 0x11, 0x29, 0x9B, 0xD5, 0x63,0xFD, 0x20, 0x3B, 0x02, 0x68, 0x35, 0xC2, 0xF2,0x38, 0xB2, 0x4E, 0xB6, 0x9E, 0xDD, 0x1B, 0x39,0x6A, 0x5D, 0xF7, 0x30, 0xCA, 0x8A, 0xFC, 0xF8,0x28, 0x43, 0xC6, 0x22, 0x53, 0x37, 0xAA, 0xC7,0xFA, 0x40, 0x76, 0x04, 0xD0, 0x6B, 0x85, 0xE4,0x71, 0x64, 0x9D, 0x6D, 0x3D, 0xBA, 0x36, 0x72,0xD4, 0xBB, 0xEE, 0x61, 0x95, 0x15, 0xF9, 0xF0,0x50, 0x87, 0x8C, 0x44, 0xA6, 0x6F, 0x55, 0x8F,0xF4, 0x80, 0xEC, 0x09, 0xA0, 0xD7, 0x0B, 0xC8,0xE2, 0xC9, 0x3A, 0xDA, 0x7B, 0x74, 0x6C, 0xE5,0xA9, 0x77, 0xDC, 0xC3, 0x2A, 0x2B, 0xF3, 0xE0,0xA1, 0x0F, 0x18, 0x89, 0x4C, 0xDE, 0xAB, 0x1F,0xE9, 0x01, 0xD8, 0x13, 0x41, 0xAE, 0x17, 0x91,0xC5, 0x92, 0x75, 0xB4, 0xF6, 0xE8, 0xD9, 0xCB,0x52, 0xEF, 0xB9, 0x86, 0x54, 0x57, 0xE7, 0xC1,0x42, 0x1E, 0x31, 0x12, 0x99, 0xBD, 0x56, 0x3F,0xD2, 0x03, 0xB0, 0x26, 0x83, 0x5C, 0x2F), True, 1, [])
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_int*1)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((8.05, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((mrg, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_gr_complex*1, 48)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, 8)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 0.5)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((-1, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-1, ))
        self.analog_sig_source_x_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 0, 1, 0)
        (self.analog_sig_source_x_2).set_max_output_buffer(4096)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, (1.0/snr)**0.5, 0)
        self.analog_agc_xx_0 = analog.agc_ff(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.analog_agc_xx_0, 0), (self.qtgui_time_sink_x_0_1_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_delay_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))
        self.connect((self.blocks_complex_to_imag_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_delay_1, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_delay_2, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.blocks_delay_2, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.isl_pmod_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_complex_to_imag_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.qtgui_time_sink_x_2_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.fft_correlator_hier_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_vector_source_x_1_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_binary_slicer_fb_1, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_1, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.dslwp_set_gain_by_tag_cc_0, 0), (self.isl_oqpsk_coherrent_demod_0, 0))
        self.connect((self.fft_correlator_hier_0, 0), (self.dslwp_set_gain_by_tag_cc_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.interp_fir_filter_xxx_1, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.isl_oqpsk_coherrent_demod_0, 1), (self.blocks_delay_2, 0))
        self.connect((self.isl_oqpsk_coherrent_demod_0, 0), (self.isl_qpsk_decimator_cc_0, 0))
        self.connect((self.isl_oqpsk_coherrent_demod_0, 0), (self.isl_qpsk_recover_cc_0, 0))
        self.connect((self.isl_pmod_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.isl_pn_generate_i_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.isl_pn_generate_i_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.isl_qpsk_decimator_cc_0, 0), (self.blocks_null_sink_0_0, 0))
        self.connect((self.isl_qpsk_decimator_cc_0, 1), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.isl_qpsk_recover_cc_0, 0), (self.interp_fir_filter_xxx_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_snr_threshold(10.0**(self.ebn0_threshold/10.0)/self.sps)
        self.set_snr(10.0**(self.ebn0/10.0)/self.sps)

    def get_ebn0_threshold(self):
        return self.ebn0_threshold

    def set_ebn0_threshold(self, ebn0_threshold):
        self.ebn0_threshold = ebn0_threshold
        self.set_snr_threshold(10.0**(self.ebn0_threshold/10.0)/self.sps)

    def get_ebn0(self):
        return self.ebn0

    def set_ebn0(self, ebn0):
        self.ebn0 = ebn0
        self.set_snr(10.0**(self.ebn0/10.0)/self.sps)

    def get_sps_pn(self):
        return self.sps_pn

    def set_sps_pn(self, sps_pn):
        self.sps_pn = sps_pn

    def get_snr_threshold(self):
        return self.snr_threshold

    def set_snr_threshold(self, snr_threshold):
        self.snr_threshold = snr_threshold
        self.fft_correlator_hier_0.set_threshold(self.snr_threshold)

    def get_snr(self):
        return self.snr

    def set_snr(self, snr):
        self.snr = snr
        self.analog_noise_source_x_0.set_amplitude((1.0/self.snr)**0.5)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)

    def get_pll_loop_bw(self):
        return self.pll_loop_bw

    def set_pll_loop_bw(self, pll_loop_bw):
        self.pll_loop_bw = pll_loop_bw

    def get_mrg(self):
        return self.mrg

    def set_mrg(self, mrg):
        self.mrg = mrg
        self.blocks_multiply_const_vxx_1.set_k((self.mrg, ))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start(16)
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
