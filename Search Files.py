# coding=utf-8
# __author__ = Jason Zhang
search_target = input('Please input the file name you want to search')


def search(file_path):
    with open('file_record.txt') as fl:
        for x in fl.readlines():
            if search_target in x:
                print(x.strip())
            else:
                continue
