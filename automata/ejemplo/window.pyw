import sys
import random
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from serial import Serial

pinguino = Serial("COM4", timeout=0.1, baudrate=9600)
pinguino.write(b"pinMode(7,OUTPUT)")

data = [[1, 2, 3, 4],
		[2, 3, 2, 4],
		[2, 3, 4, 5],
		[2, 2, 2, 2]]
		
	
def button1_clicked():
	pinguino.write(b"digitalWrite(7,HIGH)")
	pinguino.write(b"delay(1000)")
	pinguino.write(b"digitalWrite(7,LOW)")
	print(data)


class ClassName(QWidget):
	def __init__(self):
		super().__init__()
		layout = QGridLayout()
		self.setLayout(layout)

		table = QTableWidget(4,4)
		newitem = QTableWidgetItem()

		def matrix():
			for i in range(0, 4):
				for j in range(0, 4):
					newitem = table.item(i, j)
					if newitem == None:
						a = "x"
						pass
					else:
						a = newitem.text()
						pass
					data[i][j] = a

		
			
			
		table.cellChanged.connect(matrix)
	


		boton = QPushButton('holamundo')
		boton.clicked.connect(button1_clicked)
		layout.addWidget(boton, 1, 1)
		layout.addWidget(table, 2, 1)
	
		
		   
		
if __name__  == "__main__":
	app  = QApplication([])

	widget  = ClassName()
	widget.resize(800, 600)
	widget.show()
	sys.exit(app.exec_())
	



		