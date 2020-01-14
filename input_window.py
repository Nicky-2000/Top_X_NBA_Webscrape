import tkinter

from tkinter import ttk

window = tkinter.Tk()

# NAME OF THE WINDOW

window.title("ESPN DATA SELECTOR")

#LABEL 1 (input #1 title)
label_one = ttk.Label(window, text = 'Enter a year (2001-Present)): ')
label_one.grid(row = 0, column = 0)

#User entry 1 box
user_entry1 = ttk.Entry(window, width = 26)
user_entry1.grid(row = 0, column = 1)

#REGULAR OR POST SEASON

label_two = ttk.Label(window, text = 'Regular season (R) or Post season (P): ')
label_two.grid(row = 1, column = 0)

#User Entry 2 box
user_entry2 = ttk.Entry(window, width= 26)
user_entry2.grid(row = 1, column = 1)


#NUM OF ENTRIES

label_three = ttk.Label(window, text = 'How many entries: ')
label_three.grid(row = 2, column = 0)

#User Entry 3 box

user_entry3 = ttk.Entry(window, width= 26)
user_entry3.grid(row = 2, column = 1)






def action():
    year = user_entry1.get()
    reg_or_p = user_entry2.get()
    entries = user_entry3.get()


btn = ttk.Button(window, text="search", command=action)
btn.grid(row=2, column=2)


# RUN THE APPLET

window.mainloop()


# enter year - box - submitButton
