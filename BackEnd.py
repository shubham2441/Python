import sqlite3

def connect():
    conn=sqlite3.connect("Movie.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS rental (id INTEGER PRIMARY KEY, name text, title text, time integer, phone integer, address text)")
    conn.commit()
    conn.close()

def insert(name, title, time, phone, address):
    conn=sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO rental VALUES(NULL,?,?,?,?,?)", (name, title, time, phone, address))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM rental")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(name="", title="", time="", phone="", address=""):
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM rental WHERE name=? OR title=? OR time=? OR phone=? OR address=?", (name, title, time, phone, address))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("Movie.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM rental WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, title, time, phone, address):
    conn = sqlite3.connect("Movie.db")
    cur = conn.cursor()
    cur.execute("UPDATE rental SET name=?, title=?, time=?, phone=?, address=? WHERE id=?", (name, title, time, phone, address, id))
    conn.commit()
    conn.close()

def calculate(cost, time):
    amount = int(cost) + (int(time)*10)
    return amount

connect()



