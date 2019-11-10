import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


data = [2,3,4,1]

class entradas(QDialog):
    def __init__(self):
        super(entradas ,self).__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.data = data      

        #tabla
        tabla = QTableWidget(1, 4)
        newitem = QTableWidgetItem()

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
                data[i] = a
                
        def _print():
            print(data)

        #boton
        ok = QPushButton('ok')
        
        tabla.cellChanged.connect(datas)
        ok.clicked.connect(_print)
        
        

        #mostrar
        layout.addWidget(tabla)
        layout.addWidget(ok)