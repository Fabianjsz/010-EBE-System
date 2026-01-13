#import
import sqlite3
import os

#Variables
global dbName

dbName = "BackendDatabase.db"


#Functions

def createTable():
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(kundenTabelle)
    con.commit()
    con.close()

def createKunde():
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute()
    con.commit()
    con.close()

#Erstellt Kundentabelle
# Anmerkung: ausweisart und 
kundenTabelle = """
    CREATE TABLE IF NOT EXISTS kunden(
        kunden_nr INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        vorname VARCHAR(30) NOT NULL,
        geschlecht VARCHAR(1),
        geburtsdatum DATE,
        strasse VARCHAR(50) NOT NULL,
        hausnummer INTEGER NOT NULL,
        plz INTEGER(6) NOT NULL,
        ort VARCHAR(30) NOT NULL,
        ausweisart VARCHAR(30), 
        ausweisnummer VARCHAR(30),
        gesetzlicher_vertreter kunden_nr)
"""

#createTable()