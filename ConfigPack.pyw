# -*- coding: utf-8 -*-

import sys, requests

from PyQt5.QtWidgets import QApplication, QDialog, QComboBox, QListWidget, QMessageBox, QInputDialog
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
        self.cmbEscri.activated.connect(self.getListaPackages)

        #Cargamos la lista de paquetes de la arquitectura seleccion
        self.cmbArqui.activated.connect(self.getListaPackages)

        #Cargamos la lista de paquetes de la arquitectura seleccion
        self.cmbDist.activated.connect(self.getListaPackages)

        #Cuando le den click al boton añadir llamamos al metodo setListEnd
        self.btnAdd.clicked.connect(self.setListEnd)

        #Cuando le den click al boton quitar llamamos al metodo deletePackEnd
        self.btnRemo.clicked.connect(self.deletePackEnd)

        #Cuando le den click al boton cancelar llamamos al metodo Cancelar
        self.btnCancel.clicked.connect(self.Cancelar)

        #Cuando le den click al boton Añadir paquete nuevo llamamos al metodo addPackage
        self.btnAddNew.clicked.connect(self.addPackage)


    #Metodo que llena la lista de paquete seleccionada en el cmbox
    def getListaPackages(self):

        #Definimos un diccionario con los escritorios
        escritorios = { '1': "cinnamon", '2': "mate"}

        #Definimos un diccionario con las arquitectura
        arquitectura = { '1': "amd64", '2': "i386", '3': "i586"}

        #Definimos un diccionario con las distribuciones
        distribuciones = { '1': "", '2': "edu"}

        #Guardamops en una variable el escritorio seleccionado
        escri = self.cmbEscri.currentIndex()

        #Guardamops en una variable la arquitectura seleccionada
        arqui = self.cmbArqui.currentIndex()

        #Guardamops en una variable la distro seleccionada
        distro = self.cmbDist.currentIndex()

        if escri != 0 & arqui != 0 & distro != 0:

            try:

                #Limpiamos la lista
                self.listIni.clear()

                #Obtenemos la lista de los paquetes genericos de la api generada
                r = requests.get('http://127.0.0.1:8000/api/0.1/paquetes-generic/?format=json')

                a = r.json()['objects'][0]

                print a

                ######### Manera vieja ############
                #distro = arqui[str(item)]

                 #Abrimos el archivo de la aquitectura que hallan seleccionado
                #infile = open('config/canaima-' + distro + '.list.chroot', 'r')

                # Y hacemos un for para leer linea por linea y agregarlo al listWidget
                #for line in infile:
                    #self.listIni.addItem(line)
                # Cerramos el fichero.
                #infile.close()
                ######### Manera vieja ############

            except:

                #Limpiamos la lista
                self.listIni.clear()
                QMessageBox.warning(self, "Canaima Semilla", "Debe Seleccionar una arquitectura", QMessageBox.Discard)

    #Metodo para agregar un paquete a la lista final
    def setListEnd(self):

        #Guardamos en una variable el item seleccionado
        item = self.listIni.selectedItems()[0].text()

        #Si hay elementos en la lista, hacemos la comprobación
        if self.listFin.count() > 0:

            #Recorremos item a item. El metodo count nos devuelve cuantos items tiene la lista
            for x in range(self.listFin.count()):

                #Comprobamos si el paquete esta en la lista, le enviamos un msj de duplicado y lo sacamos de la función
                if self.listFin.item(x).text() == item:

                    QMessageBox.warning(self, "Paquete Duplicadado", "El Paquete seleccionado ya se encuentra en la lista",
                                        QMessageBox.Discard)
                    return

            #Añadimos el elemento seleccionado
            self.listFin.addItem(item)

        #Si no hay elementos en la lista, agregamos el primer paquete
        else:

            #Añadimos el elemento seleccionado
             self.listFin.addItem(item)

    #Metodo para quitar un paquete de la lista
    def deletePackEnd(self):

        #Eliminamos el elemento de la lista seleccionado, con el metodo currentRow obtenemos el index
        self.listFin.model().removeRow(self.listFin.currentRow())

    #Meotdo para cerrar la ventana
    def Cancelar(self):
        self.close()

    #Metodo para agregar un paquete nuevo a la lista
    def addPackage(self):

        text, ok = QInputDialog.getText(self, 'Nuevo Paquete',
            'Ingrese el nuevo paquete:')

        if ok:
            item = str(text)

            #Si hay elementos en la lista, hacemos la comprobación
            if self.listFin.count() > 0:

                #Recorremos item a item. El metodo count nos devuelve cuantos items tiene la lista
                for x in range(self.listFin.count()):

                    #Comprobamos si el paquete esta en la lista, le enviamos un msj de duplicado y lo sacamos de la función
                    if self.listFin.item(x).text() == item:

                        QMessageBox.warning(self, "Paquete Duplicadado", "El Paquete que intenta agregar ya se encuentra en "
                                                                         "la lista",
                                            QMessageBox.Discard)
                        return

                #Añadimos el elemento seleccionado
                self.listFin.addItem(item)

            #Si no hay elementos en la lista, agregamos el primer paquete
            else:

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