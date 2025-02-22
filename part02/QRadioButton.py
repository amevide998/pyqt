from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QRadioButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('PyQt6 QRadioButton')
        self.setWindowIcon(QIcon('../images/python.png'))

        self.create_radio()

    def create_radio(self):
        self.label = QLabel("")
        self.label.setFont(QFont('Arial', 40))

        hbox = QHBoxLayout()
        rad1 = QRadioButton("Python")
        rad1.setIcon(QIcon('../images/py.png'))
        rad1.setIconSize(QSize(40, 40))
        rad1.setFont(QFont('Arial', 20))
        rad1.toggled.connect(self.radio_selected)
        rad1.setChecked(True)

        rad2 = QRadioButton("Java")
        rad2.setIcon(QIcon('../images/java.png'))
        rad2.setIconSize(QSize(40, 40))
        rad2.setFont(QFont('Arial', 20))
        rad2.toggled.connect(self.radio_selected)

        rad3 = QRadioButton("Javascript")
        rad3.setIcon(QIcon('../images/javascript.png'))
        rad3.setIconSize(QSize(40, 40))
        rad3.setFont(QFont('Arial', 20))
        rad3.toggled.connect(self.radio_selected)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        hbox.addWidget(rad1)
        hbox.addWidget(rad2)
        hbox.addWidget(rad3)

        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText("You have selected : {} ".format(radio_btn.text()))



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())