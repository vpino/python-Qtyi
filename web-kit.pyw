# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5 import uic

#Creamos la clase Navegador la cual recibe un QMainWindow
class Navegador(QMainWindow):
    #Iniciamos el constructor
    def __init__(self):
        #Iniciamos el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargos el objeto uic que hicimos con Qcreator
        uic.loadUi("webkit.ui", self)
        #definimos una url por defecto
        default_url = "http://gitlab.canaima.softwarelibre.gob.ve"
        #Ir a la url por defecto
        self.navegador.setUrl(QUrl(default_url))
        #Agregamos al buscador la url por defecto
        self.url.setText(default_url)
        #Desactivamos el botón back hasta que no haya historial
        self.btn_back.setEnabled(False)
        #Cuando le den click al botón back, retrocedemos a la pag anterior
        self.btn_back.clicked.connect(self.navegador.back)
        #Cuando pulsemos la tecla enter llamamos al metodo navegar
        self.url.returnPressed.connect(self.navegar)
        #Cuando cambie la url del navegador llamamos al metodo url_change
        self.navegador.urlChanged.connect(self.url_changed)

    #Creamos un metodo que nos permita ir a la url digitada
    def navegar(self):
        #Obtenemos la url indicada por el usuario
        url = QUrl(self.url.text())
        #Se la pasamos al navegador
        self.navegador.setUrl(url)

    #Metodo para detectar el cambio de la url en la barra de navegacion
    def url_changed(self):
        #Creamos un objeto de la página para poder acceder al historial
        page = self.navegador.page()
        history = page.history()
        #Si hay historial, activamso el botón back
        if history.canGoBack():
            #Activamos el botón
            self.btn_back.setEnabled(True)
        else:
            #De lo contrario lo desactivamos
            self.btn_back.setEnabled(False)

        #Agregamos el cambio de url al campo de busqueda
        #Obtenemos la url que tiene el navegador
        url = self.navegador.url()
        #Se la paasamos al campo de busqueda
        self.url.setText(url.toString())


#Inciamos la aplicación
app = QApplication(sys.argv)
#Instanciamos un objeto de la Clase Navegador
navegador = Navegador()
#Lo mostramos
navegador.show()
#Ejecutamos la aplicación
app.exec_()


