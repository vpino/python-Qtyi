# -*- coding: utf-8 -*

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

#Creamos la calse Dialog que recibe un QDialog
class Dialogo(QDialog):
    #Inciamos el constructor
    def __init__(self):
        #Iniciamos el objeto
        QDialog.__init__(self)
        #Cargos el objeto uic que hicimos con Qcreator
        uic.loadUi("combo-box.ui", self)
        #Cuando le den click al boton llamamos al metodo getItem
        self.boton.clicked.connect(self.getItem)
        #Agregar un nuevo item al combo
        self.cmbLenguajes.addItem("C++")
        #Eliminar un item
        self.cmbLenguajes.removeItem(0)

    #Metodo que te devuelve el item del cmb seleccionado
    def getItem(self):
        #Guardamops en una variable el item seleccionado
        item = self.cmbLenguajes.currentText()
        #Mostramos en el label el lenguaje seleccionado
        self.labelLenguaje.setText("Has seleccionado: "+ item)

#Inciamos la aplicacion
app = QApplication(sys.argv)
#Instanciamos un objeto de la clase Dialogo
dialogo = Dialogo()
#Lo mostramos
dialogo.show()
#Ejecutamos la aplicación
app.exec_()