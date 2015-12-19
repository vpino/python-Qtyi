# -*- coding: utf-8 -*-

import sys, time, os, subprocess
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5 import uic
from os import listdir, path, stat
from mimetypes import MimeTypes

#Creamos la clase Dialog que recibe un QDialog
class Dialogo(QDialog):
    #Iniciamos el constructor
    def __init__(self):
        #Iniciamos el objeto QDialog
        QDialog.__init__(self)
        #Cargo el objeto uic que hicimos con Qcreator
        uic.loadUi("tree-widget.ui", self)
        #Cuando le den click al moton llamamos al metodo getDir
        self.boton.clicked.connect(self.getDir)
        #Cuando le den double click a un elemento del tree llamamos al metodo openElement
        self.directorio.itemDoubleClicked.connect(self.openElement)


    #Metodo para obtener el directorio
    def getDir(self):
        #Limpiamos el tree, eliminando todas las filas de la busqueda anterior
        self.directorio.clear()
        #Guardamos la ruta que indique el usuario en el campo de texto
        dir = self.ruta.text()
        #Comprobamos si es un directorio
        if path.isdir(dir):
            #Recorremos sus elementos tantos carpetas como archivos
            for element in listdir(dir):
                #Nombre del elemento
                name = element
                pathinfo = dir + "/" + name
                #Obtenemos los datos del elemento
                informacion = stat(pathinfo)

                #Comprobamos si es un directorio
                if path.isdir(pathinfo):
                    #SI el elemento es un directorio entonces es una carpeta de archivo
                    type = "Carpeta de archivos"
                    size = ""
                #Si no lo buscado es un archivo
                else:
                    #Declaramos un obejto de tipo MimeTypes para saber de que tipo es el archivo
                    mime = MimeTypes()
                    #Con el meotdo mime.guess_type obtenemso el tipo de archivo
                    type = mime.guess_type(pathinfo)[0]
                    #Obtenemos el tamaño del archivo
                    size = str(informacion.st_size) + " bytes"
                #Fecha de modificacion
                date = str(time.ctime(informacion.st_mtime))

                #Creamos un vector con las filas de los elementos
                row = [name, date, type, size]
                #Agregamos la fila al arbol
                self.directorio.insertTopLevelItems(0,[QTreeWidgetItem(self.directorio, row)])

    #Metodo para abrir un elemento del tree
    def openElement(self):
        #Obtener el item seleccionado por el usuario
        item = self.directorio.currentItem()
        #Creamos la ruta accediendo al nombre del elemento (carpeta o archivo)
        elemento = self.ruta.text() + "/" + item.text(0)
        #Si es un directorio navegar a su contenido
        if path.isdir(elemento):
            #Asignamos la nueva ruta y llamamos al metodo getDIr
            self.ruta.setText(elemento)
            self.getDir()
        else: #Si es un arhcivo lo abrimos con el programa por defecto
            opener ="run-mailcap"
            subprocess.call([opener, elemento])

#Iniciamos la aplicacion
app = QApplication(sys.argv)
#Instanciamos un objeto de la Clase Dialogo
dialogo = Dialogo()
#Lo mostramos
dialogo.show()
#Ejecutamos la aplicación
app.exec_()
