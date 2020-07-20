from multiprocessing import Pool, freeze_support
from tkinter import *
from functools import reduce
from operator import add
import changeUser as edit
import multiprocessing as mp
from functools import partial
import re
import time

#All calendar IDs
newDict = {
    '2875 Broadway' : 'columbia.edu_3634343538303339393332@resource.calendar.google.com',
    'The Yard 9A' : 'columbia.edu_1886rf4mc1mfag6kghp73f2fttf5i6gb6os30e1m6ko38dhn68@resource.calendar.google.com',
    'The Yard 9B' : 'columbia.edu_1880mgrd7sf92glaj469rmeah1t1u6gb6orjic9o6cs3ed1o68@resource.calendar.google.com',
    'The Yard 9C' : 'columbia.edu_188el4hr2ok5minflnjojhgapfuga6gb6orjgd9k68pjgcpg6c@resource.calendar.google.com',
    'Lewisohn 203A' : 'columbia.edu_35343032323839342d363935@resource.calendar.google.com',
    'Lewisohn 203B' : 'columbia.edu_1884n0i2dkfgmi32isqpcealde0b86gb6kp36dhl60r3cd9k64@resource.calendar.google.com',
    'Lewisohn 203D' : 'columbia.edu_3532353238343634393731@resource.calendar.google.com',
    'Lewisohn 203E' : 'columbia.edu_1886ghk841pv6hftl62d73rd3675o6gb6kp3cc9g68p38c9m6o@resource.calendar.google.com',
    'Lewisohn 203F' : 'columbia.edu_18813q25q6djqgfslqaeauismuv9o6g96kp3ed1o60qj2e0@resource.calendar.google.com',
    'Lewisohn 203I' : 'columbia.edu_1884cst50kde2g3vmdci2rqh09gl06gb6kpj0e1n74pjed1p6c@resource.calendar.google.com',
    'Lewisohn 203K-6' : 'columbia.edu_188c1aq7s485qgu0hg5jd0hmcip6g6gb6sp36d9k74sj8d9m6o@resource.calendar.google.com',
    'Lewisohn 203K-7' : 'columbia.edu_1885n4lramp88hndl93qf9gfhotpi6gb6sp34e9n74p32dhm74@resource.calendar.google.com',
    'Lewisohn 203N' : 'columbia.edu_188cdrv99d5hsj9mlb470edcu214e6gb6kpjac9p6os36d9h60@resource.calendar.google.com',
    'Lewisohn 203Y' : 'columbia.edu_3534363133303738373435@resource.calendar.google.com',
    'Lewisohn 203Z' : 'columbia.edu_3534373434303839393134@resource.calendar.google.com',
    'Lewisohn 214A' : 'columbia.edu_35333233343630372d333234@resource.calendar.google.com',
    'Lewisohn 303A' : 'columbia.edu_313935343339302d393131@resource.calendar.google.com',
    'Lewisohn 303C' : 'columbia.edu_333135393838313532@resource.calendar.google.com',
    'Lewisohn 504A' : 'columbia.edu_3934343437373831353937@resource.calendar.google.com',
    'Lewisohn 504B' : 'columbia.edu_3934353736353031323032@resource.calendar.google.com',
    'Lewisohn 504C' : 'columbia.edu_393436313334353532@resource.calendar.google.com',
    'Lewisohn 504D' : 'columbia.edu_39343733343433372d3431@resource.calendar.google.com',
    'Lewisohn 504F' : 'columbia.edu_39343935353630382d323730@resource.calendar.google.com',
    'Lewisohn 203.3' : 'columbia.edu_188dlk63ma0akg5unmvgkn43inb6q6gb64pjadpk6ko3acpi60@resource.calendar.google.com',
    'Lewisohn 203.3.2' : 'columbia.edu_1880oaobslh32ipck6iffvubdaleq@resource.calendar.google.com',
    'Lewisohn 203.4' : 'columbia.edu_1888m15lnejvsgunm92k0fhudk3ns6gb70o34d1h6ss38d1m60@resource.calendar.google.com',
    'Lewisohn 203.6' : 'columbia.edu_188bk3blna4cei5imtndensvomege6gb74ojccho70oj6dpi60@resource.calendar.google.com',
    'Lewisohn 203.7' : 'columbia.edu_1880jsfmm7er2j81huvtde7lcsp9a6ga68ojacho70r34e9n@resource.calendar.google.com',
    'Lewisohn 504.1' : 'columbia.edu_18889cge37182h4dlhno07mhsbrhu6gb6ks3idpo64pjae9m68@resource.calendar.google.com',
    'Lewisohn 504.2' : 'columbia.edu_18855soespk0mjvbnkalccoa9l7n46ga6cq3gd1g60o32dhn@resource.calendar.google.coms',
    'Lewisohn 504.3' : 'columbia.edu_1889f7lel2udah5rnff5ki9u8lmhm6ga64oj4e1n6osjgc9g@resource.calendar.google.com',
    'Lewisohn 504.4' : 'columbia.edu_18810hagnega6j6djosj53k6t6gi86gb74p3cdhg6gr3gcpl70@resource.calendar.google.com',
}

