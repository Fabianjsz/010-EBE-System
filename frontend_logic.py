import sqlite3
import datetime

global frontdb, front_database

front_database = 'frontend_database.db'
frontdb = False

class EBE():
    def __init__(self, datum, name, vorname, adresse, hausnummer, ort):
        self.datum = datum
        self.name = name
        self.vorname = vorname
        self.adresse = adresse
        self.hausnummer = hausnummer
        self.ort = ort

def init_database():
    global frontdb
    frontdb = True
    conn = sqlite3.connect(front_database)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ebe (ebe_nr INTEGER PRIMARY KEY AUTOINCREMENT, datum DATE, vorname TEXT, name TEXT, adresse TEXT, hausnummer TEXT, ort TEXT)''')
    conn.commit()
    conn.close()



def insert_ebe(datum, vorname, name, adresse, hausnummer, ort):
    global frontdb
    if frontdb == False:
        init_database()
        insert_ebe(datum, vorname, name, adresse, hausnummer, ort)
    else:
        con = sqlite3.connect(front_database)
        cur = con.cursor()
        cur.execute('INSERT INTO ebe (datum, vorname, name, adresse, hausnummer, ort) VALUES (?, ?, ?, ?, ?, ?)', (datum, vorname, name, adresse, hausnummer, ort))
        con.commit()
        con.close()

def create_ebe():
    print("EBE erstellen")
    datum = datetime.date.today()
    vorname = input("Vorname: ")
    name = input("Name: ")
    adresse = input("Adresse: ")
    hausnummer = input("Hausnummer: ")
    ort = input("Ort: ")
    insert_ebe(datum, vorname, name, adresse, hausnummer, ort)

create_ebe()