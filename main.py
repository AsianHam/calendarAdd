from tkinter import *
from functools import reduce
from operator import add
import changeUser as edit
import re

root = Tk()
root.title("Google Calendar Access Permissions Editor")

canvas = Canvas(root, scrollregion = (0, 0, 500, 500))
canvas.grid(row = 0, column = 0, sticky = 'news')

vbar = Scrollbar(canvas, orient = 'vertical', command = canvas.yview)
vbar.grid(row = 0, column = 5, sticky = 'ens', rowspan = 100)
canvas.configure(yscrollcommand = vbar.set)

frame = Frame(canvas)
frame.grid(row = 0, column = 0, sticky = "news", padx = 30, pady = 30)

enter = StringVar()
v = IntVar()
broadwayBool, yard9aBool, yard9bBool = IntVar(), IntVar(), IntVar()
yard9cBool, lew203aBool, lew203bBool = IntVar(), IntVar(), IntVar()
lew203dBool, lew203eBool, lew203fBool = IntVar(), IntVar(), IntVar()
lew203iBool, lew203k6Bool, lew203k7Bool = IntVar(), IntVar(), IntVar()
lew203nBool, lew203yBool, lew203zBool = IntVar(), IntVar(), IntVar()
lew214aBool, lew303aBool,  lew303cBool = IntVar(), IntVar(), IntVar()
lew504aBool, lew504bBool, lew504cBool = IntVar(), IntVar(), IntVar()
lew504dBool, lew504fBool = IntVar(), IntVar()

prompt1 = Label(frame, text = "Please enter the uni(s) you would like to change permissions for.")
prompt1.grid(row = 0, column = 1, columnspan = 4)

prompt2 = Label(frame, text = "Seperate multiple unis with spaces or commas.")
prompt2.grid(row = 1, column = 1, columnspan = 4)

space2 = Label(frame).grid(row = 2, column = 2)

entry = Entry(frame, textvariable = enter)
entry.grid(row = 3, column = 2, columnspan = 2)

space3 = Label(frame).grid(row = 4, column = 2)
space4 = Label(frame).grid(row = 5, column = 2)

prompt3 = Label(frame, text = "Select whether to add or remove the user(s).")
prompt3.grid(row = 6, column = 1, columnspan = 4)

space5 = Label(frame).grid(row = 7, column = 2)

plusButton = Radiobutton(frame, text = "Add User", variable = v, value = 1, indicatoron = 0)
plusButton.grid(row = 8, column = 2)

minusButton = Radiobutton(frame, text = "Delete User", variable = v, value = 0, indicatoron = 0)
minusButton.grid(row = 8, column = 3)

space6 = Label(frame).grid(row = 9, column = 2)
space7 = Label(frame).grid(row = 10, column = 2)

prompt4 = Label(frame, text = "Select which conference rooms to add the user(s) to.")
prompt4.grid(row = 11, column = 1, columnspan = 4)

space8 = Label(frame).grid(row = 12, column = 2)

b2875 = Checkbutton(frame, text = "2875 Broadway", variable = broadwayBool, indicatoron = 0)
b2875.grid(row =13, column = 1)

lc9a = Checkbutton(frame, text = "The Yard 9th: A", variable = yard9aBool, indicatoron = 0)
lc9a.grid(row = 13, column = 2, columnspan = 2)

lc9b = Checkbutton(frame, text = "The Yard 9th: B", variable = yard9bBool, indicatoron = 0)
lc9b.grid(row = 13, column = 4)

space9 = Label(frame).grid(row = 14, column = 2)

lc9c = Checkbutton(frame, text = "The Yard 9th: C", variable = yard9cBool, indicatoron = 0)
lc9c.grid(row = 15, column = 1)

lewisohn203a = Checkbutton(frame, text = "Lewisohn 203A", variable = lew203aBool, indicatoron = 0)
lewisohn203a.grid(row = 15, column = 2, columnspan = 2)

lewisohn203b = Checkbutton(frame, text = "Lewisohn 203B", variable = lew203bBool, indicatoron = 0)
lewisohn203b.grid(row = 15, column = 4)

space10 = Label(frame).grid(row = 16, column = 2)

