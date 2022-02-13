import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.ticker as ticker

import numpy as np


from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtMultimedia import QAudioDeviceInfo,QAudio,QCameraInfo


class MplCanvas(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		
		Fs = 1 # Hz
		N = 100
		t = np.arange(N) # because our sample rate is 1 Hz
		s = np.sin(0.15*2*np.pi*t)


		super(MplCanvas, self).__init__(fig)
		fig.tight_layout()

class MainApp(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.ui = uic.loadUi('main.ui', self)
		self.resize(888, 600)
		
		self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
		self.ui.gridLayout_4.addWidget(self.canvas, 0, 1)

		self.canvas2 = MplCanvas(self, width=5, height=4, dpi=100)
		self.ui.gridLayout_4.addWidget(self.canvas2, 1, 1)
		
		self.hs.valueChanged.connect(self.update_plot)
		self.update_plot()
		self.addToolBar(NavigationToolbar(self.canvas, self))
		self.addToolBar(NavigationToolbar(self.canvas2, self))

	def update_plot(self):
		Fs = 1 # Hz
		N = 100
		t = np.arange(N) # because our sample rate is 1 Hz
		s = np.sin(0.15*2*np.pi*t)
		self.canvas.axes.plot(t, s, "-")
		
		# print(self.hs.value()) # печатает значение слайдера

		self.canvas.axes.set_ylim( ymin=-0.5, ymax=self.hs.value())	
		self.canvas.draw()
		

		self.canvas2.axes.plot(t, s, "*")
		self.canvas2.draw()

app = QtWidgets.QApplication(sys.argv)
mainWindow = MainApp()
mainWindow.show()
sys.exit(app.exec_())
