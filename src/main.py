import sys
import re
import pandas as pd
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui, QtSql

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.frame_data = pd.read_csv("data/frames.csv")

        self.chars = pd.unique(self.frame_data["Character"])

        self.buttons = []
        
        for char in self.chars:    
            self.buttons.append(QtWidgets.QPushButton(char))
        
        self.layout = QtWidgets.QVBoxLayout(self)
        for button in self.buttons:
            _name = button.text().lower()
            _name = re.sub('[\\W]+','',_name)
            button.setObjectName(_name+"Main")
            self.layout.addWidget(button)
            button.clicked.connect(self.goToScreen)

    def goToScreen(self):
        # print(self.sender().text())
        ind = np.where(self.chars == self.sender().text())[0][0] + 1
        widget.setCurrentIndex(ind)
        
    def initCharScreens(self):
        for button in self.buttons:
            widget.addWidget(CharWindow(button.text()))

class CharWindow(QtWidgets.QWidget):
    def __init__(self,charName):
        super().__init__()

        self.frame_data = pd.read_csv("data/frames.csv")
        self.char_data = self.frame_data[self.frame_data["Character"]==charName]

        self.layout = QtWidgets.QGridLayout(self)

        windowTitle = QtWidgets.QLabel(charName)
        windowTitle.setMaximumSize(30,10)
        self.layout.addWidget(windowTitle,0,0)

        self.numButtons = QtWidgets.QButtonGroup()
        for i in range(1,10):
            button = QtWidgets.QPushButton(str(i))
            button.setCheckable(True)
            self.numButtons.addButton(button,i)
        self.numButtons.setExclusive(True)

        self.layout.addWidget(self.numButtons.button(7),1,0)
        self.layout.addWidget(self.numButtons.button(8),1,1)
        self.layout.addWidget(self.numButtons.button(9),1,2)
        self.layout.addWidget(self.numButtons.button(4),2,0)
        self.layout.addWidget(self.numButtons.button(5),2,1)
        self.layout.addWidget(self.numButtons.button(6),2,2)
        self.layout.addWidget(self.numButtons.button(1),3,0)
        self.layout.addWidget(self.numButtons.button(2),3,1)
        self.layout.addWidget(self.numButtons.button(3),3,2)
        self.numButtons.button(5).setChecked(True)

        self.attackButtons = QtWidgets.QButtonGroup()
        self.attacks = ["LP","MP","HP","LK","MK","HK"]
        for i in range(6):
            button = QtWidgets.QPushButton(self.attacks[i])
            button.setCheckable(True)
            self.attackButtons.addButton(button,i)
        self.attackButtons.setExclusive(False)
        
        self.layout.addWidget(self.attackButtons.button(0),1,4)
        self.layout.addWidget(self.attackButtons.button(1),1,5)
        self.layout.addWidget(self.attackButtons.button(2),1,6)
        self.layout.addWidget(self.attackButtons.button(3),2,4)
        self.layout.addWidget(self.attackButtons.button(4),2,5)
        self.layout.addWidget(self.attackButtons.button(5),2,6)

        self.resultTable = QtWidgets.QTableWidget(self)
        self.layout.addWidget(self.resultTable,1,7,3,6)
        self.resultTable.setColumnCount(len(list(self.char_data.columns)[1:-1]))
        self.resultTable.setHorizontalHeaderLabels(list(self.char_data.columns)[1:-1])

        self.returnButton = QtWidgets.QPushButton("Return to main screen")
        self.layout.addWidget(self.returnButton,4,0,1,3)
        self.returnButton.clicked.connect(self.returnToMain)

    # def initTable(self):
    #     resultTable = self.resultTable
        

    def returnToMain(self):
        widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = QtWidgets.QStackedWidget()
    mainWindow = MainWindow()
    widget.addWidget(mainWindow)
    mainWindow.initCharScreens()
    widget.resize(1280,720)
    widget.show()

    with open("styles/style.qss","r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())