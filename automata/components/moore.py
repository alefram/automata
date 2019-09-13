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
        layout = QVBoxLayout()
        self.setLayout(layout)



        # svg
        pixmap = QPixmap("./svgs/moore.svg")
        svg = QLabel()
        svg.setPixmap(pixmap)


        #botones
        combEntrada = QPushButton('entrada', self)
        combEntrada.clicked.connect(tablaEntrada)
        
        combSalida = QPushButton('salida', self)
        combSalida.clicked.connect(TablaSalida)


        # layouts
        layoutI = QGridLayout()

        layoutI.addWidget(combEntrada,1,1)
        layoutI.addWidget(combSalida,1,2)

        layout.addWidget(svg)
        layout.addLayout(layoutI)
        