def build():
    bColor1 = "#122d62"
    bColor2 = "#33cc33"
    fColor1 = "#ffffff"

    root = Tk()
    root.title("Google Calendar Access Permissions Editor")
    root.configure(bg = "lime")
    root.geometry("+600+25")

    canvas = Canvas(root, scrollregion = (0, 0, 500, 500), bg = bColor1, highlightthickness = 0)
    canvas.grid(row = 0, column = 0, sticky = 'news')

    vbar = Scrollbar(canvas, orient = 'vertical', command = canvas.yview)
    vbar.grid(row = 0, column = 5, sticky = 'ens', rowspan = 100)
    canvas.configure(yscrollcommand = vbar.set)

    frame = Frame(canvas, bg = bColor1)
    frame.grid(row = 0, column = 0, sticky = "news", padx = 30, pady = 30)

    #Create 'empty' arrays to contain the dynamically generated buttons
    allRadio = []
    allCheck = []
    allBool = []

    enter = StringVar()
    v = IntVar()
    v.set(3)
    r = IntVar()

    #First Set of Instructions
    prompt1 = Label(frame, text = "Please enter the uni(s) you would like to change permissions for.", 
                    bg = bColor1, fg = fColor1)
    prompt1.grid(row = 0, column = 1, columnspan = 4)

    prompt2 = Label(frame, text = "Seperate multiple unis with spaces or commas.", bg = bColor1, 
                    fg = fColor1)
    prompt2.grid(row = 1, column = 1, columnspan = 4)

    #Listbox to list users for each calendar
    space1 = Label(frame, text = "      ", bg = bColor1).grid(row = 1, rowspan = 50, column = 5)
    listbox = Listbox(frame, width = 40, yscrollcommand = vbar.set)
    listbox.insert(END, "Shandao sucks and is one of them")
    listbox.grid(row = 1, rowspan = 50, column = 6, sticky = "news")

    vbar.config(command = listbox.yview)

    space2 = Label(frame, bg = bColor1).grid(row = 2, column = 2)

    #Email entry
    entry = Entry(frame, textvariable = enter)
    entry.grid(row = 3, column = 1, columnspan = 4)

    space3 = Label(frame, bg = bColor1).grid(row = 4, column = 2)
    space4 = Label(frame, bg = bColor1).grid(row = 5, column = 2)

    #Decide whether to add, delete, or list users for a calendar
    prompt3 = Label(frame, text = "Select whether to add, remove, or list the user(s).", 
                    bg = bColor1, fg = fColor1)
    prompt3.grid(row = 6, column = 1, columnspan = 4)

    space5 = Label(frame, bg = bColor1).grid(row = 7, column = 2)

    space6 = Label(frame, bg = bColor1).grid(row = 9, column = 2)
    space7 = Label(frame, bg = bColor1).grid(row = 10, column = 2)

    prompt4 = Label(frame, text = "Select which conference rooms to configure.", 
                    bg = bColor1, fg = fColor1)
    prompt4.grid(row = 11, column = 1, columnspan = 4)

    space8 = Label(frame, bg = bColor1).grid(row = 12, column = 2)

    #Conference Rooms as Radio Buttons and Checkbuttons (Default)
    mainRow = 13
    col = 1
    for index, key in enumerate(newDict):
        allBool.append(IntVar())
        if col == 1:
            allRadio.append(Radiobutton(frame, text = key, variable = r, value = index+1, indicatoron = 0,
            bg = bColor1, fg = fColor1, selectcolor = bColor2, command = partial(userList, listbox, v, key, newDict[key])))
            
            allCheck.append(Checkbutton(frame, text = key, variable = allBool[index], indicatoron = 0, 
            bg = bColor1, fg = fColor1, selectcolor = bColor2))
            allCheck[index].grid(row = mainRow, column = col)

            col += 1

        elif col == 2:
            allRadio.append(Radiobutton(frame, text = key, variable = r, value = index+1, indicatoron = 0,
            bg = bColor1, fg = fColor1, selectcolor = bColor2, command = partial(userList, listbox, v, key, newDict[key])))
            
            allCheck.append(Checkbutton(frame, text = key, variable = allBool[index], indicatoron = 0, 
            bg = bColor1, fg = fColor1, selectcolor = bColor2))
            allCheck[index].grid(row = mainRow, column = col)

            col += 1

        elif col ==3:
            allRadio.append(Radiobutton(frame, text = key, variable = r, value = index+1, indicatoron = 0,
            bg = bColor1, fg = fColor1, selectcolor = bColor2, command = partial(userList, listbox, v, key, newDict[key])))
            
            allCheck.append(Checkbutton(frame, text = key, variable = allBool[index], indicatoron = 0, 
            bg = bColor1, fg = fColor1, selectcolor = bColor2))
            allCheck[index].grid(row = mainRow, column = col)

            col += 1

        elif col == 4:
            allRadio.append(Radiobutton(frame, text = key, variable = r, value = index+1, indicatoron = 0,
            bg = bColor1, fg = fColor1, selectcolor = bColor2, command = partial(userList, listbox, v, key, newDict[key])))
            
            allCheck.append(Checkbutton(frame, text = key, variable = allBool[index], indicatoron = 0, 
            bg = bColor1, fg = fColor1, selectcolor = bColor2))
            allCheck[index].grid(row = mainRow, column = col)

            mainRow += 1
            spaceRadio = Label(frame, bg = bColor1)
            spaceRadio.grid(row = mainRow, column = col)

            spaceCheck = Label(frame, bg = bColor1)
            spaceCheck.grid(row = mainRow, column = col)

            mainRow += 1
            col = 1

    mainRow += 1 #row (cal/3) + 1

    #Select All Toggle Button
    space16 = Label(frame, bg = bColor1).grid(row = mainRow, column = 2)
    mainRow += 1
    space17 = Label(frame, bg = bColor1).grid(row = mainRow, column = 2)
    mainRow +=1

    select = partial(selectAll, allBool)
    sAll = Button(frame, text = "Select All Toggle Switch", command = select, bg = bColor1, fg = fColor1)
    sAll.grid(row = mainRow, column = 2, columnspan = 2)
    mainRow += 1

    #Submit Button
    space18 = Label(frame, bg = bColor1).grid(row = mainRow, column = 2)
    mainRow += 1
    space19 = Label(frame, bg = bColor1).grid(row = mainRow, column = 2)
    mainRow += 1

    action = partial(parallel, v, enter, root, allBool)

    submit = Button(frame, text = "Submit", command = action, width = 10, height = 3, 
                    font = ('Helvetica', '17'), bg = bColor1, fg = fColor1)
    submit.grid(row = mainRow, column = 2, columnspan = 2)

    #Dynamic Listing commands
    userAction = partial(userList, listbox, v, newDict)

    submitAction1 = partial(addSubmit, frame, submit, sAll, allRadio, allCheck, mainRow)

    submitAction2 = partial(removeSubmit, frame, submit, sAll, allRadio, allCheck)

    plusButton = Radiobutton(frame, text = "Add User", variable = v, value = 1, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = submitAction1)
    plusButton.grid(row = 8, column = 1)

    minusButton = Radiobutton(frame, text = "Delete User", variable = v, value = 0, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = submitAction1)
    minusButton.grid(row = 8, column = 2, columnspan = 2)

    listButton = Radiobutton(frame, text = "List Users", variable = v, value = 2, indicatoron = 0,
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = submitAction2)
    listButton.grid(row = 8, column = 4)

    mainloop()

