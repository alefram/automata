import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from combinacional import combinacional
from mealy import mealy
from moore import moore

class App(QWidget):
	"""docstring for App"""
	def __init__(self):
		super(App, self).__init__()
		self.setGeometry(50,50,800,500)
		self.setWindowTitle("MEPIC18F")
		layout = QGridLayout()
		self.setLayout(layout)

		#barra de menu
		comb = combinacional()
		mea = mealy()
		moor = moore()

		menubar = QTabWidget()
		menubar.addTab(mea,"automata mealy")
		menubar.addTab(moor,"automata moore")
		menubar.addTab(comb,"combinacional")
		layout.addWidget(menubar,0,0)


		

        


app = QApplication(sys.argv)
screen = App()
screen.show()
sys.exit(app.exec_())




