# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5 import uic

class Navegador(QMainWindow):
 def __init__(self):
  QMainWindow.__init__(self)
  uic.loadUi("tab-widget.ui", self)
  self.pages = [] #array donde se guardará cada página objeto
  self.index = 0 #Al crear o eliminar tabs incrementar o disminuir el index
  self.add_tab() #Crear un tab por defecto

  #Agregar un nuevo tab con página
  self.btn_mas.clicked.connect(self.add_tab)
  #Eliminar un tab
  self.btn_menos.clicked.connect(self.remove_tab)
  #Cargar información de la página activa al terminar de cargarla
  self.pages[self.tabWidget.currentIndex()].loadFinished.connect(self.getInfo)
  #Actualizar información de la página del tab activo
  self.tabWidget.currentChanged.connect(self.current_changed)
  #Buscar la url indicada por el usuario
  self.url.returnPressed.connect(self.search)


 #Agregar un nuevo tab con página
 def add_tab(self):
  #Comprobar el número de páginas/tabs e incrementar en 1 para el index del nuevo elemento
  if len(self.pages) > 0:
   for i in range(len(self.pages)):
    self.index = i + 1
  #Crear objeto página
  pagina = QWebView()
  #Agregar objeto página al array pages
  self.pages.append(pagina)
  #Cargar la url por defecto
  self.pages[self.index].load(QUrl("http://www.google.com"))
  #Agregar el objeto página a un nuevo tab
  self.tabWidget.addTab(self.pages[self.index], "")
  #Poner el foco en el nuevo tab
  self.tabWidget.setCurrentIndex(self.index)

 def getInfo(self):
  #Index del tab que tiene el foco
  index = self.tabWidget.currentIndex()
  #Título de la página web
  title = self.pages[index].title()
  #Agregar título al tab
  self.tabWidget.setTabText(index, title)
  #Agregar título a la ventana
  self.setWindowTitle(title)
  #Actualizar la url del buscador
  url = self.pages[index].url()
  self.url.setText(url.toString())


 def current_changed(self):
  #Index del tab que tiene el foco
  index = self.tabWidget.currentIndex()
  #Actualizar la información de la página si un tab obtiene el foco
  self.pages[index].loadFinished.connect(self.getInfo)
  #Título de la página web
  title = self.pages[index].title()
  #Agregar título al tab
  self.tabWidget.setTabText(index, title)
  #Agregar título a la ventana
  self.setWindowTitle(title)
  #Actualizar la url del buscador
  url = self.pages[index].url()
  self.url.setText(url.toString())

 def search(self):
  #Url del campo de búsqueda
  url = QUrl(self.url.text())
  #Obtener el index del tab que tiene el foco
  index = self.tabWidget.currentIndex()
  #Navegar a la url
  self.pages[index].setUrl(url)

 def remove_tab(self):
  #Obtener el index del tab que tiene el foco
  index = self.tabWidget.currentIndex()
  #Eliminar el tab
  self.tabWidget.removeTab(index)
  #Eliminar la página objeto del array pages
  self.pages.pop(index)
  #Actualizar el valor del atributo index
  if self.index > 0: self.index = self.index - 1
  #Actualizar la información del tab que obtendrá el foco tras la eliminación del seleccionado
  self.current_changed()

app = QApplication(sys.argv)
navegador = Navegador()
navegador.show()
app.exec_()