def addSubmit(frame, submit, sAll, allRadio, allCheck, mainRow):
    submit.grid(row = mainRow, column = 2, columnspan = 2)
    sAll.grid(row = mainRow - 3, column = 2, columnspan = 2)

    for radioButton in allRadio:
        radioButton.grid_forget()

    row = 13
    col = 1
    for checkButton in allCheck:
        if col == 1:
            checkButton.grid(row = row, column = col)
            col += 1
        elif col == 2:
            checkButton.grid(row = row, column = col)
            col += 1
        elif col ==3:
            checkButton.grid(row = row, column = col)
            col += 1
        elif col == 4:
            checkButton.grid(row = row, column = col)
            row += 2
            col = 1

def removeSubmit(frame, submit, sAll, allRadio, allCheck):
    submit.grid_forget()
    sAll.grid_forget()

    for checkButton in allCheck:
        checkButton.grid_forget()
 
    row = 13
    col = 1
    for radioButton in allRadio:
        if col == 1:
            radioButton.grid(row = row, column = col)
            col += 1
        elif col == 2:
            radioButton.grid(row = row, column = col)
            col += 1
        elif col == 3:
            radioButton.grid(row = row, column = col)
            col += 1
        elif col == 4:
            radioButton.grid(row = row, column = col)
            row += 2
            col = 1

