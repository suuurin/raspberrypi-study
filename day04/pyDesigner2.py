import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadrUiType("design2.ui")[0]

class WindowClass(QDialog, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

	def slot1(self): pass

if __name__ == "__main__":
	app = QApplocation(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec()
