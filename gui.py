import sys
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.ticker as ticker

import numpy as np

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtMultimedia import QAudioDeviceInfo, QAudio, QCameraInfo


"""
кастомный класс для рисования матплолибовских графиков в виджете pyqt
"""
class MplCanvas(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)

		super(MplCanvas, self).__init__(fig)
		fig.tight_layout()

"""
Класс, создающий объект окна pyqt
"""
class MainApp(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.ui = uic.loadUi('main.ui', self)
		self.resize(888, 600)

		self.canvas = MplCanvas(self, width=5, height=4, dpi=100) # график номер 1
		self.ui.gridLayout_4.addWidget(self.canvas, 0, 1)

		self.canvas2 = MplCanvas(self, width=5, height=4, dpi=100) # график номер 2
		self.ui.gridLayout_4.addWidget(self.canvas2, 1, 1)

		self.hs.valueChanged.connect(self.update_plot) # метод, навешивающий действие
		self.update_plot() # функция, которая рисует графики (см эту функцию ниже)
		self.addToolBar(NavigationToolbar(self.canvas, self)) # добавляет тулбар для первого графика вверх окна
		self.addToolBar(NavigationToolbar(self.canvas2, self)) # добавляет тулбар для второго графика вверх окна

	# функция, ресующая графики
	def update_plot(self):
		# матан
		N = 100
		t = np.arange(N)  # because our sample rate is 1 Hz
		s = np.sin(0.15 * 2 * np.pi * t)

		self.canvas.axes.plot(t, s, "-") # задаёт второй график
		# print(self.hs.value()) # печатает значение слайдера

		"""
		меняет пределы игрек (минимум = -0,5, максимум берёт вторым из значения слайдера)
		"""
		self.canvas.axes.set_ylim(ymin=-0.5, ymax=self.hs.value())
		self.canvas.draw() # рисует первый график

		self.canvas2.axes.plot(t, s, "*") # задаёт второй график
		self.canvas2.draw() # рисует второй график


if __name__ == "__main__": #запускает шарманку
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = MainApp()
	mainWindow.show()
	sys.exit(app.exec_())
