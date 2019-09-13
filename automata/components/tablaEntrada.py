import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class tablaEntrada(QDialog):
    def __init__(self):
        super(tablaEntrada ,self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)      

        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")

        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        