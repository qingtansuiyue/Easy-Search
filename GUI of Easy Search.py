from tkinter import *


def scanner():
    # os.system('''python "File Scanner.py"''')
    print('Scanning')


root = Tk()
root.title('Easy-Search by Jason')
# Create some frames as container
frame_input = Frame(width=300, height=20, bg='white')
frame_result = Frame(width=550, height=600, bg='white')
# create some labels
Label(root, text='File Name').grid(row=0, sticky=W)
# Create some buttons
button_search = Button(root, text='Search')
button_search.grid(row=0, column=2, sticky=W)
button_scan = Button(root, text='Scan', command=scanner)
button_search.grid(row=0, column=3, sticky=W)
# Locate frames with grid
frame_input.grid(row=0, column=1)
frame_result.grid(row=1, column=0, columnspan=4)

root.mainloop()
