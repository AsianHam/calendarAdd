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
lew2033 = 'columbia.edu_188dlk63ma0akg5unmvgkn43inb6q6gb64pjadpk6ko3acpi60@resource.calendar.google.com'
lew20332 = 'columbia.edu_1880oaobslh32ipck6iffvubdaleq@resource.calendar.google.com'
lew2034 = 'columbia.edu_1888m15lnejvsgunm92k0fhudk3ns6gb70o34d1h6ss38d1m60@resource.calendar.google.com'
lew2036 = 'columbia.edu_188bk3blna4cei5imtndensvomege6gb74ojccho70oj6dpi60@resource.calendar.google.com'
lew2037 = 'columbia.edu_1880jsfmm7er2j81huvtde7lcsp9a6ga68ojacho70r34e9n@resource.calendar.google.com'
lew5041 = 'columbia.edu_18889cge37182h4dlhno07mhsbrhu6gb6ks3idpo64pjae9m68@resource.calendar.google.com'
lew5042 = 'columbia.edu_18855soespk0mjvbnkalccoa9l7n46ga6cq3gd1g60o32dhn@resource.calendar.google.coms'
lew5043 = 'columbia.edu_1889f7lel2udah5rnff5ki9u8lmhm6ga64oj4e1n6osjgc9g@resource.calendar.google.com'
lew5044 = 'columbia.edu_18810hagnega6j6djosj53k6t6gi86gb74p3cdhg6gr3gcpl70@resource.calendar.google.com'

broadwayBool, yard9aBool, yard9bBool = IntVar(), IntVar(), IntVar()
yard9cBool, lew203aBool, lew203bBool = IntVar(), IntVar(), IntVar()
lew203dBool, lew203eBool, lew203fBool = IntVar(), IntVar(), IntVar()
lew203iBool, lew203k6Bool, lew203k7Bool = IntVar(), IntVar(), IntVar()
lew203nBool, lew203yBool, lew203zBool = IntVar(), IntVar(), IntVar()
lew214aBool, lew303aBool,  lew303cBool = IntVar(), IntVar(), IntVar()
lew504aBool, lew504bBool, lew504cBool = IntVar(), IntVar(), IntVar()
lew504dBool, lew504fBool, lew2033Bool = IntVar(), IntVar(), IntVar()
lew20332Bool, lew2034Bool, lew2036Bool = IntVar(), IntVar(), IntVar()
lew2037Bool, lew5041Bool, lew5042Bool = IntVar(), IntVar(), IntVar()
lew5041Bool, lew5042Bool ,lew5043Bool = IntVar(), IntVar(), IntVar() 
lew5044Bool = IntVar()

allCal = [broadway, yard9a, yard9b, yard9c, lew203a, lew203b, lew203d, lew203e, lew203f, lew203i,\
            lew203k6, lew203k7, lew203n, lew203y, lew203z, lew214a, lew303a, lew303c, lew504a, lew504b,\
            lew504c, lew504d, lew504f, lew2033, lew20332, lew2034, lew2036, lew2037, lew5041, lew5042,\ 
            lew5043, lew5044]

