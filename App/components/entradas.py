import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


dato_entrada = [2,3,4,1]

class entradas(QDialog):
    def __init__(self):
        super(entradas ,self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.dato_entrada = dato_entrada      

        #tabla
        tabla = QTableWidget(1, 4)
        newitem = QTableWidgetItem()

        l_entrada = QLabel()
        l_entrada.setText("entrada")

        #boton
        ok = QPushButton('ok')

        def datas():
            for i in range(0, 4):
                newitem = tabla.item(0,i)
                if (newitem == None):
                    a = "x"
                    pass
                elif (not newitem.text() == "1" and not newitem.text() == "0"):
                    a = "x"
                    pass
                else:
                    a = newitem.text()
                    pass
                dato_entrada[i] = a
                
        def _print():
            print(dato_entrada)

        
        tabla.cellChanged.connect(datas)
        ok.clicked.connect(_print)
        
        

        #mostrar
        layout.addWidget(l_entrada,0,0)
        layout.addWidget(tabla,1,0)
      #  layout.addWidget(ok,2,0)