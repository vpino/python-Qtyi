# -*- coding: utf-8 -*

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

#Creamos la calse Dialog que recibe un QDialog
class Dialogo(QDialog):
    #Inciamos el constructor
    def __init__(self):
        #Inicamos el objeto
        QDialog.__init__(self)
        #Cargos el objeto uic que hicimos con Qcreator
        uic.loadUi("check-button.ui", self)
        #Incluimos el metodo
        self.radio_value()
        #Cuando le den click al boton llamamos al metodo radio_value
        self.boton.clicked.connect(self.radio_value)
        #Incluimos el metodo
        self.checkbox_state()
        #Cuando le den click al boton llamamos al metodo radio_value
        self.boton.clicked.connect(self.checkbox_state)

    #Metodo que valida que hallan seleccionado algo de los radio button
    def radio_value(self):

        #Si el radio button python esta checked
        if self.rbPython.isChecked():
            #Si fue seleccionado le cambiamos el texto al label
            self.labelLenguaje.setText("Python ha sido seleccionado")
        # Si no, es es php
        elif self.rbPhp.isChecked():
            #Si fue seleccionado le cambiamos el texto al label
            self.labelLenguaje.setText("Php ha sido seleccionado")
        # Si no, es es ruby
        elif self.rbRuby.isChecked():
            #Si fue seleccionado le cambiamos el texto al label
            self.labelLenguaje.setText("Ruby ha sido seleccionado")
        # Si no, es es angular
        elif self.rbAngular.isChecked():
            #Si fue seleccionado le cambiamos el texto al label
            self.labelLenguaje.setText("AngularJS ha sido seleccionado")
        #Si ninguno fue seleccionado
        else:
            #Le cambiamos el texto al label
            self.labelLenguaje.setText("No ha seleccionado ningún lenguaje")

    #Metodo para saber clickearon en el check box
    def checkbox_state(self):
        #Si aceptaron los terminos
        if self.cbTerminos.isChecked():
            #Le cambiamos el texto al label
            self.labelTerminos.setText("Has aceptado los términios")
        #si no
        else:
            self.labelTerminos.setText("No has aceptado los términos")

#Iniciamos la aplicación
app = QApplication(sys.argv)
#Instanciamos un Objeto Dialogo()
dialogo = Dialogo()
#La mostramos
dialogo.show()
#Ejecutamos la aplicacion
app.exec_()
