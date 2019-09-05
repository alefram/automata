import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def showDialog():
    # win = QWidget()
    # layout = QGridLayout()
    # win.setLayout(layout)
    pass

def showDialog2():
    # win = QWidget()
    # layout = QGridLayout()
    # win.setLayout(layout)
    pass

class mealy(QWidget):
    def __init__(self):
        super(mealy,self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        
        

        #botones
        combEntrada = QPushButton()
        combEntrada.setText('entrada')
        combEntrada.clicked.connect(showDialog)
        label2 = QLabel("Widget in Tab comb.")
        
        combSalida = QPushButton()
        combSalida.setText('salida')
        combSalida.clicked.connect(showDialog2)
        label2 = QLabel("Widget in Tab mealy")

        layout.addWidget(label2)
        layout.addWidget(combEntrada)
        layout.addWidget(combSalida)
        
        
