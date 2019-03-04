from config import *
from PyQt5 import QtWidgets, QtCore


class Input:
    def __init__(self):
        self.label = QtWidgets.QLabel('Введёное выражение: ')
        self.label.setFont(FONT)

        self.input = QtWidgets.QLineEdit()
        self.input.setFont(FONT)
        self.input.setReadOnly(True)

        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.input)
