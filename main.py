from functools import partial, reduce
from operator import add
from tkinter import (
    END,
    Button,
    Canvas,
    Checkbutton,
    Entry,
    Frame,
    IntVar,
    Label,
    Listbox,
    Radiobutton,
    Scrollbar,
    StringVar,
    Tk,
    Toplevel,
    mainloop,
)

import calUpdate
from calSetup import get_calendar_service

# All calendar IDs
calendar_ids = {
    "cal1": "id1@resource.calendar.google.com",
    "cal2": "id2@resource.calendar.google.com",
    "cal3": "id3@resource.calendar.google.com",
}


def addSubmit(frame, submit, sAll, allRadio, allCheck, mainRow):
    submit.grid(row=mainRow, column=2, columnspan=2)
    sAll.grid(row=mainRow - 3, column=2, columnspan=2)

    for radioButton in allRadio:
        radioButton.grid_forget()

    row = 13
    col = 1
    for checkButton in allCheck:
        if col in range(1, 5):
            checkButton.grid(row=row, column=col)
            col += 1

        if col == 4:
            row += 2


def removeSubmit(frame, submit, sAll, allRadio, allCheck):
    submit.grid_forget()
    sAll.grid_forget()

    for checkButton in allCheck:
        checkButton.grid_forget()

    row = 13
    col = 1
    for radioButton in allRadio:
        if col in range(1, 5):
            radioButton.grid(row=row, column=col)
            col += 1

        if col == 4:
            row += 2


def listUsers(listbox, v, name, cal):
    if v.get() == 2:
        listbox.delete(0, END)
        listbox.insert(END, name)

        users = calUpdate.listUser(cal)

        for i in range(len(users)):
            if i == 0:
                continue
            else:
                user = users[i]
                listbox.insert(END, user[5:])


def selectAll(buttons):
    for item in buttons:
        if item.get():
            item.set(0)
        else:
            item.set(1)


