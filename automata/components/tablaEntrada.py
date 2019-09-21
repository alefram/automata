import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class tablaEntrada(QDialog):
    def __init__(self):
        super(tablaEntrada ,self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)      

        #tabla
        tabla =   QTableWidget()
        tabla.setRowCount(8)
        tabla.setColumnCount(8)
        

        #mostrar
        layout.addWidget(tabla)
        