allBool = [broadwayBool, yard9aBool, yard9bBool, yard9cBool, lew203aBool, lew203bBool, lew203dBool,\ 
            lew203eBool, lew203fBool, lew203iBool, lew203k6Bool, lew203k7Bool, lew203nBool, lew203yBool,\ 
            lew203zBool, lew214aBool, lew303aBool,  lew303cBool, lew504aBool, lew504bBool, lew504cBool,\
            lew504dBool, lew504fBool, lew2033Bool, lew20332Bool, lew2034Bool, lew2036Bool, lew2037Bool,\ 
            lew5041Bool, lew5042Bool, lew5041Bool, lew5042Bool, lew5043Bool, lew5044Bool]

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

    enter = StringVar()
    v = IntVar()
    v.set(3)
    r = IntVar()

    b2875Radio, lc9aRadio = Radiobutton(frame), Radiobutton(frame)
    lc9bRadio, lc9cRadio = Radiobutton(frame), Radiobutton(frame)
    lewisohn203aRadio, lewisohn203bRadio = Radiobutton(frame), Radiobutton(frame)
    lewisohn203dRadio, lewisohn203eRadio = Radiobutton(frame), Radiobutton(frame)
    lewisohn203fRadio, lewisohn203iRadio = Radiobutton(frame), Radiobutton(frame)
    lewisohn203k6Radio, lewisohn203k7Radio = Radiobutton(frame), Radiobutton(frame)
    lewisohn203nRadio, lewisohn203yRadio = Radiobutton(frame), Radiobutton(frame)
    lewisohn203zRadio, lewisohn214aRadio = Radiobutton(frame), Radiobutton(frame)
    lewisohn303aRadio, lewisohn303cRadio = Radiobutton(frame), Radiobutton(frame)
    lewisohn504aRadio, lewisohn504bRadio = Radiobutton(frame), Radiobutton(frame)
    lewisohn504cRadio, lewisohn504dRadio = Radiobutton(frame), Radiobutton(frame)
    lewisohn504fRadio = Radiobutton(frame)

    buttons = [broadwayBool, yard9aBool, yard9bBool, yard9cBool, lew203aBool, lew203bBool, 
                lew203dBool, lew203eBool, lew203fBool, lew203iBool, lew203k6Bool, lew203k7Bool,
                lew203nBool, lew203yBool, lew203zBool, lew214aBool, lew303aBool,  lew303cBool, 
                lew504aBool, lew504bBool, lew504cBool, lew504dBool, lew504fBool]

    #Listbox to list users for each calendar
    space1 = Label(frame, text = "      ", bg = bColor1).grid(row = 1, rowspan = 50, column = 5)
    listbox = Listbox(frame, width = 40, yscrollcommand = vbar.set)
    listbox.insert(END, "Shandao sucks and is one of them")
    listbox.grid(row = 1, rowspan = 50, column = 6, sticky = "news")

    vbar.config(command = listbox.yview)

    #Dynamic Listing commands
    b2875Action = partial(userList, listbox, v, broadway)
    yard9aAction = partial(userList, listbox, v, yard9a)
    yard9bAction = partial(userList, listbox, v, yard9b)
    yard9cAction = partial(userList, listbox, v, yard9c)
    lew203aAction = partial(userList, listbox, v, lew203a)
    lew203bAction = partial(userList, listbox, v, lew203b)
    lew203dAction = partial(userList, listbox, v, lew203d)
    lew203eAction = partial(userList, listbox, v, lew203e)
    lew203fAction = partial(userList, listbox, v, lew203f)
    lew203iAction = partial(userList, listbox, v, lew203i)
    lew203k6Action = partial(userList, listbox, v, lew203k6)
    lew203k7Action = partial(userList, listbox, v, lew203k7)
    lew203nAction = partial(userList, listbox, v, lew203n)
    lew203yAction = partial(userList, listbox, v, lew203y)
    lew203zAction = partial(userList, listbox, v, lew203z)
    lew214aAction = partial(userList, listbox, v, lew214a)
    lew303aAction = partial(userList, listbox, v, lew303a)
    lew303cAction = partial(userList, listbox, v, lew303c)
    lew504aAction = partial(userList, listbox, v, lew504a)
    lew504bAction = partial(userList, listbox, v, lew504b)
    lew504cAction = partial(userList, listbox, v, lew504c)
    lew504dAction = partial(userList, listbox, v, lew504d)
    lew504fAction = partial(userList, listbox, v, lew504f)

    #Conference Rooms as Radio Buttons
    b2875Radio = Radiobutton(frame, text = "2875 Broadway", variable = r, value = 1, indicatoron = 0, 
                        bg = bColor1, fg = fColor1, selectcolor = bColor2, command = b2875Action)

    lc9aRadio = Radiobutton(frame, text = "The Yard 9th: A", variable = r, value = 2, indicatoron = 0, 
                        bg = bColor1, fg = fColor1, selectcolor = bColor2, command = yard9aAction)

    lc9bRadio = Radiobutton(frame, text = "The Yard 9th: B", variable = r, value = 3, indicatoron = 0, 
                        bg = bColor1, fg = fColor1, selectcolor = bColor2, command = yard9bAction)

    space9Radio = Label(frame, bg = bColor1).grid(row = 14, column = 2)

    lc9cRadio = Radiobutton(frame, text = "The Yard 9th: C", variable = r, value = 4, indicatoron = 0, 
                        bg = bColor1, fg = fColor1, selectcolor = bColor2, command = yard9cAction)

    lewisohn203aRadio = Radiobutton(frame, text = "Lewisohn 203A", variable = r, value = 5, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203aAction)

    lewisohn203bRadio = Radiobutton(frame, text = "Lewisohn 203B", variable = r, value = 6, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203bAction)

    space10Radio = Label(frame, bg = bColor1).grid(row = 16, column = 2)

    lewisohn203dRadio = Radiobutton(frame, text = "Lewisohn 203D", variable = r, value = 7, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203dAction)

    lewisohn203eRadio = Radiobutton(frame, text = "Lewisohn 203E", variable = r, value = 8, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203eAction)

    lewisohn203fRadio = Radiobutton(frame, text = "Lewisohn 203F", variable = r, value = 9, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203fAction)

    space11Radio = Label(frame, bg = bColor1).grid(row = 18, column = 2)

    lewisohn203iRadio = Radiobutton(frame, text = "Lewisohn 203I", variable = r, value = 10, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203iAction)

    lewisohn203k6Radio = Radiobutton(frame, text = "Lewisohn 203K-6", variable = r, value = 11, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203k6Action,
                                width = 17)

    lewisohn203k7Radio = Radiobutton(frame, text = "Lewisohn 203K-7", variable = r, value = 12, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203k7Action)

    space12Radio = Label(frame, bg = bColor1).grid(row = 20, column = 2)

    lewisohn203nRadio = Radiobutton(frame, text = "Lewisohn 203N", variable = r, value = 13, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203nAction)

    lewisohn203yRadio = Radiobutton(frame, text = "Lewisohn 203Y", variable = r, value = 14, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203yAction)

    lewisohn203zRadio = Radiobutton(frame, text = "Lewisohn 203Z", variable = r, value = 15, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203zAction)

    space13Radio = Label(frame, bg = bColor1).grid(row = 22, column = 2)

    lewisohn214aRadio = Radiobutton(frame, text = "Lewisohn 214A", variable = r, value = 16, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew214aAction)

    lewisohn303aRadio = Radiobutton(frame, text = "Lewisohn 303A", variable = r, value = 17, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew303aAction)

    lewisohn303cRadio = Radiobutton(frame, text = "Lewisohn 303C", variable = r, value = 18, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew303cAction)

    space14Radio = Label(frame, bg = bColor1).grid(row = 24, column = 2)

    lewisohn504aRadio = Radiobutton(frame, text = "Lewisohn 504A", variable = r, value = 19, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504aAction)

    lewisohn504bRadio = Radiobutton(frame, text = "Lewisohn 504B", variable = r, value = 20, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504bAction)

    lewisohn504cRadio = Radiobutton(frame, text = "Lewisohn 504C", variable = r, value = 21, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504cAction)

    space15Radio = Label(frame, bg = bColor1).grid(row = 26, column = 2)

    lewisohn504dRadio = Radiobutton(frame, text = "Lewisohn 504D", variable = r, value = 22, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504dAction)

    lewisohn504fRadio = Radiobutton(frame, text = "Lewisohn 504F", variable = r, value = 23, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504fAction)

    #Select All Toggle Button
    space16 = Label(frame, bg = bColor1).grid(row = 28, column = 2)
    space17 = Label(frame, bg = bColor1).grid(row = 29, column = 2)

    select = partial(selectAll, buttons)
    sAll = Button(frame, text = "Select All Toggle Switch", command = select, bg = bColor1, fg = fColor1)
    sAll.grid(row = 30, column = 2, columnspan = 2)

    #Submit Button
    space18 = Label(frame, bg = bColor1).grid(row = 31, column = 2)
    space19 = Label(frame, bg = bColor1).grid(row = 32, column = 2)

    action = partial(parallel, broadwayBool, yard9aBool, yard9bBool, yard9cBool, lew203aBool, lew203bBool,
                        lew203dBool, lew203eBool, lew203fBool, lew203iBool, lew203k6Bool, lew203k7Bool,
                        lew203nBool, lew203yBool, lew203zBool, lew214aBool, lew303aBool, lew303cBool,
                        lew504aBool, lew504bBool, lew504cBool, lew504dBool, lew504fBool, v, enter,
                        root)

    submit = Button(frame, text = "Submit", command = action, width = 10, height = 3, 
                    font = ('Helvetica', '17'), bg = bColor1, fg = fColor1)
    submit.grid(row = 33, column = 2, columnspan = 2)

    #First Set of Instructions
    prompt1 = Label(frame, text = "Please enter the uni(s) you would like to change permissions for.", 
                    bg = bColor1, fg = fColor1)
    prompt1.grid(row = 0, column = 1, columnspan = 4)

    prompt2 = Label(frame, text = "Seperate multiple unis with spaces or commas.", bg = bColor1, 
                    fg = fColor1)
    prompt2.grid(row = 1, column = 1, columnspan = 4)

    space2 = Label(frame, bg = bColor1).grid(row = 2, column = 2)

    #Email entry
    entry = Entry(frame, textvariable = enter)
    entry.grid(row = 3, column = 1, columnspan = 4)

    space3 = Label(frame, bg = bColor1).grid(row = 4, column = 2)
    space4 = Label(frame, bg = bColor1).grid(row = 5, column = 2)

        #List of all conference rooms(calendars) as Checkbuttons (Default)
    prompt4 = Label(frame, text = "Select which conference rooms to configure.", 
                    bg = bColor1, fg = fColor1)
    prompt4.grid(row = 11, column = 1, columnspan = 4)

    space8 = Label(frame, bg = bColor1).grid(row = 12, column = 2)

    b2875 = Checkbutton(frame, text = "2875 Broadway", variable = broadwayBool, indicatoron = 0, 
                        bg = bColor1, fg = fColor1, selectcolor = bColor2, command = b2875Action)
    b2875.grid(row =13, column = 1)

    lc9a = Checkbutton(frame, text = "The Yard 9th: A", variable = yard9aBool, indicatoron = 0, 
                        bg = bColor1, fg = fColor1, selectcolor = bColor2, command = yard9aAction)
    lc9a.grid(row = 13, column = 2, columnspan = 2)

    lc9b = Checkbutton(frame, text = "The Yard 9th: B", variable = yard9bBool, indicatoron = 0, 
                        bg = bColor1, fg = fColor1, selectcolor = bColor2, command = yard9bAction)
    lc9b.grid(row = 13, column = 4)

    space9 = Label(frame, bg = bColor1).grid(row = 14, column = 2)

    lc9c = Checkbutton(frame, text = "The Yard 9th: C", variable = yard9cBool, indicatoron = 0, 
                        bg = bColor1, fg = fColor1, selectcolor = bColor2, command = yard9cAction)
    lc9c.grid(row = 15, column = 1)

    lewisohn203a = Checkbutton(frame, text = "Lewisohn 203A", variable = lew203aBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203aAction)
    lewisohn203a.grid(row = 15, column = 2, columnspan = 2)

    lewisohn203b = Checkbutton(frame, text = "Lewisohn 203B", variable = lew203bBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203bAction)
    lewisohn203b.grid(row = 15, column = 4)

    space10 = Label(frame, bg = bColor1).grid(row = 16, column = 2)

    lewisohn203d = Checkbutton(frame, text = "Lewisohn 203D", variable = lew203dBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203dAction)
    lewisohn203d.grid(row = 17, column = 1)

    lewisohn203e = Checkbutton(frame, text = "Lewisohn 203E", variable = lew203eBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203eAction)
    lewisohn203e.grid(row = 17, column = 2, columnspan = 2)

    lewisohn203f = Checkbutton(frame, text = "Lewisohn 203F", variable = lew203fBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203fAction)
    lewisohn203f.grid(row = 17, column = 4)

    space11 = Label(frame, bg = bColor1).grid(row = 18, column = 2)

    lewisohn203i = Checkbutton(frame, text = "Lewisohn 203I", variable = lew203iBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203iAction)
    lewisohn203i.grid(row = 19, column = 1)

    lewisohn203k6 = Checkbutton(frame, text = "Lewisohn 203K-6", variable = lew203k6Bool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203k6Action)
    lewisohn203k6.grid(row = 19, column = 2, columnspan = 2)

    lewisohn203k7 = Checkbutton(frame, text = "Lewisohn 203K-7", variable = lew203k7Bool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203k7Action)
    lewisohn203k7.grid(row = 19, column = 4)

    space12 = Label(frame, bg = bColor1).grid(row = 20, column = 2)

    lewisohn203n = Checkbutton(frame, text = "Lewisohn 203N", variable = lew203nBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203nAction)
    lewisohn203n.grid(row = 21, column = 1)

    lewisohn203y = Checkbutton(frame, text = "Lewisohn 203Y", variable = lew203yBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203yAction)
    lewisohn203y.grid(row = 21, column = 2, columnspan = 2)

    lewisohn203z = Checkbutton(frame, text = "Lewisohn 203Z", variable = lew203zBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew203zAction)
    lewisohn203z.grid(row = 21, column = 4)

    space13 = Label(frame, bg = bColor1).grid(row = 22, column = 2)

    lewisohn214a = Checkbutton(frame, text = "Lewisohn 214A", variable = lew214aBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew214aAction)
    lewisohn214a.grid(row = 23, column = 1)

    lewisohn303a = Checkbutton(frame, text = "Lewisohn 303A", variable = lew303aBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew303aAction)
    lewisohn303a.grid(row = 23, column = 2, columnspan = 2)

    lewisohn303c = Checkbutton(frame, text = "Lewisohn 303C", variable = lew303cBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew303cAction)
    lewisohn303c.grid(row = 23, column = 4)

    space14 = Label(frame, bg = bColor1).grid(row = 24, column = 2)

    lewisohn504a = Checkbutton(frame, text = "Lewisohn 504A", variable = lew504aBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504aAction)
    lewisohn504a.grid(row = 25, column = 1)

    lewisohn504b = Checkbutton(frame, text = "Lewisohn 504B", variable = lew504bBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504bAction)
    lewisohn504b.grid(row = 25, column = 2, columnspan = 2)

    lewisohn504c = Checkbutton(frame, text = "Lewisohn 504C", variable = lew504cBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504cAction)
    lewisohn504c.grid(row = 25, column = 4)

    space15 = Label(frame, bg = bColor1).grid(row = 26, column = 2)

    lewisohn504d = Checkbutton(frame, text = "Lewisohn 504D", variable = lew504dBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504dAction)
    lewisohn504d.grid(row = 27, column = 1)

    lewisohn504f = Checkbutton(frame, text = "Lewisohn 504F", variable = lew504fBool, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = lew504fAction)
    lewisohn504f.grid(row = 27, column = 2, columnspan = 2)

    #Decide whether to add, delete, or list users for a calendar
    prompt3 = Label(frame, text = "Select whether to add, remove, or list the user(s).", 
                    bg = bColor1, fg = fColor1)
    prompt3.grid(row = 6, column = 1, columnspan = 4)

    space5 = Label(frame, bg = bColor1).grid(row = 7, column = 2)

    submitAction1 = partial(addSubmit, frame, submit, sAll, b2875Radio, lc9aRadio, lc9bRadio, lc9cRadio, lewisohn203aRadio, 
                    lewisohn203bRadio, lewisohn203dRadio, lewisohn203eRadio, lewisohn203fRadio,
                    lewisohn203iRadio, lewisohn203k6Radio, lewisohn203k7Radio, lewisohn203nRadio, 
                    lewisohn203yRadio, lewisohn203zRadio, lewisohn214aRadio, lewisohn303aRadio,
                    lewisohn303cRadio, lewisohn504aRadio, lewisohn504bRadio, lewisohn504cRadio,
                    lewisohn504dRadio, lewisohn504fRadio, b2875, lc9a, lc9b, lc9c, lewisohn203a, 
                    lewisohn203b, lewisohn203d, lewisohn203e, lewisohn203f, lewisohn203i, lewisohn203k6, 
                    lewisohn203k7, lewisohn203n, lewisohn203y, lewisohn203z, lewisohn214a, lewisohn303a,
                    lewisohn303c, lewisohn504a, lewisohn504b, lewisohn504c,  lewisohn504d, lewisohn504f)

    submitAction2 = partial(removeSubmit, frame, submit, sAll, b2875Radio, lc9aRadio, lc9bRadio, lc9cRadio, lewisohn203aRadio, 
                    lewisohn203bRadio, lewisohn203dRadio, lewisohn203eRadio, lewisohn203fRadio,
                    lewisohn203iRadio, lewisohn203k6Radio, lewisohn203k7Radio, lewisohn203nRadio, 
                    lewisohn203yRadio, lewisohn203zRadio, lewisohn214aRadio, lewisohn303aRadio,
                    lewisohn303cRadio, lewisohn504aRadio, lewisohn504bRadio, lewisohn504cRadio,
                    lewisohn504dRadio, lewisohn504fRadio, b2875, lc9a, lc9b, lc9c, lewisohn203a, 
                    lewisohn203b, lewisohn203d, lewisohn203e, lewisohn203f, lewisohn203i, lewisohn203k6, 
                    lewisohn203k7, lewisohn203n, lewisohn203y, lewisohn203z, lewisohn214a, lewisohn303a,
                    lewisohn303c, lewisohn504a, lewisohn504b, lewisohn504c,  lewisohn504d, lewisohn504f)

    plusButton = Radiobutton(frame, text = "Add User", variable = v, value = 1, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = submitAction1)
    plusButton.grid(row = 8, column = 1)

    minusButton = Radiobutton(frame, text = "Delete User", variable = v, value = 0, indicatoron = 0, 
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = submitAction1)
    minusButton.grid(row = 8, column = 2, columnspan = 2)

    listButton = Radiobutton(frame, text = "List Users", variable = v, value = 2, indicatoron = 0,
                                bg = bColor1, fg = fColor1, selectcolor = bColor2, command = submitAction2)
    listButton.grid(row = 8, column = 4)

    space6 = Label(frame, bg = bColor1).grid(row = 9, column = 2)
    space7 = Label(frame, bg = bColor1).grid(row = 10, column = 2)

    mainloop()

