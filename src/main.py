import sys
import re
import os
import pandas as pd
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui, QtSql
from DataFrameModel import *

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.frame_data = pd.read_csv("data/frames.csv")

        self.chars = pd.unique(self.frame_data["Character"])

        self.buttons = []

        portraits = os.listdir("assets/char_portraits")
        
        self.layout = QtWidgets.QGridLayout(self)

        for char in self.chars:   
            button = QtWidgets.QPushButton(re.sub('_',' ',char)) 
            self.buttons.append(button)
            for i in range(len(portraits)):
                if (re.sub('[\\W]+','',button.text()).lower() in re.sub('[\\W]+','',portraits[i]).lower()):
                    button.setIcon(QtGui.QIcon("assets/char_portraits/"+portraits[i]))
            button.setFixedSize(100,100)
            #button.setContentsMargins(0,0,0,0)
            #button.setIconSize(QtCore.QSize(100,100))
            #button.setText("")
            button.setObjectName("Main_Menu")
            button.clicked.connect(self.goToScreen)

        row = -1
        for i in range(len(self.chars)):
            col = i % 5
            if (col == 0): row += 1
            self.layout.addWidget(self.buttons[i],row,col)


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

        # Dataframe init
        self.frame_data = pd.read_csv("data/frames.csv")
        self.char_data = self.frame_data[self.frame_data["Character"]==charName]

        # Layout init
        self.layout = QtWidgets.QGridLayout(self)

        # Char Name
        windowTitle = QtWidgets.QLabel(charName)
        windowTitle.setMaximumSize(30,10)
        self.layout.addWidget(windowTitle,0,0)

        # Numpad buttons
        self.numButtons = QtWidgets.QButtonGroup()
        for i in range(1,10):
            button = QtWidgets.QPushButton(str(i))
            button.setCheckable(True)
            button.setObjectName("Char_Button")
            self.numButtons.addButton(button,i)
        self.numButtons.setExclusive(True)
        self.numButtons.buttonClicked.connect(self.updateFrameTable)

        # Adding to layout
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

        # Attack buttons
        self.attackButtons = QtWidgets.QButtonGroup()
        self.attacks = ["LP","MP","HP","LK","MK","HK"]
        for i in range(6):
            button = QtWidgets.QPushButton(self.attacks[i])
            button.setCheckable(True)
            self.attackButtons.addButton(button,i)
        self.attackButtons.setExclusive(False)
        self.attackButtons.buttonClicked.connect(self.updateFrameTable)
        
        # Adding to layout
        self.layout.addWidget(self.attackButtons.button(0),1,4)
        self.layout.addWidget(self.attackButtons.button(1),1,5)
        self.layout.addWidget(self.attackButtons.button(2),1,6)
        self.layout.addWidget(self.attackButtons.button(3),2,4)
        self.layout.addWidget(self.attackButtons.button(4),2,5)
        self.layout.addWidget(self.attackButtons.button(5),2,6)

        # Adding specials checkbox
        self.specialCheckbox = QtWidgets.QCheckBox("Include specials")
        self.layout.addWidget(self.specialCheckbox,4,7,1,1)
        self.specialCheckbox.clicked.connect(self.updateFrameTable)

        # Adding move gif
        #movie = QtGui.QMovie("assets/char_data/AKI/aki-2hk.gif")
        self.moveImage = QtWidgets.QLabel("Test")
        #self.moveImage.setMovie(movie)
        #movie.start()
        self.moveImage.setFixedSize(200,200)
        self.moveImage.setScaledContents(True)
        self.layout.addWidget(self.moveImage,5,0,1,1)

        # Creating result table
        self.resultTable = QtWidgets.QTableView(self)
        self.layout.addWidget(self.resultTable,1,7,3,6)
        self.resultTable.setModel(DataFrameModel(self.char_data))
        self.updateFrameTable()
        self.resultTable.doubleClicked.connect(self.updateLinkTable)

        # Creating link table
        self.linkTable = QtWidgets.QTableView(self)
        self.layout.addWidget(self.linkTable,5,7,1,6)
        self.linkTable.setModel(DataFrameModel(self.char_data))
        self.linkTable.setMaximumHeight(200)

        # Adding counter hit, punish counter, and drive rush boxes
        self.hitAdv = QtWidgets.QButtonGroup()
        self.hitAdv.addButton(QtWidgets.QCheckBox("NH (+0)"),0)
        self.hitAdv.addButton(QtWidgets.QCheckBox("CH (+2)"),1)
        self.hitAdv.addButton(QtWidgets.QCheckBox("PC (+4)"),2)
        self.dr = QtWidgets.QCheckBox("DR (+4)")
        self.layout.addWidget(self.hitAdv.button(0),6,7,1,1)
        self.layout.addWidget(self.hitAdv.button(1),6,8,1,1)
        self.layout.addWidget(self.hitAdv.button(2),6,9,1,1)
        self.layout.addWidget(self.dr,6,10,1,1)
        self.hitAdv.buttonClicked.connect(self.updateLinkTable)
        self.hitAdv.button(0).setChecked(True)
        self.dr.clicked.connect(self.updateLinkTable)
        
        # Return button
        self.returnButton = QtWidgets.QPushButton("Return to main screen")
        self.layout.addWidget(self.returnButton,4,0,1,3)
        self.returnButton.clicked.connect(self.returnToMain)

    def updateFrameTable(self):
        # Checking direction (one is always pressed)
        num = self.numButtons.checkedButton().text()
        attack = ""

        # Checking for any attack buttons, can be none or multiple
        for button in self.attackButtons.buttons():
            if (button.isChecked()):
                attack += button.text()

        # If more than one attack button remove the strengths
        if len(attack) > 2:
            attack = re.sub('[^KP]','',attack)

        # Check for specials
        if (self.specialCheckbox.isChecked()):
            if (num in '789'):
                new_data = self.char_data[(self.char_data["Input"].str.contains(num) | (self.char_data["Input"].str.contains('j'))) & (self.char_data["Input"].str.contains(attack))]
            else:
                new_data = self.char_data[(self.char_data["Input"].str.contains(num)) & (self.char_data["Input"].str.contains(attack))]
        else:
            if (num in '789'):
                new_data = self.char_data[(self.char_data["Input"].str.contains(num) | (self.char_data["Input"].str.contains('j'))) & (self.char_data["Input"].str.contains(attack)) & (self.char_data["Type"] == "Normal")]  
            else:
                new_data = self.char_data[(self.char_data["Input"].str.contains(num)) & (self.char_data["Input"].str.contains(attack)) & (self.char_data["Type"] == "Normal")]  
        
        # Update data in table
        self.resultTable.model().setDataFrame(new_data)    

    def updateLinkTable(self):
        try:
            mi = self.resultTable.selectedIndexes()[0]
        except IndexError:
            return
        ind = QtCore.QAbstractItemModel.createIndex(self.resultTable.model(),mi.row(),0)
        new_data = self.char_data[(self.char_data["Startup"].str.isnumeric()) & (self.char_data["Type"] == "Normal") & ~(self.char_data["Input"].str.contains("j"))]
        adv = 0
        try:
            adv = int(self.resultTable.model().data(ind))
        except ValueError:
            adv = 0
            return
        if (self.hitAdv.button(1).isChecked()): adv += 2
        if (self.hitAdv.button(2).isChecked()): adv += 4
        if (self.dr.isChecked()): adv += 4 
        new_data = new_data[(new_data["Startup"].astype(int) <= adv)]
        self.linkTable.model().setDataFrame(new_data)

    def updateMoveGif(self):
        try:
            mi = self.resultTable.selectedIndexes()[0]
        except IndexError:
            return
        ind = QtCore.QAbstractItemModel.createIndex(self.resultTable.model(),mi.row(),3)
        move_input = self.resultTable.model().data(ind)
        


    def returnToMain(self):
        widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = QtWidgets.QStackedWidget()
    mainWindow = MainWindow()
    widget.addWidget(mainWindow)
    mainWindow.initCharScreens()
    widget.resize(1366,720)
    widget.show()

    with open("styles/style.qss","r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())