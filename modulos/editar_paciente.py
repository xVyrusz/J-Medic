import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets


class WindowTree(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Editar Pacientes.ui", self)
        self.setWindowTitle("J-Medic: Editar Paciente")
        self.boton_buscar.clicked.connect(self.switch)
        self.boton_guardar.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)

    def switch(self):
        self.switch_window.emit()
