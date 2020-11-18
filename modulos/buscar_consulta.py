import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/buscar_consultas.ui", self)
        self.setWindowTitle("J-Medic: Buscar Consulta")
        self.boton_buscarid.clicked.connect(self.switch)
        self.boton_buscarmed.clicked.connect(self.switch)
        self.boton_buscarpac.clicked.connect(self.switch)
        self.boton_buscarmotivo.clicked.connect(self.switch)
        self.boton_buscarfecha.clicked.connect(self.switch)
        self.boton_mostrartodo.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)

    def switch(self):
        self.switch_window.emit()
