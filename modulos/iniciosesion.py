import bcrypt
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import modulos.db_iniciosesion as comprobar


class Login(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/iniciar_sesion.ui", self)
        self.setWindowTitle("J-Medic: Inicio de Sesion")
        self.boton_iniciar.clicked.connect(self.validar_datos)
        self.validar()

    def validar(self):
        self.input_user.textChanged.connect(self.validar_usuario)
        pass

    def validar_contra(self):
        result = comprobar.comprobar_inicio_contra()
        contra = self.input_Contra.text()
        encontro = 0
        try:
            contador = 0
            for elements in result:
                if bcrypt.checkpw(contra.encode(), result[contador][0].encode()):
                    encontro += 1
                    break
                else:
                    pass
                contador += 1
            if encontro>=1:
                return True
            else:
                return False
        except:
            pass

    def validar_usuario(self):
        result = comprobar.comprobar_inicio_usuario()
        user = self.input_user.text()
        encontro = 0
        try:
            contador = 0
            for elements in result:
                if user == result[contador][0]:
                    encontro += 1
                    break
                else:
                    pass
                contador += 1
            if encontro>=1:
                return True
            else:
                return False
        except:
            pass

    def validar_datos(self):
        if self.validar_usuario() and self.validar_contra():
            QMessageBox.information(
                self, "Exito", "Ingreso correctamente", QMessageBox.Discard)
            self.login()
        else:
            QMessageBox.warning(
                self, "Error", "El usuario o la contraseña estan incorrectos", QMessageBox.Discard)

    def login(self):
        self.switch_window.emit()
