import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from combinacional import combinacional
from mealy import mealy
from moore import moore


class App(QMainWindow):
	"""docstring for App"""
	def __init__(self):
		super(App, self).__init__()
		self.setGeometry(50, 50, 800, 500)
		self.setWindowTitle("MEPIC18F")
		layout = QGridLayout()
		widget = QWidget()
		widget.setLayout(layout)


		#barra de menu
		_combinacional = combinacional()
		_mealy = mealy()
		_moore = moore()

		menubar = QTabWidget()
		#menubar.addTab(_mealy, "automata mealy")
		#menubar.addTab(_moore, "automata moore")
		menubar.addTab(_combinacional, "combinacional")
		layout.addWidget(menubar, 0, 0)

		self.setCentralWidget(widget)

app = QApplication(sys.argv)
screen = App()
screen.show()
sys.exit(app.exec_())




