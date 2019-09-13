import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *




def tablaEntrada():
    sw = QDialog()
    sw.setWindowTitle("tabla de entrada")
    sw.exec_()



def tablaSalida():
    sw = QDialog()
    sw.setWindowTitle("tabla de salida")
    sw.exec_()
    

class mealy(QWidget):
    """docstring for mealy"""
    def __init__(self):
        super(mealy, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle("mealy")
        layout = QGridLayout()
        self.setLayout(layout)
        
        #svg

  
        

        #botones
        combEntrada = QPushButton('entrada', self)
        combEntrada.clicked.connect(tablaEntrada)
        
        combSalida = QPushButton('salida', self)
        combSalida.clicked.connect(tablaSalida)


        #adding widgets
        layout.addWidget(combEntrada,1,1)
        layout.addWidget(combSalida,1,2)
        #layout.addWidget(foto, )

    
        
     