def addSubmit(frame, submit, sAll, b2875Radio, lc9aRadio, lc9bRadio, lc9cRadio, lewisohn203aRadio, 
                    lewisohn203bRadio, lewisohn203dRadio, lewisohn203eRadio, lewisohn203fRadio,
                    lewisohn203iRadio, lewisohn203k6Radio, lewisohn203k7Radio, lewisohn203nRadio, 
                    lewisohn203yRadio, lewisohn203zRadio, lewisohn214aRadio, lewisohn303aRadio,
                    lewisohn303cRadio, lewisohn504aRadio, lewisohn504bRadio, lewisohn504cRadio,
                    lewisohn504dRadio, lewisohn504fRadio, b2875, lc9a, lc9b, lc9c, lewisohn203a, 
                    lewisohn203b, lewisohn203d, lewisohn203e, lewisohn203f, lewisohn203i, lewisohn203k6, 
                    lewisohn203k7, lewisohn203n, lewisohn203y, lewisohn203z, lewisohn214a, lewisohn303a,
                    lewisohn303c, lewisohn504a, lewisohn504b, lewisohn504c,  lewisohn504d, lewisohn504f):
    submit.grid(row = 33, column = 2, columnspan = 2)
    sAll.grid(row = 30, column = 2, columnspan = 2)

    b2875Radio.grid_forget()
    lc9aRadio.grid_forget()
    lc9bRadio.grid_forget()
    lc9cRadio.grid_forget()
    lewisohn203aRadio.grid_forget()
    lewisohn203bRadio.grid_forget()
    lewisohn203dRadio.grid_forget()
    lewisohn203eRadio.grid_forget()
    lewisohn203fRadio.grid_forget()
    lewisohn203iRadio.grid_forget()
    lewisohn203k6Radio.grid_forget()
    lewisohn203k7Radio.grid_forget()
    lewisohn203nRadio.grid_forget()
    lewisohn203yRadio.grid_forget()
    lewisohn203zRadio.grid_forget()
    lewisohn214aRadio.grid_forget()
    lewisohn303aRadio.grid_forget()
    lewisohn303cRadio.grid_forget()
    lewisohn504aRadio.grid_forget()
    lewisohn504bRadio.grid_forget()
    lewisohn504cRadio.grid_forget()
    lewisohn504dRadio.grid_forget()
    lewisohn504fRadio.grid_forget()

    b2875.grid(row =13, column = 1)
    lc9a.grid(row = 13, column = 2, columnspan = 2)
    lc9b.grid(row = 13, column = 4)
    lc9c.grid(row = 15, column = 1)
    lewisohn203a.grid(row = 15, column = 2, columnspan = 2)
    lewisohn203b.grid(row = 15, column = 4)
    lewisohn203d.grid(row = 17, column = 1)
    lewisohn203e.grid(row = 17, column = 2, columnspan = 2)
    lewisohn203f.grid(row = 17, column = 4)
    lewisohn203i.grid(row = 19, column = 1)
    lewisohn203k6.grid(row = 19, column = 2, columnspan = 2)
    lewisohn203k7.grid(row = 19, column = 4)
    lewisohn203n.grid(row = 21, column = 1)
    lewisohn203y.grid(row = 21, column = 2, columnspan = 2)
    lewisohn203z.grid(row = 21, column = 4)
    lewisohn214a.grid(row = 23, column = 1)
    lewisohn303a.grid(row = 23, column = 2, columnspan = 2)
    lewisohn303c.grid(row = 23, column = 4)
    lewisohn504a.grid(row = 25, column = 1)
    lewisohn504b.grid(row = 25, column = 2, columnspan = 2)
    lewisohn504c.grid(row = 25, column = 4)
    lewisohn504d.grid(row = 27, column = 1)
    lewisohn504f.grid(row = 27, column = 2, columnspan = 2)

