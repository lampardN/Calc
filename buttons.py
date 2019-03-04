from PyQt5 import QtWidgets
from config import *


class Buttons(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__()
        self.font(FONT)
