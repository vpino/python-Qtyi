# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QComboBox, QListWidget
from PyQt5 import uic

#Creamos la clase ConfigPack que recibe un QDialog
class ConfigPack(QDialog):
    #Inciamos el Constructor
    def __init__(self):

        #Iniciamos el Objeto QDialog
        QDialog.__init__(self)

        #Cargamos el archivo ui que contiene la interfaz hecha
        uic.loadUi("frmConfigPack.ui", self)

        #Cargamos la lista de paquetes de la arquitectura seleccionada en el combo box
        self.cmbArqui.activated.connect(self.getListaPackages)

        #Cuando le den click al boton añadir llamamos al metodo setListEnd
        self.btnAdd.clicked.connect(self.setListEnd)

    #Metodo que llena la lista de paquete seleccionada en el cmbox
    def getListaPackages(self):

        #Definimos un diccionario con las distribuciones
        arqui = { '1': "cinnamon", '2': "cinnamon", '3': "cinnamon-edu", '4': "mate", '5': "mate", '6': "mate-edu"}

         #Guardamops en una variable el item seleccionado del cmbox
        item = self.cmbArqui.currentIndex()

        try:

            distro = arqui[str(item)]

             #Abrimos el archivo de la aquitectura que hallan seleccionado
            infile = open('config/canaima-' + distro + '.list.chroot', 'r')

            # Y hacemos un for para leer linea por linea y agregarlo al listWidget
            for line in infile:
                self.listIni.addItem(line)
            # Cerramos el fichero.
            infile.close()

        except:
            print("Debe seleccionar una arquitectura")

    #Metodo para agregar un paquete a la lista final
    def setListEnd(self):

        #Guardamos en una variable el item seleccionado
        item = self.listIni.selectedItems()[0].text()

        #Añadimos el elemento seleccionado
        self.listFin.addItem(item)








#Inciamos la aplicacion
app = QApplication(sys.argv)
#Instanciamos un objeto de la clase configPack
configPack = ConfigPack()
#Lo mostramos
configPack.show()
#Ejecutamos la aplicación
app.exec_()