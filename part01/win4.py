from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Hello PyQt')
        self.setWindowIcon(QIcon('../images/python.png'))
        self.setFixedWidth(250)
        self.setFixedHeight(150)

        self.setStyleSheet('background-color:green')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())