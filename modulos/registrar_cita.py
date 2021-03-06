import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import modulos.db_cita as cita

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/agendar_cita.ui", self)
        self.setWindowTitle("J-Medic: Registrar Cita")
        self.boton_agendar_cita.clicked.connect(self.validar_datos)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_idp.textChanged.connect(self.validar_id_paciente)
        self.input_fecha.textChanged.connect(self.validar_fecha)
        pass


    def validar_id_paciente(self):
        id_paciente = self.input_idp.text()
        validar = re.match("^\d{1,}$", id_paciente, re.I)
        if id_paciente == "":
            self.input_idp.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_idp.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_idp.setStyleSheet("border: 2px solid green;")
            return True

    def validar_fecha(self):
        anio = self.comboBox_4.currentText()
        mes = self.comboBox_3.currentText()
        dia = self.comboBox_2.currentText()
        hora = self.comboBox.currentText()
        minutos = self.comboBox_5.currentText()
        cont = 0
        if anio == "":
            cont+=1

        if mes == "":
            cont+=1

        if dia == "":
            cont+=1

        if hora == "":
            cont+=1

        if minutos == "":
            cont+=1

        
        if cont>0:
            self.input_fecha.setText("")
        else:
            self.input_fecha.setText(anio+'-'+mes+'-'+dia+hora+minutos)
            fecha = self.input_fecha.text()
            if fecha == "":
                self.input_fecha.setStyleSheet("border: 2px solid yellow;")
                return False
            else:
                self.input_fecha.setStyleSheet("border: 2px solid green;")
                return True

        



    def validar_datos(self):
        if self.validar_id_paciente() and self.validar_fecha():
            result=cita.insertar_cita(self.input_idp.text(),self.input_fecha.text())
            if result == 1:
                result2 =cita.mostrar_citas()
                print(result2)

                ayuda = result2

                try:
                    if ayuda:
                        contador = 0
                        for elements in ayuda:
                            self.tabla_citas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                            self.tabla_citas.setItem(contador , 1, QTableWidgetItem(str(ayuda[contador][1])))
                            self.tabla_citas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                            self.tabla_citas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                            self.tabla_citas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                            self.tabla_citas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                            contador+=1
                    else:
                        QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
                except:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
                #QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
                #self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
