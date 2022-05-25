import sqlite3, os

class DB:
    conn = ""
    cur  = ""
    
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join('db', 'okulOtomasyon.db'))
        self.cur  = self.conn.cursor()
    
    def close(self):
        self.conn.close()