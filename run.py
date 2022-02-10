# import sys  
# from PyQt5 import QtWidgets, uic
# from pyqtgraph import PlotWidget, plot
# import pyqtgraph as pg


# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         # Загрузите страницу интерфейса
#         uic.loadUi('main.ui', self)

#         grid = QtWidgets.QGridLayout(self.centralwidget)
#         grid.addWidget(self.graphWidget, 0, 0)

#         self.plot([0, 1,2,3,4,5,6,7,8,9,10], [30, 30,32,34,32,33,31,29,32,35,45])

#     # мы добавили метод plot(), который принимает два массива: 
#     # temperature и hour, затем строит данные с помощью метода graphWidget.plot().

#     def plot(self, hour, temperature):
#         self.graphWidget.plot(hour, temperature)

#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(570, 20, 231, 431))
#         font = QtGui.QFont()
#         font.setFamily("Comic Sans MS")
#         font.setPointSize(72)
#         self.label.setFont(font)
#         self.label.setTextFormat(QtCore.Qt.AutoText)
#         self.label.setObjectName("label")
#         self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
#         self.horizontalScrollBar.setGeometry(QtCore.QRect(230, 300, 160, 16))
#         self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
#         self.horizontalScrollBar.setObjectName("horizontalScrollBar")
#         self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
#         self.progressBar.setGeometry(QtCore.QRect(230, 330, 171, 131))
#         self.progressBar.setProperty("value", 24)
#         self.progressBar.setObjectName("progressBar")
#         self.graphWidget = PlotWidget(self.centralwidget)
#         self.graphWidget.setGeometry(QtCore.QRect(30, 60, 381, 221))
#         self.graphWidget.setObjectName("graphWidget")
#         self.horizontalScrollBar.raise_()
#         self.progressBar.raise_()
#         self.label.raise_()
#         self.graphWidget.raise_()
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
# if __name__ == '__main__': 
#     app = QtWidgets.QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     sys.exit(app.exec_())


from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import numpy as np
import sys

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('main.ui', self)

        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])
        self.addToolBar(NavigationToolbar(self.widget_2.canvas, self))

    def plot(self, hour, temperature):
        self.graphWidget.plot(hour, temperature)
        t = np.arange(100)
        s = np.sin(0.15*2*np.pi*t)
        S = np.fft.fft(s)
        S_mag = np.abs(S)
        S_phase = np.angle(S)
        self.widget_1.canvas.axes.plot(t,S_mag,'.-')
        self.widget_1.canvas.axes.plot(t,S_phase,'.-')
        
        self.widget_2.canvas.axes.clear()
        self.widget_2.canvas.axes.plot(t, s)
        self.widget_2.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        self.widget_2.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.widget_2.canvas.draw()



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()