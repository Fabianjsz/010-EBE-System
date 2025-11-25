#import
import sqlite3
import os

#Variables
global dbName

dbName = "Hintergrundsystem"


#Functions

def createTable():
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute("")
    con.commit()
    con.close()