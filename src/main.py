import sys
import re
import os
from os import path
import pandas as pd
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui
from DataFrameModel import *
from palettes import *
from enum import IntEnum

FRAME_PATH = "data\\frame_data\\frames.csv"
CHAR_PORTRAITS = "data\\assets\\char_portraits"
CHAR_DATA = "data\\assets\\char_data"
STYLE_PATH = "data\\styles"

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("Main_Window")
        #self.setPalette(mm_palette)
        #self.setAutoFillBackground(True)

        self.frame_data = pd.read_csv(FRAME_PATH)

        self.chars = pd.unique(self.frame_data["Character"])

        self.buttons = []

        portraits = os.listdir(CHAR_PORTRAITS)
        
        self.layout = QtWidgets.QGridLayout(self)

        for char in self.chars:   
            button = QtWidgets.QPushButton(re.sub('_',' ',char)) 
            self.buttons.append(button)
            for i in range(len(portraits)):
                if (re.sub('[\\W]+','',button.text()).lower() in re.sub('[\\W]+','',portraits[i]).lower()):
                    #button.setIcon(QtGui.QIcon(CHAR_PORTRAITS+"/"+portraits[i]))
                    button.setStyleSheet(f'''
                        border-image: url({str.replace(CHAR_PORTRAITS,'\\','/')+"/"+portraits[i]});
                    ''')
            button.setObjectName("Main_Menu_Button")
            button.clicked.connect(self.goToScreen)

        title = QtWidgets.QLabel("Street Fighter 6 Frame Data Visualizer")
        self.layout.addWidget(title,0,0,1,5,alignment=Qt.AlignmentFlag.AlignHCenter)

        row = 0
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

    def paintEvent(self,event: QtGui.QPaintEvent):
        super().paintEvent(event)
        paint = QtGui.QPainter(self)
        paint.setBrush(QBrush(QColor('darkGray'),Qt.BrushStyle.SolidPattern))
        # opt = QtWidgets.QStyleOption.initFrom(self)
        # QtWidgets.QStyle.drawPrimitive(pe=QtWidgets.QStyle.PrimitiveElement(),opt=opt,p=paint,widget=self)
        # QtWidgets.QWidget.paintEvent(event)
        paint.drawRect(0,0,self.width(),self.height())

