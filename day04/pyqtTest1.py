import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):	# 상속 받음
	def __init__(self):
		super().__init__()	# 부모 생성자 호출
		self.initUI()			# 자기 객체 initUI() 객체 호출

	def initUI(self):
		self.setWindowTitle("My First Application")
		self.move(300, 300)		# 위젯 위치
		self.resize(400, 200)	# 위젯 크기
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())
