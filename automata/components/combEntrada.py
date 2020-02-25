import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

data_edoSiguiente = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]

data_entrada = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]

data_edoActual = [[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],
          [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]

class combEntrada(QDialog):
    def __init__(self):
        super(combEntrada ,self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.data_edoSiguiente = data_edoSiguiente
        self.data_edoActual = data_edoActual
        self.data_entrada = data_entrada


        #tabla
        entrada = QTableWidget(16, 4)
        salida = QTableWidget(16, 4)
        estado = QTableWidget(16, 4)

        newitem = QTableWidgetItem()

        label_entrada = QLabel()
        label_entrada.setText("tabla de entradas")j
        label_salida = QLabel()
        label_salida.setText("Estado siguiente")

        label_edo = QLabel()
        label_edo.setText("estado actual")


        #boton
        ok = QPushButton('ok')
        ok2 = QPushButton('ok2')
        ok3 = QPushButton('ok3')

        def _matrix():
    k        for i in range(0, 16):
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
                    data_entrada[i][j] = a

        def _matrix2():
            for i in range(0, 16):
                for j in range(0, 4):
                    newitem = salida.item(i, j)
                    if (newitem == None):
                        a = "x"
                        pass
                    elif (not newitem.text() == "1" and not newitem.text() == "0"):
                        a = "x"
                        pass
                    else:
                        a = newitem.text()
                        pass
                    data_edoSiguiente[i][j] = a

        def _matrix3():
            for i in range(0, 16):
                for j in range(0, 4):
                    newitem = estado.item(i, j)
                    if (newitem == None):
                        a = "x"
                        pass
                    elif (not newitem.text() == "1" and not newitem.text() == "0"):
                        a = "x"
                        pass
                    else:
                        a = newitem.text()
                        pass
                    data_edoActual[i][j] = a

        def _print():
            print(self.data_entrada)

        def _print2():
            print(self.data_edoSiguiente)

        def _print3():
            print(self.data_edoActual)

        entrada.cellChanged.connect(_matrix)
        salida.cellChanged.connect(_matrix2)
        estado.cellChanged.connect(_matrix3)
        ok.clicked.connect(_print)
        ok2.clicked.connect(_print2)
        ok3.clicked.connect(_print3)

        #mostrar
        layout.addWidget(entrada, 1, 0)
        layout.addWidget(salida, 1, 1)
        layout.addWidget(estado,1,2)
        layout.addWidget(ok,2,0)
        layout.addWidget(ok2, 2, 1)
        layout.addWidget(ok3,2,2)
        layout.addWidget(label_entrada, 0, 0)
        layout.addWidget(label_salida, 0, 1)
        layout.addWidget(label_edo,0,2)
