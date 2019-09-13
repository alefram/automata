import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



def tablaEntrada():
    sw = QDialog()
    sw.setWindowTitle("tabla de entrada")
    sw.exec_()

def TablaSalida():
    sw = QDialog()
    sw.setWindowTitle("tabla de salida")
    sw.exec_()


class moore(QWidget):
    """docstring for moore"""
    def __init__(self):
        super(moore, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle("moore")
        layout = QGridLayout()
        self.setLayout(layout)


        #botones
        combEntrada = QPushButton('entrada', self)
        combEntrada.clicked.connect(tablaEntrada)
        
        combSalida = QPushButton('salida', self)
        combSalida.clicked.connect(TablaSalida)

        layout.addWidget(combEntrada,1,1)
        layout.addWidget(combSalida,1,2)


        
