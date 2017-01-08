# coding=utf-8
# __author__ = Jason Zhang
import os
import sqlite3

search_target = input('Please input the file name you want to search')

con = sqlite3.connect('file_list_new.sqlite')
cursor = con.cursor()


def file_exists(file):
    file = '%' + file + '%'
    file_list = cursor.execute('''SELECT path FROM file WHERE path LIKE (?) ''', (file,))
    for x in file_list:
        print(x[0])


file_exists(search_target)
con.close()
os.system('pause')
