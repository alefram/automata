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
        layout = QGridLayout()
        self.setLayout(layout)      


        #botones
        combEntrada = QPushButton('entrada')
        combEntrada.clicked.connect(_tablaEntrada)
 
        combSalida = QPushButton('salida', self)
        combSalida.clicked.connect(_tablaSalida)

        
        pixmap1 = QPixmap("graficos.svg")
        label = QLabel()
        label.setPixmap(pixmap1)
        label.resize(pixmap1.width(),pixmap1.height())

        layout.addWidget(combEntrada,1,1)
        layout.addWidget(combSalida,1,2)
        # layout.addWidget(label,3,7)
        
