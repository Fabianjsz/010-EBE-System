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

def insertData(query, data):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(query, data)
    con.commit()
    con.close()

def createAusweisartTable():
    createTable(ausweisTable)
    con = sqlite3.connect(dbName)
    cur = con.cursor()
    cur.execute("insert into ausweisart (bezeichnung) VALUES (?), (?), (?)", ("Personalausweis", "Schülerausweis", "Reisepass"))
    con.commit()
    con.close()

def dropTable(table):
    con = sqlite3.connect(dbName)
    cursor = con.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    con.commit()
    con.close()

def createEBE(datum, name, vorname, adresse, hausnummer, plz, ort, ausweisart, ausweisnr, kontrolleur_id, feststellungsort, bemerkung):
    con = sqlite3.connect(dbName)
    cur = con.cursor()
    cur.execute("insert into ebe (datum, name, vorname, adresse, hausnummer, plz, ort, ausweisart, ausweis_nr, kontrolleur_id, feststellungsort, Bemerkung) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (f"{datum}", f"{name}", f"{vorname}", f"{adresse}", f"{hausnummer}", f"{plz}", f"{ort}", f"{ausweisart}", f"{ausweisnr}", f"{kontrolleur_id}", f"{feststellungsort}", f"{bemerkung}"))
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

kontrolleurTable = """CREATE TABLE IF NOT EXISTS kontrolleur(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    vorname TEXT
    )"""

ebeTable = """CREATE TABLE IF NOT EXISTS ebe(
    nr INTEGER PRIMARY KEY AUTOINCREMENT,
    datum DATE,
    name TEXT,
    vorname TEXT,
    adresse TEXT,
    hausnummer INT,
    plz INT,
    ort TEXT,
    ausweisart TEXT,
    ausweis_nr INT,
    kontrolleur_id INTEGER,
    feststellungsort TEXT,
        bemerkung TEXT
    )"""



#dropTable("ebe")
#createTable(ebeTable)

