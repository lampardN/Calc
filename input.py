from config import *
from PyQt5 import QtWidgets


class Input:
    def __init__(self):
        self.label = QtWidgets.QLabel('Введёное выражение: ')
        self.label.setFont(FONT)

        self.input = QtWidgets.QLineEdit()
        self.input.setFont(FONT)

        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.input)