def userList(listbox, v, name, cal):
    if v.get() == 2:
        listbox.delete(0, END)
        listbox.insert(END, name)
        
        users = edit.listUser(cal)

        for i in range(len(users)):
            if i == 0:
                continue
            else:
                user = users[i]
                listbox.insert(END, user[5:])
                
def main(info):
    #listing = []

    try:    
        if info[2] == 1:
            edit.add(str(info[0]), str(info[1]))
            #print(str(info[0]), str(info[1]), info[2])
            return(["yes", info[3]])

        elif info[2] == 0:
            edit.delete(str(info[0]), str(info[1]))
            #print(str(info[0]), str(info[1]), info[2])
            return(["yes", info[3]])

    except Exception as ex:
        error = str(ex).split("returned")[1]
        if "Rate Limit Exceeded" in error:
            time.sleep(5)
            main(info)
        else:
            return([error, info[0], info[3]])

def parallel(v, enter, root, allBool):
    bColor1 = "#122d62"
    bColor2 = "#33cc33"
    fColor1 = "#ffffff"

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

        #for j in range(len(allBool)):
        for index, key in enumerate(newDict):
            if allBool[index].get() == 1:
                final.append([uni, newDict[key], v.get(), key])

    with Pool(mp.cpu_count()) as p:
        records = p.map(main, final)
        p.terminate()
        p.join()

    window = Toplevel(root, bg = bColor1)
    window.geometry("500x500+600+50")
    newCanvas = Canvas(window, scrollregion = (0, 0, 500, 500), bg = bColor1, highlightthickness = 0)
    newCanvas.grid(row = 0, column = 0, sticky = 'news')
    newCanvas.grid_rowconfigure(0, weight = 1)
    newCanvas.grid_columnconfigure(0, weight = 1)
    window.grid_rowconfigure(0, weight = 1)
    window.grid_columnconfigure(0, weight = 1)

    errorBool = False
    for i in range(len(records)):
        if records[i][0] != "yes" and records[i][0] != "list":
            errorBool = True
            spaces0 = Label(newCanvas, bg = bColor1).grid(row = 0 + (7 * i))
            display1 = Label(newCanvas, text = "Finished but with errors...", bg = bColor1, fg = fColor1)
            display1.grid(row = 1 + (7 * i))

            spaces1 = Label(newCanvas, bg = bColor1).grid(row = 2 + (7 * i))
            display2 = Label(newCanvas, text = records[i][0], bg = bColor1, fg = fColor1)
            display2.grid(row = 3 + (7 * i))

            spaces2 = Label(newCanvas, bg = bColor1).grid(row = 4 + (7 * i))
            display3 = Label(newCanvas, text = records[i][1], bg = bColor1, fg = fColor1)
            display3.grid(row = 5 + (7 * i))

            spaces3 = Label(newCanvas, bg = bColor1).grid(row = 6 + (7 * i))
            display4 = Label(newCanvas, text = records[i][2], bg = bColor1, fg = fColor1)
            display4.grid(row = 7 + (7 * i))

    if errorBool == False:
        display1 = Label(newCanvas, text = "Finished!", font = ('Helvetica', '17'), bg = bColor1, fg = fColor1)
        display1.grid(row = 0, rowspan = 3, column = 0, columnspan = 3, sticky = "news")

def selectAll(buttons):
    for item in buttons:
        if item.get():
            item.set(0)
        else:
            item.set(1)

if __name__ == "__main__":
    freeze_support()
    build()