import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def Mealy():
   win = QWidget()
   grid = QGridLayout()
	
   for i in range(0,5):
      for j in range(0,5):
         grid.addWidget(QPushButton(str(i)+str(j)),i,j)
			

if __name__ == '__main__':
   window()

