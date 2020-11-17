import sys, os, re, ctypes
from PyQt5 import uic, QtCore, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("J-Medic: Menu 1")
        uic.loadUi("interfaces/menu.ui", self)
        self.boton_AgregarMedico.clicked.connect(self.switch)

    def switch(self):
        self.switch_window.emit()