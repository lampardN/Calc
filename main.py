from PyQt5 import QtWidgets
from buttons import Button
from config import *
from input import Input


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        global primer
        self.Input = Input()

        self.hboxes = []
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.Input.label)
        mainBox.addLayout(self.Input.box)
        for row in BUTTONS:
            box = QtWidgets.QHBoxLayout()
            self.hboxes.append(box)
            for item in row:
                if isinstance(item, str):
                    box.addWidget(Button(item, self.simpleButtonPress))
                elif item[1] == BUTTON_MATH:
                    box.addWidget(Button(item[0], self.mathButtonPress))
                else:
                    box.addWidget(Button(item[0], self.clearButtonPress))
            mainBox.addLayout(box)
        self.setLayout(mainBox)

    def simpleButtonPress(self, value):
        self.Input.input.insert(value)

    def clearButtonPress(self, value):
        self.Input.input.setText('')
        self.Input.input.displayText()

    def mathButtonPress(self, value):
        print('Нажата кнопка вычисления выражения.')


if __name__ == '__main__':
    from sys import *
    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    window.setWindowTitle('Calc')
    window.show()
    exit(app.exec_())