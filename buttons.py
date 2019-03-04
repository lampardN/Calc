from PyQt5 import QtWidgets
from config import *


class Button(QtWidgets.QPushButton):
    def __init__(self, value, trigger):
        super().__init__()
        self.vbox = QtWidgets.QVBoxLayout()
        self.setFont(FONT)
        self.setText(value)
        self.value = value
        self.trigger = trigger

        self.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.trigger(self.value)