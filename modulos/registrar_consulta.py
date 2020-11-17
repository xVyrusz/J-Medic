import sys, os, re, ctypes
from PyQt5 import uic, QtCore, QtWidgets

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Nueva_consulta.ui", self)
        self.setWindowTitle("J-Medic: Registrar Consulta")
        self.guardar_consulta.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)

    def switch(self):
        self.switch_window.emit()