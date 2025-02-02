from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQt6 QPushButton')
        self.setWindowIcon(QIcon('../images/python.png'))

        self.create_button()

    def create_button(self):
        btn = QPushButton("Click", self)
        btn.setGeometry(100,100,100,100)
        btn.setIcon(QIcon('../images/python.png'))
        btn.setFont(QFont('Times', 10, QFont.Weight.ExtraBold))

        # pop up menu
        menu = QMenu()
        menu.setFont(QFont('Times', 10, QFont.Weight.ExtraBold))
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())