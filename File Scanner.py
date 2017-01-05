# **---encoding=utf-8-----
# __author__=Jason
import os
from time import time

with open('file_record.txt', 'r') as fl:
    path_list = fl.readlines()

updated_files = 0
if os.name == 'nt':
    volume = ''.join(os.popen('wmic VOLUME get DriveLetter').read().split('\n')).split()
    volume.pop(0)
else:
    volume = ['/']


def created_time(file):
    time_list = os.stat(file)
    return time_list.st_ctime


f = open(r'file_record.txt', 'a', encoding='utf-8')

start = time()

for i in volume:
    List = os.walk(i + '/')
    for directory, dir_list, file_list in List:
        for x in file_list:
            try:
                file_path = directory.replace('\\', '/') + '/' + x
                if file_path in path_list:
                    continue
                else:
                    f.write(file_path + '\n')
                    print(file_path)
                    updated_files += 1
            except IOError:
                continue

f.close()

print('Time_used:', time() - start)
print(updated_files, 'file records were updated')