def removeSubmit(frame, submit, sAll, b2875Radio, lc9aRadio, lc9bRadio, lc9cRadio, lewisohn203aRadio, 
                    lewisohn203bRadio, lewisohn203dRadio, lewisohn203eRadio, lewisohn203fRadio,
                    lewisohn203iRadio, lewisohn203k6Radio, lewisohn203k7Radio, lewisohn203nRadio, 
                    lewisohn203yRadio, lewisohn203zRadio, lewisohn214aRadio, lewisohn303aRadio,
                    lewisohn303cRadio, lewisohn504aRadio, lewisohn504bRadio, lewisohn504cRadio,
                    lewisohn504dRadio, lewisohn504fRadio, b2875, lc9a, lc9b, lc9c, lewisohn203a, 
                    lewisohn203b, lewisohn203d, lewisohn203e, lewisohn203f, lewisohn203i, lewisohn203k6, 
                    lewisohn203k7, lewisohn203n, lewisohn203y, lewisohn203z, lewisohn214a, lewisohn303a,
                    lewisohn303c, lewisohn504a, lewisohn504b, lewisohn504c,  lewisohn504d, lewisohn504f):
    submit.grid_forget()
    sAll.grid_forget()

    b2875.grid_forget()
    lc9a.grid_forget()
    lc9b.grid_forget()
    lc9c.grid_forget()
    lewisohn203a.grid_forget()
    lewisohn203b.grid_forget()
    lewisohn203d.grid_forget()
    lewisohn203e.grid_forget()
    lewisohn203f.grid_forget()
    lewisohn203i.grid_forget()
    lewisohn203k6.grid_forget()
    lewisohn203k7.grid_forget()
    lewisohn203n.grid_forget()
    lewisohn203y.grid_forget()
    lewisohn203z.grid_forget()
    lewisohn214a.grid_forget()
    lewisohn303a.grid_forget()
    lewisohn303c.grid_forget()
    lewisohn504a.grid_forget()
    lewisohn504b.grid_forget()
    lewisohn504c.grid_forget()
    lewisohn504d.grid_forget()
    lewisohn504f.grid_forget()

    b2875Radio.grid(row =13, column = 1)
    lc9aRadio.grid(row = 13, column = 2, columnspan = 2)
    lc9bRadio.grid(row = 13, column = 4)
    lc9cRadio.grid(row = 15, column = 1)
    lewisohn203aRadio.grid(row = 15, column = 2, columnspan = 2)
    lewisohn203bRadio.grid(row = 15, column = 4)
    lewisohn203dRadio.grid(row = 17, column = 1)
    lewisohn203eRadio.grid(row = 17, column = 2, columnspan = 2)
    lewisohn203fRadio.grid(row = 17, column = 4)
    lewisohn203iRadio.grid(row = 19, column = 1)
    lewisohn203k6Radio.grid(row = 19, column = 2, columnspan = 2)
    lewisohn203k7Radio.grid(row = 19, column = 4)
    lewisohn203nRadio.grid(row = 21, column = 1)
    lewisohn203yRadio.grid(row = 21, column = 2, columnspan = 2)
    lewisohn203zRadio.grid(row = 21, column = 4)
    lewisohn214aRadio.grid(row = 23, column = 1)
    lewisohn303aRadio.grid(row = 23, column = 2, columnspan = 2)
    lewisohn303cRadio.grid(row = 23, column = 4)
    lewisohn504aRadio.grid(row = 25, column = 1)
    lewisohn504bRadio.grid(row = 25, column = 2, columnspan = 2)
    lewisohn504cRadio.grid(row = 25, column = 4)
    lewisohn504dRadio.grid(row = 27, column = 1)
    lewisohn504fRadio.grid(row = 27, column = 2, columnspan = 2)