def main():
    # set up the primary color palette for the tkinter application
    backgroundColor = "#122d62"
    backgroundSecondary = "#33cc33"
    fontColor = "#ffffff"

    # set up the root window of the application
    root = Tk()
    root.title("Google Calendar Access Permissions Editor")
    root.configure(bg="lime")
    root.geometry("+600+25")

    canvas = Canvas(
        root,
        scrollregion=(0, 0, 500, 500),
        bg=backgroundColor,
        highlightthickness=0,
    )
    canvas.grid(row=0, column=0, sticky="news")

    # add a scroll bar to the window
    vert_scroll_bar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    vert_scroll_bar.grid(row=0, column=5, sticky="ens", rowspan=100)
    canvas.configure(yscrollcommand=vert_scroll_bar.set)

    frame = Frame(canvas, bg=backgroundColor)
    frame.grid(row=0, column=0, sticky="news", padx=30, pady=30)

    # Create arrays to contain the dynamically generated buttons
    allRadio = []
    allCheck = []
    allBool = []

    enter = StringVar()
    v = IntVar(value=3)
    r = IntVar()

    # First Set of Instructions
    uni_permission_entry_prompt = Label(
        frame,
        text="Please enter the uni(s) whose permissions you'd like to change.",
        bg=backgroundColor,
        fg=fontColor,
    )
    uni_permission_entry_prompt.grid(row=0, column=1, columnspan=4)

    uni_permission_entry_info = Label(
        frame,
        text="Seperate multiple unis with spaces or commas.",
        bg=backgroundColor,
        fg=fontColor,
    )
    uni_permission_entry_info.grid(row=1, column=1, columnspan=4)

    # Listbox to list users for each calendar
    Label(frame, text="      ", bg=backgroundColor).grid(
        row=1, rowspan=50, column=5
    )
    users_listbox = Listbox(frame, width=40, yscrollcommand=vert_scroll_bar.set)
    users_listbox.grid(row=1, rowspan=50, column=6, sticky="news")

    vert_scroll_bar.config(command=users_listbox.yview)

    Label(frame, bg=backgroundColor).grid(row=2, column=2)

    # Email entry
    entry = Entry(frame, textvariable=enter)
    entry.grid(row=3, column=1, columnspan=4)

    Label(frame, bg=backgroundColor).grid(row=4, column=2)
    Label(frame, bg=backgroundColor).grid(row=5, column=2)

    # Decide whether to add, delete, or list users for a calendar
    action_type_prompt = Label(
        frame,
        text="Select whether to add, remove, or list the user(s).",
        bg=backgroundColor,
        fg=fontColor,
    )
    action_type_prompt.grid(row=6, column=1, columnspan=4)

    Label(frame, bg=backgroundColor).grid(row=7, column=2)
    Label(frame, bg=backgroundColor).grid(row=9, column=2)
    Label(frame, bg=backgroundColor).grid(row=10, column=2)

    conference_room_prompt = Label(
        frame,
        text="Select which conference rooms to configure.",
        bg=backgroundColor,
        fg=fontColor,
    )
    conference_room_prompt.grid(row=11, column=1, columnspan=4)

    Label(frame, bg=backgroundColor).grid(row=12, column=2)

    # Conference Rooms as Radio Buttons and Checkbuttons (Default)
    mainRow = 13
    col = 1
    for index, key in enumerate(calendar_ids):
        allBool.append(IntVar())
        if col == 1:
            allRadio.append(
                Radiobutton(
                    frame,
                    text=key,
                    variable=r,
                    value=index + 1,
                    indicatoron=0,
                    bg=backgroundColor,
                    fg=fontColor,
                    selectcolor=backgroundSecondary,
                    command=partial(
                        listUsers, users_listbox, v, key, calendar_ids[key]
                    ),
                )
            )

            allCheck.append(
                Checkbutton(
                    frame,
                    text=key,
                    variable=allBool[index],
                    indicatoron=0,
                    bg=backgroundColor,
                    fg=fontColor,
                    selectcolor=backgroundSecondary,
                )
            )
            allCheck[index].grid(row=mainRow, column=col)

            col += 1

        elif col == 2:
            allRadio.append(
                Radiobutton(
                    frame,
                    text=key,
                    variable=r,
                    value=index + 1,
                    indicatoron=0,
                    bg=backgroundColor,
                    fg=fontColor,
                    selectcolor=backgroundSecondary,
                    command=partial(
                        listUsers, users_listbox, v, key, calendar_ids[key]
                    ),
                )
            )

            allCheck.append(
                Checkbutton(
                    frame,
                    text=key,
                    variable=allBool[index],
                    indicatoron=0,
                    bg=backgroundColor,
                    fg=fontColor,
                    selectcolor=backgroundSecondary,
                )
            )
            allCheck[index].grid(row=mainRow, column=col)

            col += 1

        elif col == 3:
            allRadio.append(
                Radiobutton(
                    frame,
                    text=key,
                    variable=r,
                    value=index + 1,
                    indicatoron=0,
                    bg=backgroundColor,
                    fg=fontColor,
                    selectcolor=backgroundSecondary,
                    command=partial(
                        listUsers, users_listbox, v, key, calendar_ids[key]
                    ),
                )
            )

            allCheck.append(
                Checkbutton(
                    frame,
                    text=key,
                    variable=allBool[index],
                    indicatoron=0,
                    bg=backgroundColor,
                    fg=fontColor,
                    selectcolor=backgroundSecondary,
                )
            )
            allCheck[index].grid(row=mainRow, column=col)

            col += 1

        elif col == 4:
            allRadio.append(
                Radiobutton(
                    frame,
                    text=key,
                    variable=r,
                    value=index + 1,
                    indicatoron=0,
                    bg=backgroundColor,
                    fg=fontColor,
                    selectcolor=backgroundSecondary,
                    command=partial(
                        listUsers, users_listbox, v, key, calendar_ids[key]
                    ),
                )
            )

            allCheck.append(
                Checkbutton(
                    frame,
                    text=key,
                    variable=allBool[index],
                    indicatoron=0,
                    bg=backgroundColor,
                    fg=fontColor,
                    selectcolor=backgroundSecondary,
                )
            )
            allCheck[index].grid(row=mainRow, column=col)

            mainRow += 1
            spaceRadio = Label(frame, bg=backgroundColor)
            spaceRadio.grid(row=mainRow, column=col)

            spaceCheck = Label(frame, bg=backgroundColor)
            spaceCheck.grid(row=mainRow, column=col)

            mainRow += 1
            col = 1

    mainRow += 1  # row (cal/3) + 1

    # Select All Toggle Button
    Label(frame, bg=backgroundColor).grid(row=mainRow, column=2)
    mainRow += 1
    Label(frame, bg=backgroundColor).grid(row=mainRow, column=2)
    mainRow += 1

    select = partial(selectAll, allBool)
    sAll = Button(
        frame,
        text="Select All Toggle Switch",
        command=select,
        bg=backgroundColor,
        fg=fontColor,
    )
    sAll.grid(row=mainRow, column=2, columnspan=2)
    mainRow += 1

    # Submit Button
    Label(frame, bg=backgroundColor).grid(row=mainRow, column=2)
    mainRow += 1
    Label(frame, bg=backgroundColor).grid(row=mainRow, column=2)
    mainRow += 1

    action = partial(update_calendars, v, enter, root, allBool)

    submit = Button(
        frame,
        text="Submit",
        command=action,
        width=10,
        height=3,
        font=("Helvetica", "17"),
        bg=backgroundColor,
        fg=fontColor,
    )
    submit.grid(row=mainRow, column=2, columnspan=2)

    # Dynamic Listing commands

    addAction = partial(
        addSubmit, frame, submit, sAll, allRadio, allCheck, mainRow
    )

    removeAction = partial(
        removeSubmit, frame, submit, sAll, allRadio, allCheck
    )

    listAction = partial(listUsers, users_listbox, v, calendar_ids)

    plusButton = Radiobutton(
        frame,
        text="Add User",
        variable=v,
        value=1,
        indicatoron=0,
        bg=backgroundColor,
        fg=fontColor,
        selectcolor=backgroundSecondary,
        command=addAction,
    )
    plusButton.grid(row=8, column=1)

    minusButton = Radiobutton(
        frame,
        text="Delete User",
        variable=v,
        value=0,
        indicatoron=0,
        bg=backgroundColor,
        fg=fontColor,
        selectcolor=backgroundSecondary,
        command=removeAction,
    )
    minusButton.grid(row=8, column=2, columnspan=2)

    listButton = Radiobutton(
        frame,
        text="List Users",
        variable=v,
        value=2,
        indicatoron=0,
        bg=backgroundColor,
        fg=fontColor,
        selectcolor=backgroundSecondary,
        command=listAction,
    )
    listButton.grid(row=8, column=4)

    mainloop()


