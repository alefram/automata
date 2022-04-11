import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSvg import *
from entradas import entradas
from combEntrada import combEntrada
from combSalidaMelay import combSalidaMelay



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


        def _TablaTransicion1():
            sw = combEntrada()
            sw.setWindowTitle("combinacional de entrada")
            sw.exec_()


        def _TablaTransicion2():
            sw = combSalidaMelay()
            sw.setWindowTitle("combinacional de salida")
            sw.exec_()

        def _entradas():
            sw = entradas()
            sw.setWindowTitle("tabla de entradas")
            sw.exec_()
            pass

        def _start():
            pass

        def _output():
            

            pass

        #botones
 
        
        combTransicion1 = QPushButton('tabla de transicion 1')
        combTransicion1.clicked.connect(_TablaTransicion1)
        
        combTransicion2 = QPushButton('tabla de transicion 2')
        combTransicion2.clicked.connect(_TablaTransicion2)

        entradas = QPushButton('entrada')
        entradas.clicked.connect(_entradas)

        start = QPushButton('start')
        start.clicked.connect(_start)

        output = QPushButton('Output')
        output.clicked.connect(_output)


        # layouts
        layoutI.addWidget(entradas,0,1,)
        layoutI.addWidget(svg, 0, 2)

        layoutI.addWidget(combTransicion1, 3, 2)

        layoutI.addWidget(combTransicion2, 5, 2)
        

        layoutI.addWidget(start, 6, 4)
        layoutI.addWidget(output, 6, 5)
        
     
