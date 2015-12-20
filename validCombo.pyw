# -*- coding: utf-8 -*

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QComboBox
from PyQt5 import uic
from PyQt5 import QtCore

class Communicate(QtCore.QObject):

    closeApp = QtCore.pyqtSignal()


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
        self.cmbLenguajes.activated.connect(self.getListaPackages)
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

     #Metodo que llena la lista de paquete seleccionada en el cmbox
    def getListaPackages(self):

        #Guardamops en una variable el item seleccionado
        item = self.cmbLenguajes.currentText()

        if item == "C++":

            infile = open('canaima-cinnamon.list.chroot', 'r')
            # Mostramos por pantalla lo que leemos desde el fichero
            print('>>> Lectura del fichero línea a línea')
            for line in infile:
                print(line)
            # Cerramos el fichero.
            infile.close()


#Inciamos la aplicacion
app = QApplication(sys.argv)
#Instanciamos un objeto de la clase Dialogo
dialogo = Dialogo()
#Lo mostramos
dialogo.show()
#Ejecutamos la aplicación
app.exec_()