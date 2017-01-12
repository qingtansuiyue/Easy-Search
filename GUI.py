# coding = utf-8
from tkinter import *

from File_Scanner import scanner
from Search_Files import file_exists

root = Tk()
root.title('Easy-Search by Jason')
u = StringVar()
p = StringVar()


def scan():
    Result_Field['text'] = 'Scan Result'
    result = scanner()
    file_list.delete(0.0, END)
    file_list.insert(1.0, result)


def search():
    Result_Field['text'] = 'File List'
    file_list.delete(0.0, END)
    file = ''
    n = 0
    search_result = file_exists(u.get())
    for x in search_result:
        file_list.insert(1.0, x + '\n')


# Create some frames as container
ent1 = Entry(root, textvariable=u, width=100)
ent1.grid(row=0, column=1, columnspan=2, sticky=W)

file_list = Text(root, width=100, height=30)
file_list.grid(row=1, column=1)
# create some labels
Label(root, text='File Name').grid(row=0, column=0, sticky=W)
Result_Field = Label(root, text='File List')
Result_Field.grid(row=1, column=0, sticky=W)
# Create some buttons
button_search = Button(root, text='Search', command=search, default='active')
button_search.grid(row=0, column=3, sticky=W)
button_scan = Button(root, text='Scan', command=scan)
button_scan.grid(row=0, column=4, sticky=W)
# Locate frames with grid

root.mainloop()
