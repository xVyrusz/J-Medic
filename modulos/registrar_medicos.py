import sys, os, re, ctypes
from PyQt5 import uic, QtCore, QtWidgets

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("J-Medic: Menu 1")
        uic.loadUi("interfaces/Registrar Medicos.ui", self)
        self.Boton_Guardar.clicked.connect(self.close)