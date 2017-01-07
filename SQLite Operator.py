# coding=utf-8
# __author__ = Jason Zhang

import sqlite3

con = sqlite3.connect('file_list.db')
cursor = con.cursor()

# cursor.execute('''CREATE TABLE file (path)''')
with open('file_record.txt', 'r', encoding='utf-8') as f:
    for x in f.readlines():
        cursor.execute('''INSERT INTO file ('path') VALUES (?)''', (x,))

con.commit()
con.close()
