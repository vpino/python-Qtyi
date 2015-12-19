# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon

#Creamos la clase Window que recibe un QMainWindow
class Window(QMainWindow):
    #Inciamos el constructor
    def __init__(self):
        #Iniciamos el objeto QDialog
        QMainWindow.__init__(self)
        #Tamaño inicial de la ventana 800x500
        self.resize(800, 500)
        #Barra de estado
        self.statusBar().showMessage("Bienvenid@")
        #Objeto menuBar
        menu = self.menuBar()
        #Menu padre
        menu_archivo = menu.addMenu("&Archivo")
        #Otro menu padre
        menu_editar = menu.addMenu("&Editar")

        #Agregar un elemento action al menu_archivo
        #creamos la accion, recibe un icono, el texto, el objeto
        menu_archivo_abrir = QAction(QIcon(), "&Abrir", self)
        #Agregamos un atajo
        menu_archivo_abrir.setShortcut("Ctrl+o")
        #Mostramos un texto al submenu
        menu_archivo_abrir.setStatusTip("Abrir")
        #Incluimos una accion cuando le den click a abrir (lanzador de la accion)
        # En este caso llamamos al metodo menuArchivoAbrir
        menu_archivo_abrir.triggered.connect(self.menuArchivoAbrir)
        #Añadimos el nuevo elemento que acabamos de crear
        menu_archivo.addAction(menu_archivo_abrir)

        #Agregar un elemento submenu al menu_archivo
        #creamos la accion, recibe un icono, el texto, el objeto
        menu_archivo_cerrar = QAction(QIcon(), "&Cerrar", self)
        #Agregamos un atajo
        menu_archivo_cerrar.setShortcut("Ctrl+c")
        #Mostramos un texto al submenu
        menu_archivo_cerrar.setStatusTip("Cerrar")
        #Incluimos una accion cuando le den click a abrir (lanzador de la accion)
        # En este caso llamamos al metodo menuArchivoCerar
        menu_archivo_cerrar.triggered.connect(self.menuArchivoCerar)
        #Añadimos el nuevo elemento que acabamos de crear
        menu_archivo.addAction(menu_archivo_cerrar)

        #Agregar un submenu al menu Editar
        menu_editar_opciones = menu_editar.addMenu("&Opciones")
        #creamos la accion, recibe un icono, el texto, el objeto
        menu_editar_opciones_buscar = QAction(QIcon(), "&Buscar", self)
        #Agregamos un atajo
        menu_editar_opciones_buscar.setShortcut("Ctrl+f")
        #Añadimos el texto al submenu
        menu_editar_opciones_buscar.setStatusTip("Buscar")
        #Incluimos una accion cuando le den click a abrir (lanzador de la accion)
        # En este caso llamamos al metodo menuArchivoCerar
        menu_editar_opciones_buscar.triggered.connect(self.menuEditarOpcionesBuscar)
        #Le añadimos la acción
        menu_editar_opciones.addAction(menu_editar_opciones_buscar)

    #Metodo que solo muestra un msj
    def menuArchivoAbrir(self):
        QMessageBox.information(self, "Abrir", "Acción Abrir", QMessageBox.Discard)

    #Metodo que solo muestra un msj
    def menuArchivoCerar(self):
        QMessageBox.information(self, "Cerrar", "Acción Cerrar", QMessageBox.Discard)

    def menuEditarOpcionesBuscar(self):
        QMessageBox.information(self, "Buscar", "Acción Buscar", QMessageBox.Discard)

#Inciamos la aplicación
app = QApplication(sys.argv)
#Instanciamos un Objeto de la Clase Window
window = Window()
#Lo mostramos
window.show()
#Ejecutamos la aplicación
app.exec_()
