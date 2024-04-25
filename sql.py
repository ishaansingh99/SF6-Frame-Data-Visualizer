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

    # create a table
    query.exec('''CREATE TABLE characters (
                    CharID      INTEGER,
                    CharName    TEXT,
                    PRIMARY KEY (CharID)
                    );''')

    # populate the table
    query.exec('''INSERT INTO characters VALUES (0,"A.K.I.");''')
    query.exec('''INSERT INTO characters VALUES (1,"Blanka");''')
    query.exec('''INSERT INTO characters VALUES (2,"Cammy");''')
    query.exec('''INSERT INTO characters VALUES (3,"Chun-Li");''')
    query.exec('''INSERT INTO characters VALUES (4,"Dee Jay");''')
    query.exec('''INSERT INTO characters VALUES (5,"Dhalsim");''')
    query.exec('''INSERT INTO characters VALUES (6,"Ed");''')
    query.exec('''INSERT INTO characters VALUES (7,"Honda");''')
    query.exec('''INSERT INTO characters VALUES (8,"Guile");''')
    query.exec('''INSERT INTO characters VALUES (9,"Jamie");''')
    query.exec('''INSERT INTO characters VALUES (10,"JP");''')
    query.exec('''INSERT INTO characters VALUES (11,"Juri");''')
    query.exec('''INSERT INTO characters VALUES (12,"Ken");''')
    query.exec('''INSERT INTO characters VALUES (13,"Kimberly");''')
    query.exec('''INSERT INTO characters VALUES (14,"Lily");''')
    query.exec('''INSERT INTO characters VALUES (15,"Luke");''')
    query.exec('''INSERT INTO characters VALUES (16,"Manon");''')
    query.exec('''INSERT INTO characters VALUES (17,"Marisa");''')
    query.exec('''INSERT INTO characters VALUES (18,"Rashid");''')
    query.exec('''INSERT INTO characters VALUES (19,"Ryu");''')
    query.exec('''INSERT INTO characters VALUES (20,"Zangief");''')

    query.exec("""CREATE TABLE frame_data (
                MoveID INTEGER,
                CharID INTEGER,
                CharName TEXT,
                Input TEXT,
                Startup INTEGER,
                Active INTEGER,
                OH INTEGER,
                OB INTEGER,
                PRIMARY KEY (MoveID),
                FOREIGN KEY (CharID) REFERENCES characters(CharID)
                );""")

    query.exec('''INSERT INTO frame_data VALUES (0,0,"A.K.I.","5LP",5,2,4,-1);''')
    query.exec('''INSERT INTO frame_data VALUES (1,0,"A.K.I.","5MP",6,5,3,-3);''')
    query.exec('''INSERT INTO frame_data VALUES (2,0,"A.K.I.","5HP",12,3,1,-5);''')
    query.exec('''INSERT INTO frame_data VALUES (3,0,"A.K.I.","5LK",5,3,4,-2);''')
    query.exec('''INSERT INTO frame_data VALUES (4,0,"A.K.I.","5MK",9,3,6,-2);''')
    query.exec('''INSERT INTO frame_data VALUES (5,0,"A.K.I.","5HK",9,4,4,-3);''')

    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5LP",4,3,4,-1);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5MP",6,4,7,-1);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5HP",12,3,1,-5);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5LK",5,3,4,-2);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5MK",9,3,6,-2);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5HK",9,4,4,-3);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5LP",5,2,4,-1);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5MP",6,5,3,-3);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5HP",12,3,1,-5);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5LK",5,3,4,-2);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5MK",9,3,6,-2);''')
    query.exec('''INSERT INTO frame_data VALUES (0,0,"Ryu","5HK",9,4,4,-3);''')
    
    db.close()
    
if __name__ == '__main__':
   app = QApplication(sys.argv)
   createDB()