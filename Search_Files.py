# -*- coding: utf-8 -*-
# __author__=Jason
import sqlite3


def file_exists(file):
    search_result = []
    file = '%' + file + '%'
    con = sqlite3.connect('file_list_new.sqlite')
    cursor = con.cursor()
    file_list = cursor.execute('''SELECT path FROM file WHERE path LIKE (?) ''', (file,))
    for x in file_list:
        search_result.append(x[0])
    return search_result
    con.close()
