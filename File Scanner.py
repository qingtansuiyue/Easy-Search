# __author__=Jason
from time import time
import os
from os import popen
from os import stat
from os import walk


updated_files = 0
if os.name == 'nt':
    volume = ''.join(popen('wmic VOLUME get DriveLetter').read().split('\n')).split()
    volume.pop(0)
else:
    volume = ['/']

try:
    last_scan = stat(r'file_record.txt').st_mtime
except IOError:
    print('This is the first time to scan.')
    last_scan = 0


def created_time(file):
    time_list = stat(file)
    return time_list.st_ctime


f = open(r'file_record.txt', 'a')

start = time()

for i in volume:
    List = walk(i+'/')
    for directory, dir_list, file_list in List:
        for x in file_list:
            try:
                file_path = directory.replace('\\','/')+'/'+x
                if created_time(file_path) > last_scan:
                    f.write(file_path+'\n')
                    print(file_path)
                    updated_files += 1
            except IOError:
                continue

f.close()

print('Time_used:', time() - start)
print(updated_files, 'file records were updated')
