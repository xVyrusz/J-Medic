import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import modulos.db_Pacientes as pacientes


class WindowTree(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Editar Pacientes.ui", self)
        self.setWindowTitle("J-Medic: Editar Paciente")
        self.boton_buscar.clicked.connect(self.validar_datos)
        self.boton_guardar.clicked.connect(self.validar_datos_2)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_ID_Paciente.textChanged.connect(self.validar_id_paciente)
        self.input_Nombre.textChanged.connect(self.validar_nombre)
        self.input_ApellidoP.textChanged.connect(self.validar_apellidoP)
        self.input_ApellidoM.textChanged.connect(self.validar_apellidoM)
        self.input_Telefono.textChanged.connect(self.validar_telefono)
        pass

    def validar_id_paciente(self):
        id_paciente = self.input_ID_Paciente.text()
        validar = re.match("^\d{1,}$", id_paciente, re.I)
        if id_paciente == "":
            self.input_ID_Paciente.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_ID_Paciente.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_ID_Paciente.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos(self):
        if self.validar_id_paciente():
            result = pacientes.buscar_pacientes_id(
                int(self.input_ID_Paciente.text()))
            print(result)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            # self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda = result
            try:
                self.tabla_pacientes.setItem(
                    0, 0, QTableWidgetItem(str(ayuda[0])))
                self.tabla_pacientes.setItem(0, 1, QTableWidgetItem(ayuda[1]))
                self.tabla_pacientes.setItem(0, 2, QTableWidgetItem(ayuda[2]))
                self.tabla_pacientes.setItem(0, 3, QTableWidgetItem(ayuda[3]))
                self.tabla_pacientes.setItem(0, 4, QTableWidgetItem(ayuda[4]))
                self.tabla_pacientes.setItem(
                    0, 5, QTableWidgetItem(str(ayuda[5])))
                self.tabla_pacientes.setItem(
                    0, 6, QTableWidgetItem(str(ayuda[6])))
                self.tabla_pacientes.setItem(
                    0, 7, QTableWidgetItem(str(ayuda[7])))
                self.tabla_pacientes.setItem(0, 8, QTableWidgetItem(ayuda[8]))
                self.tabla_pacientes.setItem(0, 9, QTableWidgetItem(ayuda[9]))
                self.tabla_pacientes.setItem(
                    0, 10, QTableWidgetItem(ayuda[10]))
                self.input_Nombre.setText(str(ayuda[1]))
                self.input_ApellidoP.setText(str(ayuda[2]))
                self.input_ApellidoM.setText(str(ayuda[3]))
                self.input_sexo.setText(str(ayuda[4]))
                self.input_Peso.setText(str(ayuda[5]))
                self.input_estatura.setText(str(ayuda[6]))
                self.input_anios.setText(str(ayuda[7]))
                self.input_Telefono.setText((ayuda[8]))
                self.input_sangre.setText(str(ayuda[9]))
                self.input_Alergias.setText(str(ayuda[10]))
            except:
                QMessageBox.warning(
                    self, "Error", "No se ha encontrado nada", QMessageBox.Discard)

            #QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            # self.switch()
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def validar_nombre(self):
        nombre = self.input_Nombre.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", nombre, re.I)
        if nombre == "":
            self.input_Nombre.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Nombre.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Nombre.setStyleSheet("border: 2px solid green;")
            return True

    def validar_apellidoP(self):
        apellido = self.input_ApellidoP.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", apellido, re.I)
        if apellido == "":
            self.input_ApellidoP.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_ApellidoP.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_ApellidoP.setStyleSheet("border: 2px solid green;")
            return True

    def validar_apellidoM(self):
        apellido = self.input_ApellidoM.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", apellido, re.I)
        if apellido == "":
            self.input_ApellidoM.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_ApellidoM.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_ApellidoM.setStyleSheet("border: 2px solid green;")
            return True

    def validar_sexo(self):
        sexo = self.combo_sexo.currentText()
        self.input_sexo.setText(str(sexo))
        sexo = self.input_sexo.text()
        if sexo == "":
            self.input_sexo.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_sexo.setStyleSheet("border: 2px solid green;")
            return True

    def validar_peso(self):
        pesok = self.comboBox.currentText()
        pesog = self.comboBox_2.currentText()
        cont = 0
        if pesog == "":
            cont += 1

        if pesok == "":
            cont += 1

        self.input_Peso.setText(str(pesok)+(pesog))
        if cont > 0:
            self.input_Peso.setText("")

        peso = self.input_Peso.text()
        if peso == "":
            self.input_Peso.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_Peso.setStyleSheet("border: 2px solid green;")
            return True

    def validar_estatura(self):
        estaturam = self.comboBox_3.currentText()
        estaturacm = self.comboBox_4.currentText()
        cont = 0
        if estaturacm == "":
            cont += 1

        if estaturam == "":
            cont += 1

        self.input_estatura.setText(str(estaturam)+(estaturacm))
        if cont > 0:
            self.input_estatura.setText("")

        estatura = self.input_estatura.text()
        if estatura == "":
            self.input_estatura.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_estatura.setStyleSheet("border: 2px solid green;")
            return True

    def validar_anios(self):
        anios = self.comboBox_5.currentText()
        self.input_anios.setText(str(anios))
        anios = self.input_anios.text()
        if anios == "":
            self.input_anios.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_anios.setStyleSheet("border: 2px solid green;")
            return True

    def validar_telefono(self):
        telefono = self.input_Telefono.text()
        validar = re.match("^\d{10}$", telefono, re.I)
        if telefono == "":
            self.input_Telefono.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Telefono.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Telefono.setStyleSheet("border: 2px solid green;")
            return True

    def validar_sangre(self):
        sangre = self.input_TipoS.currentText()
        self.input_sangre.setText(str(sangre))
        sangre = self.input_sangre.text()
        if sangre == "":
            self.input_sangre.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_sangre.setStyleSheet("border: 2px solid green;")
            return True

    def validar_alergia(self):
        alergias = self.input_Alergias.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", alergias, re.I)
        if alergias == "":
            self.input_Alergias.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Alergias.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Alergias.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_2(self):
        if self.validar_nombre() and self.validar_sexo() and self.validar_apellidoP() and self.validar_peso() and self.validar_apellidoM() and self.validar_estatura() and self.validar_telefono() and self.validar_anios() and self.validar_alergia() and self.validar_sangre():
            sangre = ''
            if self.input_sangre.text() == 'A+':
                sangre = '1'
            elif self.input_sangre.text() == 'A-':
                sangre = '2'
            elif self.input_sangre.text() == 'AB+':
                sangre = '3'
            elif self.input_sangre.text() == 'AB-':
                sangre = '4'
            elif self.input_sangre.text() == 'B+':
                sangre = '5'
            elif self.input_sangre.text() == 'B-':
                sangre = '6'
            elif self.input_sangre.text() == 'O+':
                sangre = '7'
            elif self.input_sangre.text() == 'O-':
                sangre = '8'
            else:
                sangre = '1'
            # result=pacientes.buscar_pacientes_id(int(self.input_ID_Paciente.text()))
            result = pacientes.editar_pacientes(self.input_Nombre.text(), self.input_ApellidoP.text(), self.input_ApellidoM.text(), self.input_sexo.text(), self.input_Peso.text(
            ), self.input_estatura.text(), self.input_anios.text(), self.input_Telefono.text(), self.input_Alergias.toPlainText(), sangre, self.input_ID_Paciente.text())
            # self.input_ApellidoP.text(),self.input_ApellidoM.text(),self.input_sexo.text(),self.input_Peso.text(),self.input_estatura.text(),self.input_anios.text(),self.input_Telefono.text(),self.input_Alergias.toPlainText(),sangre,
            # result=pacientes.editar_pacientes(sangre,self.input_ID_Paciente.text())
            # result2=pacientes.editar_pacientes(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[10],sangre)
            print(result)
            QMessageBox.information(
                self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
