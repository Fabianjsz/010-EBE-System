#import
import sqlite3
import os

#Variables
global dbName

dbName = "Hintergrundsystem.db"


#Functions

def createTable(table):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(table)
    con.commit()
    con.close()


kundenTable = """CREATE TABLE IF NOT EXISTS kunden(
    nr INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    vorname TEXT,
    geschlecht VARCHAR(1),
    geburtsdatum DATE,
    strasse TEXT,
    plz VARCHAR(6),
    ort TEXT,
    ausweisart_id INTEGER,
    ausweisnummer TEXT,
    gesetzlicher_vertreter_id INTEGER,
    FOREIGN KEY (ausweisart_id) REFERENCES ausweisart(id),
    FOREIGN KEY (gesetzlicher_vertreter_id) REFERENCES kunden(nr)
)"""

ausweisTable = """CREATE TABLE IF NOT EXISTS ausweisart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bezeichnung TEXT
    )"""



createTable()