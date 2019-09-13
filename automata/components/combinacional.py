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

class combinacional(QWidget):
    def __init__(self):
        super(combinacional ,self).__init__()
        layoutP = QVBoxLayout()
        self.setLayout(layoutP)      


        #botones
        combEntrada = QPushButton('entrada')
        combEntrada.clicked.connect(_tablaEntrada)
 
        combSalida = QPushButton('salida')
        combSalida.clicked.connect(_tablaSalida)

        # svg
        pixmap1 = QPixmap("./svgs/combinacional.svg")
        label = QLabel()
        label.setPixmap(pixmap1)
        
        # layouts

        layoutI = QGridLayout()
        layoutI.addWidget(combEntrada,1,1)
        layoutI.addWidget(combSalida,1,2)
        
        layoutP.addWidget(label)
        layoutP.addLayout(layoutI)
        
