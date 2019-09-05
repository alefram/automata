import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class mealy(QWidget):
    def __init__(self):
        super(mealy,self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)

        label2 = QLabel("Widget in Tab mealy.")

        layout.addWidget(label2,0,0)
        
