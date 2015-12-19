# -*- coding: utf-8 -*

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

#import ctypes #GetSystemMetrics, obtener resolucion de la pantalla

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
	#Metodo constructor de la clase
    def __init__(self):
		#Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
		
		#Cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("mainwindow.ui", self)

        #Cambiando el titulo de la ventana
        self.setWindowTitle("Cambiando el titulo de la ventana")
        
        #Mostrar la ventana maximizada
        #self.showMaximized()
        
        #Fijar el tamaño minimo de la ventana
        self.setMinimumSize(500, 500)
        
        #Fijar el tamaño maximo de la ventana
        self.setMaximumSize(500, 500)

        #En windows

        #Mover la ventana y centrarla en el escritorio
        #resolucion = ctypes.windll.user32
        #resolucion_ancho = resolucion.GetSystemMetrics(0)
        #resolucion_alto = resolucion.GetSystemMetrics(1)

        #Lo centramos
        #left = (resolucion_ancho / 2) - (self.frameSize().width() / 2)
        #width = (resolucion_alto / 2) - (self.frameSize().height() / 2)
        #self.move(left, top)

        #left = (self.frameSize().width() )
        #width = (self.frameSize().height() )
        #self.move(left, 200)

        #En linux

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        #x = ( self.frameSize().width() / 2)
        #y = ( self.frameSize().height() / 2 )
        #self.move( qr.x() - x , qr.y() - y )
        #self.move(qr.topLeft())
        #self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        
        #Desactivar la ventana
        #self.setEnabled(False)

        #Asignar un tipo de fuente
        qfont = QFont("Arial", 12, QFont.Bold)
        self.setFont(qfont)

        #Asignar un tipo de cursor
        self.setCursor(Qt.OpenHandCursor)

        #Asignar estilos CSS
        #self.setStyleSheet("background-color: #000; color: #fff;")

        self.pushButton.setStyleSheet("background-color: #000; color: #fff;")

    #definimos el evento showEvent, cuando inicia la ventana
    def showEvent(self, event):
        self.bienvenido.setText("¡¡¡Bienvenido!!!")

    #Definimos el evento cuando cierren la ventana
    def closeEvent(self, event):
        #Mostamos un mensaje cuando se cierre la aplicacion
        resultado = QMessageBox.question(self, "Salir....", "¿Seguro que desea salir ?", 
            QMessageBox.Yes | QMessageBox.No)

        #Validamos si el usuario le dio a yes o a no
        #Si le da a yes, aceptamos el evento else lo ignoramos
        if resultado == QMessageBox.Yes:
            event.accept

        else:
            event.ignore()

    #Definimos el evento cuando muevan la ventana
    def moveEvent(self, event):

        #Obtenemos la cordenada de x
        x = str(event.pos().x())

        #Obtenemos la cordenada de y
        y = str(event.pos().y()) 

        self.posicion.setText("x: " + x + "y:" + y)



#Instancia para iniciar una aplicacion
app = QApplication(sys.argv)

#Crear un objeto de la clase
_ventana = Ventana()

#Mostra la ventana
_ventana.show()

#Ejecutar la aplicacion
app.exec_()