class CharWindow(QtWidgets.QWidget):
    def __init__(self,charName):
        super().__init__()

        cols = IntEnum('cols',
                         [ 'origin'
                          ,'midNum'
                          ,'rightNum'
                          ,'leftAttack'
                          ,'midAttack'
                          ,'rightAttack'
                          ,'midSpacer'
                          ,'tablesStart'
                          ,'counterHit'
                          ,'punishCounter'
                          ,'driveRush'
                          ,'rightEdge'],start=0)
        rows = IntEnum('rows',
                         ['origin'
                          ,'topNum'
                          ,'midNum'
                          ,'botNum'
                          ,'gifRow'
                          ,'returnButton'
                          ,'bottomEdge'],start=0)

        self.charName = charName

        self.setPalette(cw_palette)
        self.setAutoFillBackground(True)

        # Dataframe init
        self.frame_data = pd.read_csv(FRAME_PATH)
        self.char_data = self.frame_data[self.frame_data["Character"]==self.charName]
        self.char_data = self.char_data.drop(["Character"],axis=1)

        # Layout init
        layout = QtWidgets.QGridLayout(self)

        # Char Name
        windowTitle = QtWidgets.QLabel(re.sub("_"," ",self.charName))
        layout.addWidget(windowTitle,0,0,1,4)

        # Numpad buttons
        self.numButtons = QtWidgets.QButtonGroup()
        for i in range(1,10):
            button = QtWidgets.QPushButton(str(i))
            button.setCheckable(True)
            button.setObjectName("Num_Button")
            button.setAutoFillBackground(True)
            self.numButtons.addButton(button,i)
        self.numButtons.setExclusive(True)
        self.numButtons.buttonClicked.connect(self.updateFrameTable)

        # Adding to layout
        layout.addWidget(self.numButtons.button(7),rows.topNum,cols.origin,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.numButtons.button(8),rows.topNum,cols.midNum,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.numButtons.button(9),rows.topNum,cols.rightNum,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.numButtons.button(4),rows.midNum,cols.origin,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.numButtons.button(5),rows.midNum,cols.midNum,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.numButtons.button(6),rows.midNum,cols.rightNum,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.numButtons.button(1),rows.botNum,cols.origin,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.numButtons.button(2),rows.botNum,cols.midNum,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.numButtons.button(3),rows.botNum,cols.rightNum,alignment=Qt.AlignmentFlag.AlignCenter)
        self.numButtons.button(5).setChecked(True)

        # Sizing the elements
        #layout.addWidget(QtWidgets.QLabel(),0,cols.midSpacer,rows.bottomEdge,1)
        layout.setColumnStretch(cols.midSpacer,250)
        layout.setColumnStretch(cols.tablesStart,250)
        # for col in range(cols.midSpacer,cols.rightEdge):
        #     layout.setColumnStretch(col,1000)
        # #print(layout.item)

        # Attack buttons
        self.attackButtons = QtWidgets.QButtonGroup()
        attacks = ["LP","MP","HP","LK","MK","HK"]
        for i in range(6):
            button = QtWidgets.QPushButton(attacks[i])
            button.setCheckable(True)
            button.setObjectName("Attack_Button")
            button.setAutoFillBackground(True)
            self.attackButtons.addButton(button,i)
        self.attackButtons.setExclusive(False)
        self.attackButtons.buttonClicked.connect(self.updateFrameTable)
        
        # Adding to layout
        layout.addWidget(self.attackButtons.button(0),1,3,alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.attackButtons.button(1),1,4,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.attackButtons.button(2),1,5,alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.attackButtons.button(3),2,3,alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.attackButtons.button(4),2,4,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.attackButtons.button(5),2,5,alignment=Qt.AlignmentFlag.AlignTop)

        # Adding specials checkbox
        self.specialCheckbox = QtWidgets.QCheckBox("Include specials")
        layout.addWidget(self.specialCheckbox,4,7,1,1)
        self.specialCheckbox.clicked.connect(self.updateFrameTable)

        # Adding move gif
        self.moveImage = QtWidgets.QLabel("Double click on a move to display the hitbox data!")
        self.moveImage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.moveImage.setFixedSize(300,300)
        self.moveImage.setScaledContents(True)
        layout.addWidget(self.moveImage,rows.gifRow,cols.origin,1,cols.leftAttack)

        # Creating result table
        self.resultTable = QtWidgets.QTableView(self)
        layout.addWidget(self.resultTable,1,cols.tablesStart,3,6)
        self.resultTable.setModel(DataFrameModel(self.char_data))
        self.updateFrameTable()
        self.resultTable.doubleClicked.connect(self.updateLinkTable)
        self.resultTable.doubleClicked.connect(self.updateMoveGif)

        # Creating link table
        self.linkTable = QtWidgets.QTableView(self)
        layout.addWidget(self.linkTable,5,7,1,6)
        self.linkTable.setModel(DataFrameModel(self.char_data))
        self.linkTable.setMaximumHeight(200)

        # Adding counter hit, punish counter, and drive rush boxes
        self.hitAdv = QtWidgets.QButtonGroup()
        self.hitAdv.addButton(QtWidgets.QCheckBox("NH (+0)"),0)
        self.hitAdv.addButton(QtWidgets.QCheckBox("CH (+2)"),1)
        self.hitAdv.addButton(QtWidgets.QCheckBox("PC (+4)"),2)
        self.dr = QtWidgets.QCheckBox("DR (+4)")
        layout.addWidget(self.hitAdv.button(0),6,7,1,1)
        layout.addWidget(self.hitAdv.button(1),6,8,1,1)
        layout.addWidget(self.hitAdv.button(2),6,9,1,1)
        layout.addWidget(self.dr,6,10,1,1)
        self.hitAdv.buttonClicked.connect(self.updateLinkTable)
        self.hitAdv.button(0).setChecked(True)
        self.dr.clicked.connect(self.updateLinkTable)
        
        # Return button
        self.returnButton = QtWidgets.QPushButton("Return to main screen")
        layout.addWidget(self.returnButton,rows.bottomEdge,cols.origin,1,2)
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
        ind = QtCore.QAbstractItemModel.createIndex(self.resultTable.model(),mi.row(),3)
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
        charPath = re.sub("[\W\.\_]+","",self.charName).lower()
        ind = QtCore.QAbstractItemModel.createIndex(self.resultTable.model(),mi.row(),0)
        move_input = self.resultTable.model().data(ind)
        move_input = re.sub("\d\/","",move_input)
        move_input = re.sub("8","nj-",move_input)
        move_input = re.sub("9","j-",move_input)
        move_input = re.sub("j.","j-",move_input)
        move_input = re.sub("\[","",move_input)
        move_input = re.sub("\]","-hold",move_input)
        gifPath = CHAR_DATA+"/"+charPath+"/"+charPath+"-"+move_input.lower()+".gif"
        movie = QtGui.QMovie(gifPath)
        self.moveImage.setMovie(movie)
        movie.start()

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

    with open(STYLE_PATH+"/style.qss","r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())