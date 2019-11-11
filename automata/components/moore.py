import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSvg import *
from entradas import entradas
from combEntrada import combEntrada
from combSalida import combSalida


cont = 0

def _TablaTransicion1():
    sw = combEntrada()
    sw.setWindowTitle("combinacional de entrada")
    sw.exec_()


def _TablaTransicion2():
    sw = combSalida()
    sw.setWindowTitle("combinacional de salida")
    sw.exec_()

def _entradas():
    sw = entradas()
    sw.setWindowTitle('entradas')
    sw.exec_()
    pass

def _start():
    pass


def _output():
    entrada = entradas()
    comb_entrada = combEntrada()
    comb_salida = combSalida()
    aux = comb_salida.data_in[0]
    ent = 0
    actual = 0
    sal = 0

    for x in range(0, 16):
        if aux == comb_entrada.data_edoActual[x]:
            break
            pass
        else:
            actual = actual + 1
            pass
        pass

    for i in range(0,16):
        if entrada.dato_entrada == comb_entrada.data_entrada[i]:
            break
            pass
        else:
            ent = ent + 1
            pass
        pass


    aux = comb_entrada.data_edoSiguiente[ent]

    for z in range(0, 16):
        if aux == comb_salida.data_in:
            break
            pass
        else:
            sal = sal + 1
            pass
        pass

    for j in range(0, 4):
        if j == 0:
            if comb_salida.data_out[sal][j] == "1":
                pinguino.write(b"digitalWrite(4,HIGH)")
                pass
            else:
                pinguino.write(b"digitalWrite(4,LOW)")
                pass
        if j == 1:
            if comb_salida.data_out[sal][j] == "1":
                pinguino.write(b"digitalWrite(5,HIGH)")
                pass
            else:
                pinguino.write(b"digitalWrite(5,LOW)")
                pass
            pass
        if j == 2:
            if comb_salida.data_out[sal][j] == "1":
                pinguino.write(b"digitalWrite(6,HIGH)")
                pass
            else:
                pinguino.write(b"digitalWrite(6,LOW)")
                pass
            pass
        if j == 3:
            if comb_salida.data_out[sal][j] == "1":
                pinguino.write(b"digitalWrite(7,HIGH)")
                pass
            else:
                pinguino.write(b"digitalWrite(7,LOW)")
                pass
    pass


class moore(QWidget):
    """docstring for moore"""
    def __init__(self):
        super(moore, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle("moore")
        layoutI = QGridLayout()
        self.setLayout(layoutI)



        # svg
        svg = QSvgWidget()
        svg.renderer().load("automata\components\svgs\moore.svg")
        svg.show()


        #botones
        combTransicion1 = QPushButton('Combinacional de entrada')
        combTransicion1.clicked.connect(_TablaTransicion1)
     
        combTransicion2 = QPushButton('Combinacional de salida')
        combTransicion2.clicked.connect(_TablaTransicion2)

        entradas = QPushButton('entrada')
        entradas.clicked.connect(_entradas)

        start = QPushButton('start')
        start.clicked.connect(_start)

        output = QPushButton('Output')
        output.clicked.connect(_output)




        # layouts
        layoutI.addWidget(entradas,0,1)
        layoutI.addWidget(svg, 0, 2)
        
        layoutI.addWidget(combTransicion1, 3, 2)
        layoutI.addWidget(combTransicion2, 4, 2)
        
        layoutI.addWidget(start, 6,4)
        layoutI.addWidget(output, 6, 6)
        
        
