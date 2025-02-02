from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQt6 QCheckBox')
        self.setWindowIcon(QIcon('../images/python.png'))

        vbox = QVBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QIcon('../images/py.png'))
        self.check1.stateChanged.connect(self.item_selected)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QIcon('../images/java.png'))
        self.check2.stateChanged.connect(self.item_selected)

        self.check3 = QCheckBox("Javascript")
        self.check3.setIcon(QIcon('../images/javascript.png'))
        self.check3.stateChanged.connect(self.item_selected)

        self.label = QLabel(self)

        vbox.addWidget(self.check1)
        vbox.addWidget(self.check2)
        vbox.addWidget(self.check3)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def item_selected(self):
        value = []

        if self.check1.isChecked():
            value.append(self.check1.text())

        if self.check2.isChecked():
            value.append(self.check2.text())

        if self.check3.isChecked():
            value.append(self.check3.text())

        self.label.setText(",".join(value))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())