def userList(listbox, v, cal):
    if v.get() == 2:
        listbox.delete(0, END)
        if cal == 'columbia.edu_3634343538303339393332@resource.calendar.google.com':
            listbox.insert(END, "2875 Broadway")
        elif cal == 'columbia.edu_1886rf4mc1mfag6kghp73f2fttf5i6gb6os30e1m6ko38dhn68@resource.calendar.google.com':
            listbox.insert(END, "The Yard 9A")
        elif cal == 'columbia.edu_1880mgrd7sf92glaj469rmeah1t1u6gb6orjic9o6cs3ed1o68@resource.calendar.google.com':
            listbox.insert(END, "The Yard 9B")
        elif cal ==  'columbia.edu_188el4hr2ok5minflnjojhgapfuga6gb6orjgd9k68pjgcpg6c@resource.calendar.google.com':
            listbox.insert(END, "The Yard 9C")
        elif cal ==  'columbia.edu_35343032323839342d363935@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203A")
        elif cal ==  'columbia.edu_1884n0i2dkfgmi32isqpcealde0b86gb6kp36dhl60r3cd9k64@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203B")
        elif cal ==  'columbia.edu_3532353238343634393731@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203D")
        elif cal ==  'columbia.edu_1886ghk841pv6hftl62d73rd3675o6gb6kp3cc9g68p38c9m6o@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203E")
        elif cal == 'columbia.edu_18813q25q6djqgfslqaeauismuv9o6g96kp3ed1o60qj2e0@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203F")
        elif cal ==  'columbia.edu_1884cst50kde2g3vmdci2rqh09gl06gb6kpj0e1n74pjed1p6c@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203I")
        elif cal ==  'columbia.edu_188c1aq7s485qgu0hg5jd0hmcip6g6gb6sp36d9k74sj8d9m6o@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203K-6")
        elif cal ==  'columbia.edu_1885n4lramp88hndl93qf9gfhotpi6gb6sp34e9n74p32dhm74@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203K-7")
        elif cal ==  'columbia.edu_188cdrv99d5hsj9mlb470edcu214e6gb6kpjac9p6os36d9h60@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203N")
        elif cal ==  'columbia.edu_3534363133303738373435@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203Y")
        elif cal ==  'columbia.edu_3534373434303839393134@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 203Z")
        elif cal ==  'columbia.edu_35333233343630372d333234@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 214A")
        elif cal ==  'columbia.edu_313935343339302d393131@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 303A")
        elif cal ==  'columbia.edu_333135393838313532@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 303C")
        elif cal ==  'columbia.edu_3934343437373831353937@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 504A")
        elif cal ==  'columbia.edu_3934353736353031323032@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 504B")
        elif cal ==  'columbia.edu_393436313334353532@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 504C")
        elif cal ==  'columbia.edu_39343733343433372d3431@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 504D")
        elif cal ==  'columbia.edu_39343935353630382d323730@resource.calendar.google.com':
            listbox.insert(END, "Lewisohn 504F")
        
        users = edit.listUser(cal)

        for i in range(len(users)):
            if i == 0:
                continue
            else:
                user = users[i]
                listbox.insert(END, user[5:])
                

def main(info):
    listing = []

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

def parallel(broadwayBool, yard9aBool, yard9bBool, yard9cBool, lew203aBool, lew203bBool,
                lew203dBool, lew203eBool, lew203fBool, lew203iBool, lew203k6Bool, lew203k7Bool,
                lew203nBool, lew203yBool, lew203zBool, lew214aBool, lew303aBool, lew303cBool,
                lew504aBool, lew504bBool, lew504cBool, lew504dBool, lew504fBool, v, enter, root):
    bColor1 = "#122d62"
    bColor2 = "#33cc33"
    fColor1 = "#ffffff"
    check = False

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