lewisohn203d = Checkbutton(frame, text = "Lewisohn 203D", variable = lew203dBool, indicatoron = 0)
lewisohn203d.grid(row = 17, column = 1)

lewisohn203e = Checkbutton(frame, text = "Lewisohn 203E", variable = lew203eBool, indicatoron = 0)
lewisohn203e.grid(row = 17, column = 2, columnspan = 2)

lewisohn203f = Checkbutton(frame, text = "Lewisohn 203F", variable = lew203fBool, indicatoron = 0)
lewisohn203f.grid(row = 17, column = 4)

space11 = Label(frame).grid(row = 18, column = 2)

lewisohn203i = Checkbutton(frame, text = "Lewisohn 203I", variable = lew203iBool, indicatoron = 0)
lewisohn203i.grid(row = 19, column = 1)

lewisohn203k6 = Checkbutton(frame, text = "Lewisohn 203K-6", variable = lew203k6Bool, indicatoron = 0)
lewisohn203k6.grid(row = 19, column = 2, columnspan = 2)

lewisohn203k7 = Checkbutton(frame, text = "Lewisohn 203K-7", variable = lew203k7Bool, indicatoron = 0)
lewisohn203k7.grid(row = 19, column = 4)

space12 = Label(frame).grid(row = 20, column = 2)

lewisohn203n = Checkbutton(frame, text = "Lewisohn 203N", variable = lew203nBool, indicatoron = 0)
lewisohn203n.grid(row = 21, column = 1)

lewisohn203y = Checkbutton(frame, text = "Lewisohn 203Y", variable = lew203yBool, indicatoron = 0)
lewisohn203y.grid(row = 21, column = 2, columnspan = 2)

lewisohn203z = Checkbutton(frame, text = "Lewisohn 203Z", variable = lew203zBool, indicatoron = 0)
lewisohn203z.grid(row = 21, column = 4)

space13 = Label(frame).grid(row = 22, column = 2)

lewisohn214a = Checkbutton(frame, text = "Lewisohn 214A", variable = lew214aBool, indicatoron = 0)
lewisohn214a.grid(row = 23, column = 1)

lewisohn303a = Checkbutton(frame, text = "Lewisohn 303A", variable = lew303aBool, indicatoron = 0)
lewisohn303a.grid(row = 23, column = 2, columnspan = 2)

lewisohn303c = Checkbutton(frame, text = "Lewisohn 303C", variable = lew303cBool, indicatoron = 0)
lewisohn303c.grid(row = 23, column = 4)

space14 = Label(frame).grid(row = 24, column = 2)

lewisohn504a = Checkbutton(frame, text = "Lewisohn 504A", variable = lew504aBool, indicatoron = 0)
lewisohn504a.grid(row = 25, column = 1)

lewisohn504b = Checkbutton(frame, text = "Lewisohn 504B", variable = lew504bBool, indicatoron = 0)
lewisohn504b.grid(row = 25, column = 2, columnspan = 2)

lewisohn504c = Checkbutton(frame, text = "Lewisohn 504C", variable = lew504cBool, indicatoron = 0)
lewisohn504c.grid(row = 25, column = 4)

space15 = Label(frame).grid(row = 26, column = 2)

lewisohn504d = Checkbutton(frame, text = "Lewisohn 504D", variable = lew504dBool, indicatoron = 0)
lewisohn504d.grid(row = 27, column = 1)

lewisohn504f = Checkbutton(frame, text = "Lewisohn 504F", variable = lew504fBool, indicatoron = 0)
lewisohn504f.grid(row = 27, column = 2, columnspan = 2)

space16 = Label(frame).grid(row = 28, column = 2)
space17 = Label(frame).grid(row = 29, column = 2)

def main():
    unis = []
    unisTemp = str(enter.get())
    unisTemp = [x.strip() for x in unisTemp.split(',')]
    for i in unisTemp:
        unis.append(i.split())
    unis = reduce(add, unis)
    
    for i in unis:
        if "@columbia.edu" not in str(i):
            uni = i + "@columbia.edu"
        else:
            uni = i
        
        if 

submit = Button(frame, text = "Submit", command = main, width = 10, height = 3, font = ('Helvetica', '17'))
submit.grid(row = 30, column = 2, columnspan = 2)

mainloop()