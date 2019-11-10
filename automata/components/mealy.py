import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSvg import *
from tablaEntrada import tablaEntrada
from tablaSalida import tablaSalida
from tablaTransicion import tablaTransicion

def _tablaEntrada1():
    sw = tablaEntrada()
    sw.setWindowTitle("tabla de entrada 1")
    sw.exec_()

def _TablaTransicion1():
    sw = tablaTransicion()
    sw.setWindowTitle("tabla de transicion 1")
    sw.exec_()

def _tablaEntrada2():
    sw = tablaEntrada()
    sw.setWindowTitle("tabla de entrada 2")
    sw.exec_()

def _TablaTransicion2():
    sw = tablaTransicion()
    sw.setWindowTitle("tabla de transicion 2")
    sw.exec_()

def _entradas():
    pass

def _start():
    pass

def _stop():
    pass

def _output():
    pass


class mealy(QWidget):
    """docstring for mealy"""
    def __init__(self):
        super(mealy, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle("mealy")
        layoutI = QGridLayout()
        self.setLayout(layoutI)
        
        #svg
        # svg
        svg = QSvgWidget()
        svg.renderer().load("automata\components\svgs\mealy.svg")

        svg.show()

        #botones
        combEntrada1 = QPushButton('tabla de entrada 1', self)
        combEntrada1.clicked.connect(_tablaEntrada1)
        
        combTransicion1 = QPushButton('tabla de transicion 1', self)
        combTransicion1.clicked.connect(_TablaTransicion1)

        combEntrada2 = QPushButton('tabla de entrada 2', self)
        combEntrada2.clicked.connect(_tablaEntrada2)
        
        combTransicion2 = QPushButton('tabla de transicion 2', self)
        combTransicion2.clicked.connect(_TablaTransicion2)

        entradas = QPushButton('entrada', self)
        entradas.clicked.connect(_entradas)

        start = QPushButton('start')
        start.clicked.connect(_start)

        stop = QPushButton('stop')
        stop.clicked.connect(_stop)

        output = QPushButton('Output')
        output.clicked.connect(_output)


        # layouts
        layoutI.addWidget(entradas,0,1,)
        layoutI.addWidget(svg, 0, 2)
        
        layoutI.addWidget(combEntrada1, 2, 2)
        layoutI.addWidget(combTransicion1, 3, 2)
        layoutI.addWidget(combEntrada2, 4, 2)
        layoutI.addWidget(combTransicion2, 5, 2)
        

        layoutI.addWidget(start, 6, 4)
        layoutI.addWidget(stop, 6, 5)
        layoutI.addWidget(output, 6, 6)
        
     
