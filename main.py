from PyQt5 import QtWidgets
from buttons import Buttons
from config import *
from input import Input

class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.Input = Input()
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.Input.label)
        self.setLayout(mainBox)


if __name__ == '__main__':
    from sys import *
    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    window.resize(200,300)
    window.setWindowTitle('Calc')
    window.show()
    exit(app.exec_())