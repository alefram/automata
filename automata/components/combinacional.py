import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tablaEntrada import tablaEntrada
from tablaSalida import tablaSalida
from tablaTransicion import tablaTransicion
from entradas import entradas
from serial import Serial

pinguino = Serial("COM5", timeout=0.1, baudrate=9600)
pinguino.write(b"PinMode(7,OUTPUT)")
pinguino.write(b"PinMode(6,OUTPUT)")
pinguino.write(b"PinMode(5,OUTPUT)")
pinguino.write(b"PinMode(4,OUTPUT)")



data = [[1, 2, 3, 4],
		[2, 3, 2, 4],
		[2, 3, 4, 5],
		[2, 2, 2, 2]]


def _tablaEntrada():
    sw = tablaEntrada()
    sw.setWindowTitle("tabla de entrada")
    sw.exec_()

def _tablaTransicion():
    sw = tablaTransicion()
    sw.setWindowTitle("tabla de transicion")
    sw.exec_()

def _stop():
    s = entradas()
    a = tablaEntrada()
    sw = tablaTransicion()
    cont = 0
    for i in range(0, 4):
        if s.data == a.data[i]:
            break
            pass
        else:
            cont = cont + 1
            pass
        pass
    pass

    for j in range(0, 4):
        if j == 0:
            if sw.data[cont][j] == "1":
                pinguino.write(b"digitalWrite(4,HIGH)")
                pass
            else:
                pinguino.write(b"digitalWrite(4,LOW)")
                pass
        if j == 1:
            if sw.data[cont][j] == "1":
                pinguino.write(b"digitalWrite(5,HIGH)")
                pass
            else:
                pinguino.write(b"digitalWrite(5,LOW)")
                pass
            pass
        if j == 2:
            if sw.data[cont][j] == "1":
                pinguino.write(b"digitalWrite(6,HIGH)")
                pass
            else:
                pinguino.write(b"digitalWrite(6,LOW)")
                pass
            pass
        if j == 3:
            if sw.data[cont][j] == "1":
                pinguino.write(b"digitalWrite(7,HIGH)")
                pass
            else:
                pinguino.write(b"digitalWrite(7,LOW)")
                pass


def _start():
    stop2  = 1
    sw = tablaTransicion()
    print(sw.data)

    while stop2 <= 4:
        for i in range(0, 4):
            for z in range(0,30000000):
                pass
            for j in range(0, 4):
                if j == 0:
                    if sw.data[i][j] == "1":
                        pinguino.write(b"digitalWrite(4,HIGH)")
                        pass
                    else:
                        pinguino.write(b"digitalWrite(4,LOW)")
                        pass
                if j == 1:
                    if sw.data[i][j] == "1":
                        pinguino.write(b"digitalWrite(5,HIGH)")
                        pass
                    else:
                        pinguino.write(b"digitalWrite(5,LOW)")
                        pass
                    pass
                if j == 2:
                    if sw.data[i][j] == "1":
                        pinguino.write(b"digitalWrite(6,HIGH)")
                        pass
                    else:
                        pinguino.write(b"digitalWrite(6,LOW)")
                        pass
                    pass
                if j == 3:
                    if sw.data[i][j] == "1":
                        pinguino.write(b"digitalWrite(7,HIGH)")
                        pass
                    else:
                        pinguino.write(b"digitalWrite(7,LOW)")
                        pass
        
        stop2 = stop2 + 1

def _entradas():
    en = entradas()
    en.setWindowTitle('entradas')
    en.exec_()

    pass

    
    
class combinacional(QWidget):
    def __init__(self):
        super(combinacional, self).__init__()
        layoutI = QGridLayout()
        self.setLayout(layoutI)      

        #botones
        combEntrada = QPushButton('entradas')
        combEntrada.clicked.connect(_tablaEntrada)
 
        combTransicion = QPushButton('transición')
        combTransicion.clicked.connect(_tablaTransicion)
        
        start = QPushButton('start')
        start.clicked.connect(_start)

        stop = QPushButton('stop')
        stop.clicked.connect(_stop)

        entradas = QPushButton('entradas1')
        entradas.clicked.connect(_entradas)



        # svg
        pixmap1 = QPixmap("./svgs/combinacional.svg")
        label = QLabel()
        label.setPixmap(pixmap1)
        
        # layouts
        layoutI.addWidget(label,0,1)
        layoutI.addWidget(combEntrada,1,1)
        layoutI.addWidget(combTransicion, 1, 2)
        layoutI.addWidget(start, 1, 3)
        layoutI.addWidget(stop, 1, 4)
        layoutI.addWidget(entradas,1,5)
        
        
