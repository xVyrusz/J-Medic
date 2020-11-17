import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets


class WindowTree(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/editar_cita.ui", self)
        self.setWindowTitle("J-Medic: Editar Cita")
        self.boton_buscarc.clicked.connect(self.switch)
        self.boton_agendar.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)

    def switch(self):
        self.switch_window.emit()
