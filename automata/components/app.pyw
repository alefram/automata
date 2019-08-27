import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class App(QWidget):
	"""docstring for App"""
	def __init__(self):
		super(App, self).__init__()
		self.setGeometry(50,50,800,500)
		self.setWindowTitle("MEPIC18F")
		layout = QGridLayout()
		self.setLayout(layout)

		#barra de menu
		label1 = QLabel("Widget in Tab 1.")
		label2 = QLabel("Widget in Tab 2.")
		label3 = QLabel("widget in tab 3")
		menubar = QTabWidget()
		menubar.addTab(label1,"automata mealy")
		menubar.addTab(label2,"automata moore")
		menubar.addTab(label3,"combinacional")
		layout.addWidget(menubar,0,0)

		

        


app = QApplication(sys.argv)
screen = App()
screen.show()
sys.exit(app.exec_())




