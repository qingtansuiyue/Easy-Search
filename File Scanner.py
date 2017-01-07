# coding=utf-8
# __author__=Jason
import os
import sqlite3
from time import time

con = sqlite3.connect('file_list_new.sqlite')
cursor = con.cursor()

file_to_update = []


def insert_file(file):
    cursor.execute('''INSERT INTO file ('path') VALUES (?)''', (file,))


def file_exists(file):
    if_file = cursor.execute('''SELECT path FROM file WHERE path= (?) ''', (file,))
    for x in if_file:
        if x:
            return 1
            break
        else:
            return 0


updated_files = 0
if os.name == 'nt':
    volume = ''.join(os.popen('wmic VOLUME get DriveLetter').read().split('\n')).split()
    volume.pop(0)
else:
    volume = ['/']

start = time()

for i in volume:
    List = os.walk(i + '/')
    for directory, dir_list, file_list in List:
        for x in file_list:
            file_path = directory.replace('\\', '/') + '/' + x
            if file_exists(file_path):
                updated_files += 1
                print(updated_files)
                continue
            else:
                file_to_update.append(file_path)
                updated_files += 1
                print(file_path)

for x in file_to_update:
    insert_file(x)
con.commit()
con.close()
print('Time_used:', time() - start)
print(updated_files, 'file records were updated')
