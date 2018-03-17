import sqlite3
import json

class Authenticate:
    global conn, cur
    conn = sqlite3.connect('moodcafe.db', check_same_thread=False)
    conn.text_factory = str
    cur = conn.cursor()
    def __init__(self):
        __sql = 'create table if not exists authenticate (username text,email text)'
        cur.execute(__sql)
        conn.commit()

    def intertData(self,username,email):
        cur.execute("INSERT INTO authenticate (username, email) VALUES(?,?)",[username, email])
        conn.commit()
        return authenticate.fetch_all()

    def fetch_all(self):
        __data = cur.execute('SELECT * FROM authenticate')
        __allData =  __data.fetchall()
        return __allData

authenticate = Authenticate()