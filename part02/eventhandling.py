from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQt6 Event Handling')
        self.setWindowIcon(QIcon('../images/python.png'))

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("change Text")
        self.label = QLabel("Default Text")
        hbox.addWidget(btn)

        btn.clicked.connect(self.clicked_btn)

        hbox.addWidget(self.label)
        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText("Another Text")
        self.label.setFont(QFont('Arial', 10))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())