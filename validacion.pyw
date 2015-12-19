# -*- coding: utf-8 -*

import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic

#Creamos la calse Dialog que recibe un QDialog
class Dialogo(QDialog):
     #Iniciamos el constructor
    def __init__(self):
        #Iniciamos el objeto
        QDialog.__init__(self)
        #Cargos el objeto uic que hicimos con Qcreator
        uic.loadUi("dialogValidation.ui", self)
        #Incluimos la validacion del campo nombre cuando se escriba sobre el
        self.nombre.textChanged.connect(self.validar_nombre)
        #Incluimos la validacion del campo email cuando se escriba sobre el
        self.email.textChanged.connect(self.validar_email)
        #Incluimos el metodo validar_formulario cuando clicked en el boton
        self.boton.clicked.connect(self.validar_formulario)

    #Definimos el metodo para validar el nombre
    def validar_nombre(self):
        #guardamos el texto del campo nombre
        nombre = self.nombre.text()
        #Definir la exprecion regular y validamos el texto, con re.I ignoramos mayusculas  y minusculas
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
        #Validamos si nombre esta vacio
        if nombre == "":
            #Le cambiamos el color del campo a amarillo
            self.nombre.setStyleSheet("border-bottom: 2px solid yellow; ")
            #Retornamos false, ya que el metodo es booleano
            return False
        #Si la validacion con la expresion regular no es correcta
        elif not validar:
            #Le cambiamos el colro del campo a rojo
            self.nombre.setStyleSheet("border-bottom: 2px solid red; ")
            #Retornamos false, ya que el metodo es booleano
            return False
        #Si pasa todas las validaciones
        else:
            #Le cambiamos el color del campo a verde
            self.nombre.setStyleSheet("border-bottom: 2px solid green; ")
            #Retornamos true, ya que el metodo es booleano
            return True

    #Definimos el metodo para validar el email
    def validar_email(self):
        #guardamos el texto del campo email
        email = self.email.text()
        #Definir la exprecion regular y validamos el texto, con re.I ignoramos mayusculas y minusculas
        validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', email, re.I)
        #Validamos si nombre esta vacio
        if email == "":
            #Le cambiamos el color del campo a amarillo
            self.email.setStyleSheet("border-bottom: 2px solid yellow; ")
            #Retornamos false, ya que el metodo es booleano
            return False
        #Si la validacion con la expresion regular no es correcta
        elif not validar:
            #Le cambiamos el colro del campo a rojo
            self.email.setStyleSheet("border-bottom: 2px solid red; ")
            #Retornamos false, ya que el metodo es booleano
            return False
        #Si pasa todas las validaciones
        else:
            #Le cambiamos el colro del campo a verde
            self.email.setStyleSheet("border-bottom: 2px solid green; ")
            #Retornamos true, ya que el metodo es booleano
            return True

    #Definimos el metodo para validar el formulario
    def validar_formulario(self):

        #Validamos que los metodo validar nombre y email retornen true
        if self.validar_nombre() and self.validar_email():
            #Mostramos un mensaje
            QMessageBox.information(self, "Formulario Correcto", "Validacion Correcta", QMessageBox.Discard)

        #De lo contrario
        else:
            #Mostramos un warning
            QMessageBox.warning(self, "Formulario Incorrecto", "Validacion incorrecta", QMessageBox.Discard)

#Inciaimos la aplicacion
app = QApplication(sys.argv)
#Instanciamos un Objeto Dialogo()
dialogo = Dialogo()
#La mostramos
dialogo.show()
#Ejecutamos la aplicacion
app.exec_()




