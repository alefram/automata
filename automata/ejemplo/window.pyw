import sys
import random
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
	"""docstring for MyWidget"""
	def __init__(self):
		super().__init__()
		
		self.hello  = ["hola que pedo", "puto"]
		self.button  = QPushButton("tocame")
		self.text  = QLabel("putooo")
		self.text.setAlignment(Qt.AlignCenter)

		self.layout  = QVBoxLayout()
		self.layout.addWidget(self.text)
		self.layout.addWidget(self.button)
		self.setLayout(self.layout)

		self.button.clicked.connect(self.magic)

	def magic(self):
		self.text.setText(random.choice(self.hello))
		pass


if __name__  == "__main__":
	app  = QApplication([])

	widget  = MyWidget()
	widget.resize(800, 600)
	widget.show()
	sys.exit(app.exec_())
	



		