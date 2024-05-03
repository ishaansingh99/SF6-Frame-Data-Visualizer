import sys
import random
import pandas as pd
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui, QtSql

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.frame_data = pd.read_csv("frames.csv")

        self.chars = pd.unique(self.frame_data["Character"])

        self.buttons = []
        
        for char in self.chars:    
            self.buttons.append(QtWidgets.QPushButton(char))
        #self.text = QtWidgets.QLabel("Hello World",
                                     #alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        #self.layout.addWidget(self.text)
        for button in self.buttons:
            self.layout.addWidget(button)

        #self.button.clicked.connect(self.magic)

    # @QtCore.Slot()
    # def magic(self):
    #     self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = QtWidgets.QStackedWidget()
    widget.addWidget(MyWidget())
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec())