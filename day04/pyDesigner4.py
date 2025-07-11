# 버튼 클릭시 LED ON/OFF
import sys
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import *
from PyQt5 import uic

LED_PINS = [14, 15, 18]

class WindowClass(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = uic.loadUi("design3.ui", self)
		self.setup_gpio()

		self.ui.on_button.clicked.connect(self.slot1)
		self.ui.off_button.clicked.connect(self.slot2)

		self.show()

	def setup_gpio(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(LED_PINS, GPIO.OUT, initial=GPIO.HIGH)
		self.ui.label.setText("LED ON/OFF")

	def slot1(self):
		GPIO.output(LED_PINS, GPIO.LOW)
		self.ui.label.setText("LED ON")

	def slot2(self):
		GPIO.output(LED_PINS, GPIO.HIGH)
		self.ui.label.setText("LED OFF")

	def closeEvent(self, event):
		GPIO.cleanup()
		event.accept()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	sys.exit(app.exec_())
