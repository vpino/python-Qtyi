# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

#Creamos la clase Dialog que recibe un QDialog
class Dialogo(QDialog):
    #Inciamos el constructor
    def __init__(self):
        #Iniciamos el objeto QDialog
        QDialog.__init__(self)
        #Cargo el objeto ui que hicimos con Qcreator
        uic.loadUi("sliders.ui", self)

        #Horizontal Slider
        #Rango minimo permitido
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        #Definimos los pasos de 1 en 1
        self.horizontalSlider.setSingleStep(1)
        #Valor por defecto
        self.horizontalSlider.setValue(50)
        #Llamos al meotodo getValueHorizontal cuando el slider cambie de valor
        self.horizontalSlider.valueChanged.connect(self.getValueHorizontal)

        #Vertical Slider
        #Rango minimo permitido
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(1000)
        #Definimos los pasos de 1 en 1
        self.verticalSlider.setSingleStep(10)
        #Valor por defecto
        self.verticalSlider.setValue(500)
        #Llamos al meotodo getValueHorizontal cuando el slider cambie de valor
        self.verticalSlider.valueChanged.connect(self.getValueVertical)

    #Metodo cuando se cambie el valor del slider
    def getValueHorizontal(self):
        #Guardamos el valor del slider
        value = self.horizontalSlider.value()
        #Se lo pasamos a la etiqueta label
        self.labelHorizontal.setText(str(value))

    #Metodo cuando se cambie el valor del slider vertical
    def getValueVertical(self):
        #Guardamos el valor del slider
        value = self.verticalSlider.value()
        #Se lo pasamos a la etiqueta label
        self.labelVertical.setText(str(value))


#Inciamos la aplicación
app = QApplication(sys.argv)
#Instanciamos un Objeto de la Clase Dialogo
dialogo = Dialogo()
#Lo mostramos
dialogo.show()
#Ejecutamos la aplicación
app.exec_()
