import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *




class tablaSalida(QDialog):
    def __init__(self):
        super(tablaSalida ,self).__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)      

        #tabla
        tabla = QTableWidget(16, 4)

        def data():
            
            pass
        
        tabla.cellChanged.connect(data)
        

        #mostrar
        layout.addWidget(tabla)