import os
import sqlite3
from multiprocessing import Process, Queue
from time import time

updated_files = 0
file_to_update = []
start = time()
if os.name == 'nt':
    volume = ''.join(os.popen('wmic VOLUME get DriveLetter').read().split('\n')).split()
    volume.pop(0)
else:
    volume = ['/']


def scanner(i, q):
    List = os.walk(i + '/')
    for directory, dir_list, file_list in List:
        for x in file_list:
            file_path = directory.replace('\\', '/') + '/' + x
            q.put(file_path, timeout=3)


if __name__ == '__main__':
    con = sqlite3.connect('file_list_new.sqlite')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS file (path)''')
    cursor.execute('''DELETE FROM file''')
    con.commit()
    q = Queue()
    for x in volume:
        p = Process(target=scanner, args=(x, q,))
        p.start()
    while True:
        try:
            file = q.get(timeout=3)
            file_to_update.append(file)
            updated_files += 1
        except:
            break
    p.join()
    for x in file_to_update:
        cursor.execute('''INSERT INTO file ('path') VALUES (?)''', (x,))
    con.commit()
    con.close()
    time_used = time() - start
    result = 'Time_used:' + str(int(time() - start)) + ' seconds, and ' + str(
        len(file_to_update)) + ' files were found.'
    print(result)
