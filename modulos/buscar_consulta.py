import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import modulos.db_Consultas as consultas

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/buscar_consultas.ui", self)
        self.setWindowTitle("J-Medic: Buscar Consulta")
        self.boton_buscarid.clicked.connect(self.validar_datos_idc)
        self.boton_buscarmed.clicked.connect(self.validar_datos_nombre_medico)
        self.boton_buscarpac.clicked.connect(self.validar_datos_nombre_paciente)
        self.boton_buscarmotivo.clicked.connect(self.validar_datos_motivo)
        self.boton_buscarfecha.clicked.connect(self.validar_datos_fecha)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_idc.textChanged.connect(self.validar_id_consulta)
        self.input_medico.textChanged.connect(self.validar_nombre_medico)
        self.input_paciente.textChanged.connect(self.validar_nombre_paciente)
        self.input_motivo.textChanged.connect(self.validar_motivo)
        pass

    def validar_id_consulta(self):
        id_consulta = self.input_idc.text()
        validar = re.match("^\d{1,}$", id_consulta, re.I)
        if id_consulta == "":
            self.input_idc.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_idc.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_idc.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_idc(self):
        if self.validar_id_consulta():
            result=consultas.buscar_consulta_id(int(self.input_idc.text()))
            print (result)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            #self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda = result

            try:
                self.tabla_consultas.setItem(0 , 0, QTableWidgetItem(str(ayuda[0])))
                self.tabla_consultas.setItem(0 , 1, QTableWidgetItem(ayuda[1]))
                self.tabla_consultas.setItem(0 , 2, QTableWidgetItem(str(ayuda[2])))
                self.tabla_consultas.setItem(0 , 3, QTableWidgetItem(ayuda[3]))
                self.tabla_consultas.setItem(0 , 4, QTableWidgetItem(ayuda[4]))
                self.tabla_consultas.setItem(0 , 5, QTableWidgetItem(str(ayuda[5])))
                self.tabla_consultas.setItem(0 , 6, QTableWidgetItem(str(ayuda[6])))
                self.tabla_consultas.setItem(0 , 7, QTableWidgetItem(str(ayuda[7])))
                self.tabla_consultas.setItem(0 , 8, QTableWidgetItem(ayuda[8]))
                self.tabla_consultas.setItem(0 , 9, QTableWidgetItem(ayuda[9]))
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            #QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            #s¿self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def validar_nombre_medico(self):
        nombre = self.input_medico.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", nombre, re.I)
        if nombre == "":
            self.input_medico.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_medico.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_medico.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_nombre_medico(self):
        if self.validar_nombre_medico():
            result=consultas.buscar_consulta_medicos(self.input_medico.text())
            print (result)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            #self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda = result

            try:
                if ayuda:
                    contador = 0
                    for elements in ayuda:
                        self.tabla_consultas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                        self.tabla_consultas.setItem(contador , 1, QTableWidgetItem(ayuda[contador][1]))
                        self.tabla_consultas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                        self.tabla_consultas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                        self.tabla_consultas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                        self.tabla_consultas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                        self.tabla_consultas.setItem(contador , 6, QTableWidgetItem(str(ayuda[contador][6])))
                        self.tabla_consultas.setItem(contador , 7, QTableWidgetItem(str(ayuda[contador][7])))
                        self.tabla_consultas.setItem(contador , 8, QTableWidgetItem(ayuda[contador][8]))
                        self.tabla_consultas.setItem(contador , 9, QTableWidgetItem(ayuda[contador][9]))
                        contador+=1
                else:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


    def validar_nombre_paciente(self):
        nombre = self.input_paciente.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", nombre, re.I)
        if nombre == "":
            self.input_paciente.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_paciente.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_paciente.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_nombre_paciente(self):
        if self.validar_nombre_paciente():
            result=consultas.buscar_consulta_nombre_paciente(self.input_paciente.text())
            print (result)
            ayuda = result

            try:
                if ayuda:
                    contador = 0
                    for elements in ayuda:
                        self.tabla_consultas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                        self.tabla_consultas.setItem(contador , 1, QTableWidgetItem(ayuda[contador][1]))
                        self.tabla_consultas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                        self.tabla_consultas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                        self.tabla_consultas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                        self.tabla_consultas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                        self.tabla_consultas.setItem(contador , 6, QTableWidgetItem(str(ayuda[contador][6])))
                        self.tabla_consultas.setItem(contador , 7, QTableWidgetItem(str(ayuda[contador][7])))
                        self.tabla_consultas.setItem(contador , 8, QTableWidgetItem(ayuda[contador][8]))
                        self.tabla_consultas.setItem(contador , 9, QTableWidgetItem(ayuda[contador][9]))
                        contador+=1
                else:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


    def validar_motivo(self):
        motivos = self.motivo.currentText()
        self.input_motivo.setText(str(motivos))
        motivo = self.input_motivo.text()
        if motivo == "":
            self.input_motivo.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_motivo.setStyleSheet("border: 2px solid green;")
            return True


    def validar_datos_motivo(self):
        if self.validar_motivo():
            moti = 0
            if self.input_motivo.text() == 'Consulta general':
                moti = 1
            elif self.input_motivo.text() == 'Exámenes':
                moti = 2
            elif self.input_motivo.text() == 'Curaciones':
                moti = 3
            else:
                moti = 1
            result=consultas.buscar_consulta_motivo(moti)
            print (result)
            ayuda = result
            try:
                if ayuda:
                    contador = 0
                    for elements in ayuda:
                        self.tabla_consultas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                        self.tabla_consultas.setItem(contador , 1, QTableWidgetItem(ayuda[contador][1]))
                        self.tabla_consultas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                        self.tabla_consultas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                        self.tabla_consultas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                        self.tabla_consultas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                        self.tabla_consultas.setItem(contador , 6, QTableWidgetItem(str(ayuda[contador][6])))
                        self.tabla_consultas.setItem(contador , 7, QTableWidgetItem(str(ayuda[contador][7])))
                        self.tabla_consultas.setItem(contador , 8, QTableWidgetItem(ayuda[contador][8]))
                        self.tabla_consultas.setItem(contador , 9, QTableWidgetItem(ayuda[contador][9]))
                        contador+=1
                else:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


    def seleccionar_fecha(self):
        anio = self.comboBox_4.currentText()
        mes = self.comboBox_3.currentText()
        dia = self.comboBox_2.currentText()
        cont = 0
        if anio == "":
            cont+=1

        if mes == "":
            cont+=1

        if dia == "":
            cont+=1

        self.input_fecha.setText(str(anio)+(mes)+(dia))
        if cont>0:
            self.input_fecha.setText("")

        fecha = self.input_fecha.text()
        if fecha == "":
            self.input_fecha.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_fecha.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_fecha(self):
        if self.seleccionar_fecha():
            result=consultas.buscar_consulta_fecha(str(self.input_fecha.text()))
            print (result)
            ayuda = result

            try:
                if ayuda:
                    contador = 0
                    for elements in ayuda:
                        self.tabla_consultas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                        self.tabla_consultas.setItem(contador , 1, QTableWidgetItem(ayuda[contador][1]))
                        self.tabla_consultas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                        self.tabla_consultas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                        self.tabla_consultas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                        self.tabla_consultas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                        self.tabla_consultas.setItem(contador , 6, QTableWidgetItem(str(ayuda[contador][6])))
                        self.tabla_consultas.setItem(contador , 7, QTableWidgetItem(str(ayuda[contador][7])))
                        self.tabla_consultas.setItem(contador , 8, QTableWidgetItem(ayuda[contador][8]))
                        self.tabla_consultas.setItem(contador , 9, QTableWidgetItem(ayuda[contador][9]))
                        contador+=1
                else:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
