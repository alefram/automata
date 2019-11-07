import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

data = [[1, 2, 3, 4],
		[2, 3, 2, 4],
		[2, 3, 4, 5],
		[2, 2, 2, 2]]

class tablaTransicion(QDialog):
    def __init__(self):
        super(tablaTransicion ,self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.data = data
            
        
        #tabla
        table = QTableWidget(4, 4)
        newitem = QTableWidgetItem()

        #boton
        ok = QPushButton('ok')

        def _matrix():
            for i in range(0, 4):
                for j in range(0, 4):
                    newitem = table.item(i, j)
                    if (newitem == None):
                        a = "x"
                        pass
                    elif (not newitem.text() == "1" and not newitem.text() == "0"):
                        a = "x"
                        pass
                    else:
                        a = newitem.text()
                        pass
                    data[i][j] = a

        def _print():
            print(self.data)

        table.cellChanged.connect(_matrix)
        ok.clicked.connect(_print)

        #mostrar
        layout.addWidget(table)
        layout.addWidget(ok)