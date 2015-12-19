# -*- coding: utf-8 -*

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel

#Clase para crear un cuadro de dialogo
class Dialogo(QDialog):

	#Metodo constructor
	def __init__(self):

		#Iniciamos el objeto
		QDialog.__init__(self)

		#Le damos la dimenciones al cuadro del dialogo
		self.resize(300, 300)

		#Le damos un titulo
		self.setWindowTitle("Cuadro de diálogo")

		#Le creamos una etiqueta
		self.etiqueta = QLabel(self)

	#Hacemos la clase que va a ser la ventana principal
class Ventana(QMainWindow):

	#Creamos el metodo constructor
	def __init__(self):

		#Iniciamos el objeto
		QMainWindow.__init__(self)

		#Le definimos el tamaño
		self.resize(600,600)

		#Definimos el titutlo
		self.setWindowTitle("Ventana principal")

		#Le agregamos un button
		self.boton = QPushButton(self)

		#Le definimos un texto al boton
		self.boton.setText("Abrir cuadro de diálogo")

		#Le definimos un tamaño al boton
		self.boton.resize(200, 30)

		#Creamos un objeto de la clase dialogo
		self.dialogo = Dialogo()

		#Cuando se haga click sobre el boton mando a ejecutar la funcion abrir dialogo
		self.boton.clicked.connect(self.abrirDialogo) 


	#Creamos una funcion que cuando le den click al boton abre el boton dialogo
	def abrirDialogo(self):

		#Le cambiamos el texto al label
		self.dialogo.etiqueta.setText("Diálogo abierto desde la ventana principal")

		#Ejecutamos el cuadro de dialogo
		self.dialogo.exec_()
 

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()

