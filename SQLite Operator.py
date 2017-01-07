# coding=utf-8
# __author__ = Jason Zhang

import sqlite3

con = sqlite3.connect('file_list.db')
cursor = con.cursor()

cursor.execute('CREATE TABLE file list(file_path text)')
