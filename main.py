from multiprocessing import Pool, freeze_support
from tkinter import *
from functools import reduce
from operator import add
import changeUser as edit
import multiprocessing as mp
from functools import partial
import re
import time

def build():
    bColor1 = "#122d62"
    bColor2 = "#33cc33"
    fColor1 = "#ffffff"

    root = Tk()
    root.title("Google Calendar Access Permissions Editor")
    root.configure(bg = "lime")

    canvas = Canvas(root, scrollregion = (0, 0, 500, 500), bg = bColor1, highlightthickness = 0)
    canvas.grid(row = 0, column = 0, sticky = 'news')

    vbar = Scrollbar(canvas, orient = 'vertical', command = canvas.yview)
    vbar.grid(row = 0, column = 5, sticky = 'ens', rowspan = 100)
    canvas.configure(yscrollcommand = vbar.set)

    frame = Frame(canvas, bg = bColor1)
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

    

    buttons = [broadwayBool, yard9aBool, yard9bBool, yard9cBool, lew203aBool, lew203bBool, 
                lew203dBool, lew203eBool, lew203fBool, lew203iBool, lew203k6Bool, lew203k7Bool,
                lew203nBool, lew203yBool, lew203zBool, lew214aBool, lew303aBool,  lew303cBool, 
                lew504aBool, lew504bBool, lew504cBool, lew504dBool, lew504fBool]

    prompt1 = Label(frame, text = "Please enter the uni(s) you would like to change permissions for.", bg = bColor1, fg = fColor1)
    prompt1.grid(row = 0, column = 1, columnspan = 4)

    prompt2 = Label(frame, text = "Seperate multiple unis with spaces or commas.", bg = bColor1, fg = fColor1)
    prompt2.grid(row = 1, column = 1, columnspan = 4)

    space2 = Label(frame, bg = bColor1).grid(row = 2, column = 2)

    entry = Entry(frame, textvariable = enter)
    entry.grid(row = 3, column = 1, columnspan = 4)

    space3 = Label(frame, bg = bColor1).grid(row = 4, column = 2)
    space4 = Label(frame, bg = bColor1).grid(row = 5, column = 2)

    prompt3 = Label(frame, text = "Select whether to add or remove the user(s).", bg = bColor1, fg = fColor1)
    prompt3.grid(row = 6, column = 1, columnspan = 4)

    space5 = Label(frame, bg = bColor1).grid(row = 7, column = 2)

    plusButton = Radiobutton(frame, text = "Add User", variable = v, value = 1, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    plusButton.grid(row = 8, column = 2)

    minusButton = Radiobutton(frame, text = "Delete User", variable = v, value = 0, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    minusButton.grid(row = 8, column = 3)

    space6 = Label(frame, bg = bColor1).grid(row = 9, column = 2)
    space7 = Label(frame, bg = bColor1).grid(row = 10, column = 2)

    prompt4 = Label(frame, text = "Select which conference rooms to add the user(s) to.", bg = bColor1, fg = fColor1)
    prompt4.grid(row = 11, column = 1, columnspan = 4)

    space8 = Label(frame, bg = bColor1).grid(row = 12, column = 2)

    b2875 = Checkbutton(frame, text = "2875 Broadway", variable = broadwayBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    b2875.grid(row =13, column = 1)

    lc9a = Checkbutton(frame, text = "The Yard 9th: A", variable = yard9aBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lc9a.grid(row = 13, column = 2, columnspan = 2)

    lc9b = Checkbutton(frame, text = "The Yard 9th: B", variable = yard9bBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lc9b.grid(row = 13, column = 4)

    space9 = Label(frame, bg = bColor1).grid(row = 14, column = 2)

    lc9c = Checkbutton(frame, text = "The Yard 9th: C", variable = yard9cBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lc9c.grid(row = 15, column = 1)

    lewisohn203a = Checkbutton(frame, text = "Lewisohn 203A", variable = lew203aBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203a.grid(row = 15, column = 2, columnspan = 2)

    lewisohn203b = Checkbutton(frame, text = "Lewisohn 203B", variable = lew203bBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203b.grid(row = 15, column = 4)

    space10 = Label(frame, bg = bColor1).grid(row = 16, column = 2)

    lewisohn203d = Checkbutton(frame, text = "Lewisohn 203D", variable = lew203dBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203d.grid(row = 17, column = 1)

    lewisohn203e = Checkbutton(frame, text = "Lewisohn 203E", variable = lew203eBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203e.grid(row = 17, column = 2, columnspan = 2)

    lewisohn203f = Checkbutton(frame, text = "Lewisohn 203F", variable = lew203fBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203f.grid(row = 17, column = 4)

    space11 = Label(frame, bg = bColor1).grid(row = 18, column = 2)

    lewisohn203i = Checkbutton(frame, text = "Lewisohn 203I", variable = lew203iBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203i.grid(row = 19, column = 1)

    lewisohn203k6 = Checkbutton(frame, text = "Lewisohn 203K-6", variable = lew203k6Bool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203k6.grid(row = 19, column = 2, columnspan = 2)

    lewisohn203k7 = Checkbutton(frame, text = "Lewisohn 203K-7", variable = lew203k7Bool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203k7.grid(row = 19, column = 4)

    space12 = Label(frame, bg = bColor1).grid(row = 20, column = 2)

    lewisohn203n = Checkbutton(frame, text = "Lewisohn 203N", variable = lew203nBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203n.grid(row = 21, column = 1)

    lewisohn203y = Checkbutton(frame, text = "Lewisohn 203Y", variable = lew203yBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203y.grid(row = 21, column = 2, columnspan = 2)

    lewisohn203z = Checkbutton(frame, text = "Lewisohn 203Z", variable = lew203zBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn203z.grid(row = 21, column = 4)

    space13 = Label(frame, bg = bColor1).grid(row = 22, column = 2)

    lewisohn214a = Checkbutton(frame, text = "Lewisohn 214A", variable = lew214aBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn214a.grid(row = 23, column = 1)

    lewisohn303a = Checkbutton(frame, text = "Lewisohn 303A", variable = lew303aBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn303a.grid(row = 23, column = 2, columnspan = 2)

    lewisohn303c = Checkbutton(frame, text = "Lewisohn 303C", variable = lew303cBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn303c.grid(row = 23, column = 4)

    space14 = Label(frame, bg = bColor1).grid(row = 24, column = 2)

    lewisohn504a = Checkbutton(frame, text = "Lewisohn 504A", variable = lew504aBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn504a.grid(row = 25, column = 1)

    lewisohn504b = Checkbutton(frame, text = "Lewisohn 504B", variable = lew504bBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn504b.grid(row = 25, column = 2, columnspan = 2)

    lewisohn504c = Checkbutton(frame, text = "Lewisohn 504C", variable = lew504cBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn504c.grid(row = 25, column = 4)

    space15 = Label(frame, bg = bColor1).grid(row = 26, column = 2)

    lewisohn504d = Checkbutton(frame, text = "Lewisohn 504D", variable = lew504dBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn504d.grid(row = 27, column = 1)

    lewisohn504f = Checkbutton(frame, text = "Lewisohn 504F", variable = lew504fBool, indicatoron = 0, bg = bColor1, fg = fColor1, selectcolor = bColor2)
    lewisohn504f.grid(row = 27, column = 2, columnspan = 2)

    space16 = Label(frame, bg = bColor1).grid(row = 28, column = 2)
    space17 = Label(frame, bg = bColor1).grid(row = 29, column = 2)

    select = partial(selectAll, buttons)
    sAll = Button(frame, text = "Select All Toggle Switch", command = select, bg = bColor1, fg = fColor1)
    sAll.grid(row = 30, column = 2, columnspan = 2)

    space17 = Label(frame, bg = bColor1).grid(row = 31, column = 2)
    space18 = Label(frame, bg = bColor1).grid(row = 32, column = 2)

    action = partial(parallel, broadwayBool, yard9aBool, yard9bBool, yard9cBool, lew203aBool, lew203bBool,
                        lew203dBool, lew203eBool, lew203fBool, lew203iBool, lew203k6Bool, lew203k7Bool,
                        lew203nBool, lew203yBool, lew203zBool, lew214aBool, lew303aBool, lew303cBool,
                        lew504aBool, lew504bBool, lew504cBool, lew504dBool, lew504fBool, v, enter,
                        root)

    submit = Button(frame, text = "Submit", command = action, width = 10, height = 3, font = ('Helvetica', '17'), bg = bColor1, fg = fColor1)
    submit.grid(row = 33, column = 2, columnspan = 2)

    mainloop()

def main(info):
    try:    
        if info[2] == 1:
            edit.add(str(info[0]), str(info[1]))
            #print(str(info[0]), str(info[1]), info[2])

        elif info[2] == 0:
            edit.delete(str(info[0]), str(info[1]))
            #print(str(info[0]), str(info[1]), info[2])

        return(["yes", info[3]])

    except Exception as ex:
        return([ex, info[3]])

def parallel(broadwayBool, yard9aBool, yard9bBool, yard9cBool, lew203aBool, lew203bBool,
                lew203dBool, lew203eBool, lew203fBool, lew203iBool, lew203k6Bool, lew203k7Bool,
                lew203nBool, lew203yBool, lew203zBool, lew214aBool, lew303aBool, lew303cBool,
                lew504aBool, lew504bBool, lew504cBool, lew504dBool, lew504fBool, v, enter, root):
    bColor1 = "#122d62"
    bColor2 = "#33cc33"
    fColor1 = "#ffffff"
    check = False
    
    #All calendar IDs
    broadway = 'columbia.edu_3634343538303339393332@resource.calendar.google.com'
    yard9a = 'columbia.edu_1886rf4mc1mfag6kghp73f2fttf5i6gb6os30e1m6ko38dhn68@resource.calendar.google.com'
    yard9b = 'columbia.edu_1880mgrd7sf92glaj469rmeah1t1u6gb6orjic9o6cs3ed1o68@resource.calendar.google.com'
    yard9c  = 'columbia.edu_188el4hr2ok5minflnjojhgapfuga6gb6orjgd9k68pjgcpg6c@resource.calendar.google.com'
    lew203a = 'columbia.edu_35343032323839342d363935@resource.calendar.google.com'
    lew203b = 'columbia.edu_1884n0i2dkfgmi32isqpcealde0b86gb6kp36dhl60r3cd9k64@resource.calendar.google.com'
    lew203d = 'columbia.edu_3532353238343634393731@resource.calendar.google.com'
    lew203e = 'columbia.edu_1886ghk841pv6hftl62d73rd3675o6gb6kp3cc9g68p38c9m6o@resource.calendar.google.com'
    lew203f = 'columbia.edu_18813q25q6djqgfslqaeauismuv9o6g96kp3ed1o60qj2e0@resource.calendar.google.com'
    lew203i = 'columbia.edu_1884cst50kde2g3vmdci2rqh09gl06gb6kpj0e1n74pjed1p6c@resource.calendar.google.com'
    lew203k6 = 'columbia.edu_188c1aq7s485qgu0hg5jd0hmcip6g6gb6sp36d9k74sj8d9m6o@resource.calendar.google.com'
    lew203k7 = 'columbia.edu_1885n4lramp88hndl93qf9gfhotpi6gb6sp34e9n74p32dhm74@resource.calendar.google.com'
    lew203n = 'columbia.edu_188cdrv99d5hsj9mlb470edcu214e6gb6kpjac9p6os36d9h60@resource.calendar.google.com'
    lew203y = 'columbia.edu_3534363133303738373435@resource.calendar.google.com'
    lew203z = 'columbia.edu_3534373434303839393134@resource.calendar.google.com'
    lew214a = 'columbia.edu_35333233343630372d333234@resource.calendar.google.com'
    lew303a = 'columbia.edu_313935343339302d393131@resource.calendar.google.com'
    lew303c = 'columbia.edu_333135393838313532@resource.calendar.google.com'
    lew504a = 'columbia.edu_3934343437373831353937@resource.calendar.google.com'
    lew504b = 'columbia.edu_3934353736353031323032@resource.calendar.google.com'
    lew504c = 'columbia.edu_393436313334353532@resource.calendar.google.com'
    lew504d = 'columbia.edu_39343733343433372d3431@resource.calendar.google.com'
    lew504f = 'columbia.edu_39343935353630382d323730@resource.calendar.google.com'

    rooms = [(broadwayBool.get(),broadway,"2875 Broadway"), 
                (yard9aBool.get(),yard9a,"The Yard 9A"),                
                (yard9bBool.get(),yard9b, "The Yard 9B"), 
                (yard9cBool.get(),yard9c, "The Yard 9C"), 
                (lew203aBool.get(),lew203a, "Lewisohn 203A"), 
                (lew203bBool.get(),lew203b, "Lewisohn 203B"), 
                (lew203dBool.get(),lew203d, "Lewisohn 203D"), 
                (lew203eBool.get(),lew203e, "Lewisohn 203E"), 
                (lew203fBool.get(),lew203f, "Lewisohn 203F"), 
                (lew203iBool.get(),lew203i, "Lewisohn 203I"), 
                (lew203k6Bool.get(),lew203k6, "Lewisohn 203K-6"), 
                (lew203k7Bool.get(),lew203k7, "Lewisohn 203K-7"), 
                (lew203nBool.get(),lew203n, "Lewisohn 203N"), 
                (lew203yBool.get(),lew203y, "Lewisohn 203Y"), 
                (lew203zBool.get(),lew203z, "Lewisohn 203Z"), 
                (lew214aBool.get(),lew214a, "Lewisohn 214A"), 
                (lew303aBool.get(),lew303a, "Lewisohn 303A"), 
                (lew303cBool.get(),lew303c, "Lewisohn 303C"), 
                (lew504aBool.get(),lew504a, "Lewisohn 504A"), 
                (lew504bBool.get(),lew504b, "Lewisohn 504B"), 
                (lew504cBool.get(),lew504c, "Lewisohn 504C"), 
                (lew504dBool.get(),lew504d, "Lewisohn 504D"),
                (lew504fBool.get(),lew504f, "Lewisohn 504F")]

    unis = []
    final = []

    unisTemp = str(enter.get())
    unisTemp = [x.strip() for x in unisTemp.split(',')]

    for i in unisTemp:
        unis.append(i.split())
    unis = reduce(add, unis)
    
    for i in unis:
        if "@columbia.edu" not in str(i) and "@gmail.com" not in str(i) and "@hotmail.com" not in str(i):
            uni = i + "@columbia.edu"
        else:
            uni = i

        for j in range(len(rooms)):
                if rooms[j][0] == 1:
                    final.append([uni, rooms[j][1], v.get(), rooms[j][2]])

    with Pool(mp.cpu_count()) as p:
        records = p.map(main, final)
        p.terminate()
        p.join()

    window = Toplevel(root, bg = bColor1)
    for i in range(len(records)):
        if records[i][0] != "yes":
            spaces0 = Label(window, bg = bColor1).grid(row = 0 + i)
            display1 = Label(window, text = "Finished but with errors...", bg = bColor1, fg = fColor1)
            display1.grid(row = 1 + i)

            spaces1 = Label(window, bg = bColor1).grid(row = 2 + i)
            display2 = Label(window, text = records[i][0], bg = bColor1, fg = fColor1)
            display2.grid(row = 3 + i)

            spaces2= Label(window, bg = bColor1).grid(row = 3)
            display3 = Label(window, text = records[i][1], bg = bColor1, fg = fColor1)
            display3.grid(row = 4 + i)

        else:
            display1 = Label(window, text = "Finished!", font = ('Helvetica', '17'), bg = bColor1, fg = fColor1)
            display1.grid(row = 1, columnspan = 3)

def selectAll(buttons):
    for item in buttons:
        if item.get():
            item.set(0)
        else:
            item.set(1)

if __name__ == "__main__":
    freeze_support()
    build()