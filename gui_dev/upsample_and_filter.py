#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Interpolator
# Author: Hans Erik Fjeld
# Description: Testbench for upsampling and filtering
# Generated: Mon Dec  2 20:20:44 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class upsample_and_filter(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Interpolator")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Interpolator")
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

        self.settings = Qt.QSettings("GNU Radio", "upsample_and_filter")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 60e3
        self.interpolation = interpolation = 10
        self.interpolating_fir_taps = interpolating_fir_taps = [-0.0002766616817098111, -0.00033175433054566383, -0.00036346656270325184, -0.00035864420351572335, -0.00030406005680561066, -0.00018766550056170672, -1.2533614349332111e-18, 0.00026433332823216915, 0.0006052395910955966, 0.0010158788645640016, 0.001481720944866538, 0.00198004231788218, 0.0024799767415970564, 0.002943220781162381, 0.0033254416193813086, 0.0035784076899290085, 0.0036527991760522127, 0.0035016012843698263, 0.003083934308961034, 0.002369105350226164, 0.0013406401267275214, 9.159244364165955e-18, -0.0016303149750456214, -0.0035045843105763197, -0.005552890244871378, -0.00768158957362175, -0.009775402955710888, -0.011701236478984356, -0.013313697651028633, -0.014462219551205635, -0.01499954517930746, -0.014791217632591724, -0.013725627213716507, -0.011724085547029972, -0.008750283159315586, -0.004818509798496962, 9.162128742961927e-18, 0.00557323032990098, 0.011707546189427376, 0.018150286749005318, 0.02459602802991867, 0.030696574598550797, 0.03607456386089325, 0.040340304374694824, 0.04311129078269005, 0.04403361678123474, 0.04280437156558037, 0.03919385373592377, 0.033066511154174805, 0.024399355053901672, 0.013296681456267834, 4.3851309269661405e-17, -0.01510772854089737, -0.03150426223874092, -0.04853706806898117, -0.06543925404548645, -0.08135224133729935, -0.09535452723503113, -0.10649566352367401, -0.11383428424596786, -0.11647855490446091, -0.11362738907337189, -0.1046106144785881, -0.08892614394426346, -0.06627237051725388, -0.03657403215765953, -6.126063882365261e-17, 0.04302799701690674, 0.09183673560619354, 0.1455131620168686, 0.20292629301548004, 0.2627588212490082, 0.3235474228858948, 0.3837302029132843, 0.44169947504997253, 0.49585819244384766, 0.5446767807006836, 0.5867490172386169, 0.6208443641662598, 0.6459535360336304, 0.6613271832466125, 0.6665037274360657, 0.6613271832466125, 0.6459535360336304, 0.6208443641662598, 0.5867490172386169, 0.5446767807006836, 0.49585819244384766, 0.44169947504997253, 0.3837302029132843, 0.3235474228858948, 0.2627588212490082, 0.20292629301548004, 0.1455131620168686, 0.09183673560619354, 0.04302799701690674, -6.126063882365261e-17, -0.03657403215765953, -0.06627237051725388, -0.08892614394426346, -0.1046106144785881, -0.11362738907337189, -0.11647855490446091, -0.11383428424596786, -0.10649566352367401, -0.09535452723503113, -0.08135224133729935, -0.06543925404548645, -0.04853706806898117, -0.03150426223874092, -0.01510772854089737, 4.3851309269661405e-17, 0.013296681456267834, 0.024399355053901672, 0.033066511154174805, 0.03919385373592377, 0.04280437156558037, 0.04403361678123474, 0.04311129078269005, 0.040340304374694824, 0.03607456386089325, 0.030696574598550797, 0.02459602802991867, 0.018150286749005318, 0.011707546189427376, 0.00557323032990098, 9.162128742961927e-18, -0.004818509798496962, -0.008750283159315586, -0.011724085547029972, -0.013725627213716507, -0.014791217632591724, -0.01499954517930746, -0.014462219551205635, -0.013313697651028633, -0.011701236478984356, -0.009775402955710888, -0.00768158957362175, -0.005552890244871378, -0.0035045843105763197, -0.0016303149750456214, 9.159244364165955e-18, 0.0013406401267275214, 0.002369105350226164, 0.003083934308961034, 0.0035016012843698263, 0.0036527991760522127, 0.0035784076899290085, 0.0033254416193813086, 0.002943220781162381, 0.0024799767415970564, 0.00198004231788218, 0.001481720944866538, 0.0010158788645640016, 0.0006052395910955966, 0.00026433332823216915, -1.2533614349332111e-18, -0.00018766550056170672, -0.00030406005680561066, -0.00035864420351572335, -0.00036346656270325184, -0.00033175433054566383, -0.0002766616817098111]
        self.iir_pos_coupling_scaler_0 = iir_pos_coupling_scaler_0 = [0.3,0.2,0,3]
        self.iir_pos_coupling_scaler = iir_pos_coupling_scaler = [0.3,0.2,0,3]
        self.freq = freq = 10e3

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Time')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Frequency')
        self.top_layout.addWidget(self.tab)
        self._freq_range = Range(0, 30e3, 100, 10e3, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency', "counter_slider", float)
        self.top_layout.addWidget(self._freq_win)
        self.rational_resampler_base_xxx_0 = filter.rational_resampler_base_ccc(interpolation, 1, (1, ))
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate*interpolation, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.2, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [4, 4, 3, 3, 1,
                  1, 1, 1, 1, 1]
        markers = [9, 9, 0, 0, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(4):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_freq_sink_x_0_win)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(1, (interpolating_fir_taps))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, len(interpolating_fir_taps)/2)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_base_xxx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.rational_resampler_base_xxx_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.rational_resampler_base_xxx_0, 0), (self.interp_fir_filter_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "upsample_and_filter")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate*self.interpolation)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_interpolation(self):
        return self.interpolation

    def set_interpolation(self, interpolation):
        self.interpolation = interpolation
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate*self.interpolation)

    def get_interpolating_fir_taps(self):
        return self.interpolating_fir_taps

    def set_interpolating_fir_taps(self, interpolating_fir_taps):
        self.interpolating_fir_taps = interpolating_fir_taps
        self.interp_fir_filter_xxx_0.set_taps((self.interpolating_fir_taps))
        self.blocks_delay_0.set_dly(len(self.interpolating_fir_taps)/2)

    def get_iir_pos_coupling_scaler_0(self):
        return self.iir_pos_coupling_scaler_0

    def set_iir_pos_coupling_scaler_0(self, iir_pos_coupling_scaler_0):
        self.iir_pos_coupling_scaler_0 = iir_pos_coupling_scaler_0

    def get_iir_pos_coupling_scaler(self):
        return self.iir_pos_coupling_scaler

    def set_iir_pos_coupling_scaler(self, iir_pos_coupling_scaler):
        self.iir_pos_coupling_scaler = iir_pos_coupling_scaler

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0.set_frequency(self.freq)


def main(top_block_cls=upsample_and_filter, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
