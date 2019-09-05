import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class combinacional(QWidget):
    def __init__(self):
        super(combinacional,self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)

        label2 = QLabel("Widget in Tab comb.")

        layout.addWidget(label2,0,0)
        
