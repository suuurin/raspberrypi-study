# event
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("PyQt Button Test")
		self.move(300, 300)
		self.resize(400, 200)

		button = QPushButton("click", self)
		button.move(20, 20)

		button.clicked.connect(self.button_clicked)
