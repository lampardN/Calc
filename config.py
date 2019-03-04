from PyQt5 import QtGui

FONT = QtGui.QFont()
FONT.setFamily('Arial')
FONT.setPixelSize(20)

BUTTON_STANDARD = 'standard'
BUTTON_CLEAR = 'cear'
BUTTON_MATH = 'math'

BUTTONS = [
    ['(', ')', ['C', BUTTON_CLEAR]],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '*'],
    ['0', '.', ['=', BUTTON_MATH], '/']
]