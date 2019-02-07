import sqlite3
from datetime import datetime, timezone




class db():
    def __init__(self):
        self.cursor = None
        self.dbConnector = None
        
    def put(self, table, data):
        self.dbConnector = sqlite3.connect('yatadb.db')
        self.cursor = self.dbConnector.cursor()
        self.cursor.execute("INSERT INTO {} (date, text) VALUES ({},{})".format(table, datetime.now(timezone.utc), data))