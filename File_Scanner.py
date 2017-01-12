# coding=utf-8
# __author__=Jason
import os
import sqlite3
from time import time


def scanner():
    con = sqlite3.connect('file_list_new.sqlite')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS file (path)''')
    cursor.execute('''DELETE FROM file''')
    con.commit()
    file_to_update = []
    start = time()
    updated_files = 0
    if os.name == 'nt':
        volume = ''.join(os.popen('wmic VOLUME get DriveLetter').read().split('\n')).split()
        volume.pop(0)
    else:
        volume = ['/']
    for i in volume:
        List = os.walk(i + '/')
        for directory, dir_list, file_list in List:
            for x in file_list:
                file_path = directory.replace('\\', '/') + '/' + x
                file_to_update.append(file_path)
                updated_files += 1

    for x in file_to_update:
        cursor.execute('''INSERT INTO file ('path') VALUES (?)''', (x,))
    con.commit()
    con.close()
    result = 'Time_used:' + str(int(time() - start)) + ', and ' + str(updated_files) + ' files were found.'
    return result
