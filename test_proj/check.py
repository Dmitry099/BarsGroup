import sqlite3 as lite
import sys

con = lite.connect('db.sqlite3')

with con:
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute("SELECT * FROM sith_recruter;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute("PRAGMA table_info(sith_recruter);")
    rows = cur.fetchall()
    print(rows)
    # con.commit()