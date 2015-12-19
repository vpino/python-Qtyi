# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QMessageBox, QLabel, QPushButton, QLineEdit, QSpinBox
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Insertar datos") #Título
        self.setStyleSheet("QDialog{background-color: #FFFFFF;margin: 0;font-family: sans-serif;color: inherit;font: inherit;margin: 0;}"
                         "QPushButton{ border: none;border-radius: 2px; outline: 0; padding: 0 2rem; text-transform: uppercase; vertical-align: middle; text-decoration: none; color: #fff; background-color: #26a69a; text-align: center; }"
                         "QPushButton:hover{ background-color: #2bbbad; margin: 0; margin-left: 3rem;}"
                         "QLabel{ color: #9e9e9e; position: absolute; top: 0.8rem; left: 0.75rem;}"
                         "QLabel:hover{ color: #26a69a; }"
                         "QLineEdit{ font-family: 'Roboto'; color: #000; outline: none; background: #fff; border: none; border-bottom: 2px solid #9e9e9e;}"
                         "QLineEdit:hover{outline: none; border-bottom: 2px solid #26a69a;}"
                         "QSpinBox{ font-family: 'Roboto'; color: #000;background: #fff; border: none; border-bottom: 2px solid #9e9e9e;}"
                         "QSpinBox:hover{ outline: none; border-bottom: 2px solid #26a69a; }"
                         "QRadioButton:hover{ background: #26a69a; color: #f2f2f2; padding: 5px 15px; }"
                         "QComboBox{ font-family: 'Roboto'; color: #000; width: 20px; height: 20px; outline: none; padding: 15px; background: #fff; border: none; border-bottom: 2px solid #9e9e9e;}"
                         "QComboBox:hover{ padding: 5px 15px; outline: none; border-bottom: 2px solid #26a69a; }")

        self.resize(300, 300) #Tamaño inicial
        self.setMinimumSize(300, 300) #Tamaño mínimo
        self.setMaximumSize(300, 300) #Tamaño máximo
        self.layout = QGridLayout() #Crear un layout grid
        self.setLayout(self.layout) #Agregar el layout al cuadro de diálogo
        self.label_nombre = QLabel("Nombre:") #Etiqueta nombre
        self.txt_nombre = QLineEdit() #Campo para ingresar el nombre
        self.label_edad = QLabel("Edad:") #Etiqueta edad
        self.txt_edad = QSpinBox() #Campo para ingresar la edad
        #Botones
        self.btn_insertar = QPushButton("Insertar")
        self.btn_cancelar = QPushButton("Cancelar")

        #Agregar elementos al layout divido en dos columnas
        self.layout.addWidget(self.label_nombre, 1, 1)
        self.layout.addWidget(self.txt_nombre, 1, 2)
        self.layout.addWidget(self.label_edad, 2, 1)
        self.layout.addWidget(self.txt_edad, 2, 2)
        self.layoutButton = QGridLayout() #Layout para agrupar los botones
        #Agregar los botones al layoutButton
        self.layoutButton.addWidget(self.btn_insertar, 1, 1)
        self.layoutButton.addWidget(self.btn_cancelar, 1, 2)
        #Agregar el layoutButton en la fila 3 columna 2
        self.layout.addLayout(self.layoutButton, 3, 2)

        #Establecer conexión a la base de datos MySql
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName("localhost")
        self.db.setDatabaseName("Qtyi")
        self.db.setUserName("root")
        self.db.setPassword("11")

        self.btn_insertar.clicked.connect(self.Insertar)
        self.btn_cancelar.clicked.connect(self.Cancelar)

    def Insertar(self):
        estado = self.db.open()

        if estado == False:
            QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)
        else:
            nombre = self.txt_nombre.text()
            edad = self.txt_edad.text()
            sql = "INSERT INTO usuarios(nombre, edad) VALUES (:nombre, :edad)"
            consulta = QSqlQuery()
            consulta.prepare(sql)
            consulta.bindValue(":nombre", nombre)
            consulta.bindValue(":edad", edad)
            estado = consulta.exec_()

        if estado == True:
            QMessageBox.information(self, "Correcto", "Datos guardados", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)

        self.db.close()

    def Cancelar(self):
        self.close()

#Inciamos la aplicación
app = QApplication(sys.argv)
#Instanciamos un Objeto de la Clase Dialogo
dialogo = Dialogo()
#Lo mostramos
dialogo.show()
#Ejecutamos la aplicación
app.exec_()