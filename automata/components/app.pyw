import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class App(QWidget):
   def __init__(self):
         QWidget.__init__(self)
         widget = QWidget()
         widget.setGeometry(50,50,320,500)
         widget.setWindowTitle("hola mundo")




         



app = QApplication(sys.argv)
screen = App()
screen.show()
sys.exit(app.exec_())




