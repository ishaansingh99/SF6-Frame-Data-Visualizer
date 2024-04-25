import sys
from PySide6.QtSql import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sf6_frames.db')
    
    # try to open the database
    if not db.open():
        sys.exit(-1)


    query = QSqlQuery()

    query.exec("SELECT * FROM frame_data WHERE CharID = 0")

    while (query.next()):
        print(query.value("Input"))
    
    db.close()
    
if __name__ == '__main__':
   app = QApplication(sys.argv)
   createDB()