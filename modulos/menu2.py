import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    switch_window6 = QtCore.pyqtSignal()
    switch_window7 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/menu2.ui", self)
        self.setWindowTitle("J-Medic: Menu 2")
        self.boton_editar_paciente.clicked.connect(self.switch)
        self.boton_editar_medico.clicked.connect(self.switch2)
        self.boton_editar_consulta.clicked.connect(self.switch3)
        self.boton_editar_citas.clicked.connect(self.switch4)
        self.boton_eliminar_consulta.clicked.connect(self.switch5)
        self.boton_eliminar_cita.clicked.connect(self.switch6)
        self.boton_regresar.clicked.connect(self.switch7)

    def switch(self):
        self.switch_window.emit()

    def switch2(self):
        self.switch_window2.emit()

    def switch3(self):
        self.switch_window3.emit()

    def switch4(self):
        self.switch_window4.emit()

    def switch5(self):
        self.switch_window5.emit()

    def switch6(self):
        self.switch_window6.emit()

    def switch7(self):
        self.switch_window7.emit()
