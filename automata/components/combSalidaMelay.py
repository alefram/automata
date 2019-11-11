import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

data_out = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]

data_in = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]

class combSalidaMelay(QDialog):
    def __init__(self):
        super(combSalidaMelay ,self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.data_in = data_in
        self.data_out = data_out
            
        
        #tabla
        entrada = QTableWidget(4, 4)
        salida = QTableWidget(4, 4)
        newitem2 = QTableWidgetItem()
        newitem = QTableWidgetItem()

        label_entrada = QLabel()
        label_entrada.setText("tabla de entradas")

        label_salida = QLabel()
        label_salida.setText("tabla de salidas")

        #boton
        ok = QPushButton('ok')
        ok2 = QPushButton('ok2')

        def _matrix():
            for i in range(0, 4):
                for j in range(0, 4):
                    newitem = entrada.item(i, j)
                    if (newitem == None):
                        a = "x"
                        pass
                    elif (not newitem.text() == "1" and not newitem.text() == "0"):
                        a = "x"
                        pass
                    else:
                        a = newitem.text()
                        pass
                    data_in[i][j] = a
        
        def _matrix2():
            for i in range(0, 4):
                for j in range(0, 4):
                    newitem2 = salida.item(i, j)
                    if (newitem2 == None):
                        a = "x"
                        pass
                    elif (not newitem2.text() == "1" and not newitem2.text() == "0"):
                        a = "x"
                        pass
                    else:
                        a = newitem2.text()
                        pass
                    data_out[i][j] = a

        def _print():
            print(self.data_in)
        
        def _print2():
            print(self.data_out)

        entrada.cellChanged.connect(_matrix)
        salida.cellChanged.connect(_matrix2)
        ok.clicked.connect(_print)
        ok2.clicked.connect(_print2)

        #mostrar
        layout.addWidget(entrada, 1, 0)
        layout.addWidget(salida,1,1)
        layout.addWidget(ok,2,0)
        layout.addWidget(ok2, 2, 1)
        layout.addWidget(label_entrada, 0, 0)
        layout.addWidget(label_salida,0,1)