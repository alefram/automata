import sys
import random
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from serial import Serial

pinguino = Serial("COM4", timeout=0.1, baudrate=9600)
pinguino.write(b"pinMode(7,OUTPUT)")



	
def button1_clicked():
	pinguino.write(b"digitalWrite(7,HIGH)")
	pinguino.write(b"delay(1000)")
	pinguino.write(b"digitalWrite(7,LOW)")

class ClassName(QWidget):
	def __init__(self):
		super().__init__()
		layout = QGridLayout()
		self.setLayout(layout)

		

		boton = QPushButton('holamundo')
		boton.clicked.connect(button1_clicked)
		layout.addWidget(boton,1,1)
   		
	
		
		   
		
if __name__  == "__main__":
	app  = QApplication([])

	widget  = ClassName()
	widget.resize(800, 600)
	widget.show()
	sys.exit(app.exec_())
	



		