def update_calendar(info):
    service = get_calendar_service()

    if info[2] == 1:
        calUpdate.add(service, str(info[0]), str(info[1]))
        return ["yes", info[3]]

    elif info[2] == 0:
        calUpdate.delete(service, str(info[0]), str(info[1]))
        return ["yes", info[3]]


def update_calendars(v, enter, root, allBool):
    backgroundColor = "#122d62"
    fontColor = "#ffffff"

    unis = []
    final = []

    unisTemp = str(enter.get())
    unisTemp = [x.strip() for x in unisTemp.split(",")]

    for i in unisTemp:
        unis.append(i.split())
    unis = reduce(add, unis)

    email_domains = ["@columbia.edu", "@gmail.com", "@hotmail.com"]

    for i in unis:
        if not any([domain in i for domain in email_domains]):
            uni = i + "@columbia.edu"
        else:
            uni = i

        for index, key in enumerate(calendar_ids):
            if allBool[index].get() == 1:
                final.append([uni, calendar_ids[key], v.get(), key])

    records = map(update_calendar, final)

    window = Toplevel(root, bg=backgroundColor)
    window.geometry("500x500+600+50")
    newCanvas = Canvas(
        window,
        scrollregion=(0, 0, 500, 500),
        bg=backgroundColor,
        highlightthickness=0,
    )
    newCanvas.grid(row=0, column=0, sticky="news")
    newCanvas.grid_rowconfigure(0, weight=1)
    newCanvas.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    errorBool = False
    for i in range(len(records)):
        if records[i][0] != "yes" and records[i][0] != "list":
            errorBool = True
            Label(newCanvas, bg=backgroundColor).grid(row=0 + (7 * i))
            display1 = Label(
                newCanvas,
                text="Finished but with errors...",
                bg=backgroundColor,
                fg=fontColor,
            )
            display1.grid(row=1 + (7 * i))

            Label(newCanvas, bg=backgroundColor).grid(row=2 + (7 * i))
            display2 = Label(
                newCanvas, text=records[i][0], bg=backgroundColor, fg=fontColor
            )
            display2.grid(row=3 + (7 * i))

            Label(newCanvas, bg=backgroundColor).grid(row=4 + (7 * i))
            display3 = Label(
                newCanvas, text=records[i][1], bg=backgroundColor, fg=fontColor
            )
            display3.grid(row=5 + (7 * i))

            Label(newCanvas, bg=backgroundColor).grid(row=6 + (7 * i))
            display4 = Label(
                newCanvas, text=records[i][2], bg=backgroundColor, fg=fontColor
            )
            display4.grid(row=7 + (7 * i))

    if not errorBool:
        display1 = Label(
            newCanvas,
            text="Finished!",
            font=("Helvetica", "17"),
            bg=backgroundColor,
            fg=fontColor,
        )
        display1.grid(row=0, rowspan=3, column=0, columnspan=3, sticky="news")


if __name__ == "__main__":
    main()
