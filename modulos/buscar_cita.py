import sys, os, re, ctypes
from PyQt5 import uic, QtCore, QtWidgets

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/buscar_cita.ui", self)
        self.setWindowTitle("J-Medic: Buscar Consulta")
        self.boton_buscaridc.clicked.connect(self.switch)
        self.boton_buscaridp.clicked.connect(self.switch)
        self.boton_buscarfv.clicked.connect(self.switch)
        self.boton_mostrarc.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)

    def switch(self):
        self.switch_window.emit()