import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tablaEntrada import tablaEntrada
from tablaSalida import tablaSalida

def _tablaEntrada():
    sw = tablaEntrada()
    sw.setWindowTitle("tabla de entrada")
    sw.exec_()

def _tablaSalida():
    sw = tablaSalida()
    sw.setWindowTitle("tabla de salida")
    sw.exec_()
    

class mealy(QWidget):
    """docstring for mealy"""
    def __init__(self):
        super(mealy, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle("mealy")
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        #svg
        pixmap = QPixmap("svgs/mealy.svg")
        svg = QLabel()
        svg.setPixmap(pixmap)


        #botones
        combEntrada = QPushButton('entrada', self)
        combEntrada.clicked.connect(_tablaEntrada)
        
        combSalida = QPushButton('salida', self)
        combSalida.clicked.connect(_tablaSalida)


        #adding widgets

        layoutI = QGridLayout()
        layoutI.addWidget(combEntrada,1,1)
        layoutI.addWidget(combSalida,1,2)

        layout.addWidget(svg)
        layout.addLayout(layoutI)
    
        
     
