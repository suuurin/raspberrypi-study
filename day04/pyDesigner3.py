# L/R 버튼 클릭시 label 표시
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class WindowClass(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.ui = uic.loadUi("design2.ui", self)
		self.ui.show()

	def slot1(self):
		self.ui.label.setText("Right btn clicked")

	def slot2(self):
		self.ui.label.setText("Left btn clicked")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	app.exec_()
