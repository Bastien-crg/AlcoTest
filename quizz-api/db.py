import json
import sqlite3
import datetime

class Database():
    def __init__(self, name : str):
        self.name = name
    
    def createDatabase(self):
        db = sqlite3.connect(self.name)
        try:
            cur = db.cursor()
            with open("SQLBase.db.sql", 'r', encoding="utf-8") as sql_file:
                cur.executescript(sql_file.read())
        finally:
            cur.close()
        
