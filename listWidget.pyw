# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

#Creamos la clase Dialog que recibe un QDialog
class Dialogo(QDialog):
    #Inciamos el constructor
    def __init__(self):
        #Iniciamos el objeto
        QDialog.__init__(self)
        #Cargo el objeto uic que hicimos con Qcreator
        uic.loadUi("list-widget.ui", self)
        #Cuando le den click al boton llamamos al metodo getItems
        self.boton.clicked.connect(self.getItems)
        #Agregar un nuevo item a la lista
        self.listLenguajes.addItem("BASH")
        #Eliminamos un elemento de la lista
        self.deleteItem("AngularJs")

    #Metodo para eliminar un item de la lista recibe como parametro el nombre del label a eliminar
    def deleteItem(self, label):
        #Array para almacenar cada item objeto
        items = []
        #Recorremos item a item. El metodo count nos devuelve cuantos items tiene la lista
        for x in range(self.listLenguajes.count()):
            #Añadimos el item a la lista de items
            items.append(self.listLenguajes.item(x))

        #Este array almacena el texto de cada item de la lista
        labels = [i.text() for i in items]
        #Recorremos item a item del array labels el cual contiene el texto de los elementos de la lista
        for x in range(len(labels)):
            #Comprobamos si el elemento ya existe en la lista
            if labels[x] == label:
                #Si existe lo eliminamos
                #Obtenemos el index del elemento
                item = self.listLenguajes.indexFromItem(self.listLenguajes.item(x))
                #Eliminamos el elemento de la lista
                self.listLenguajes.model().removeRow(item.row())


    #Definimos un metodo para obtener los items seleccionados por el usuario
    def getItems(self):
        #Guardamos los items seleccionados
        items = self.listLenguajes.selectedItems()
        #Array para guardar los items seleccionados
        selected = []
        for x in range(len(items)):
            #Agregamos cada item al array selected
            selected.append(self.listLenguajes.selectedItems()[x].text())

        #Mostramos los items seleccionados
        self.labelLenguajes.setText("Seleccionados: "+ "-".join(selected))


#Iniciamos la aplicación
app = QApplication(sys.argv)
#Instanciamos un obejto de la clase Dialogo
dialogo = Dialogo()
#La mostramos
dialogo.show()
#Ejecutamos la aplicación
app.exec_()