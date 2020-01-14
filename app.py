import bs4
import lxml
import requests
import csv
import tkinter
from tkinter import ttk
from make_file import make_csv

# Makes csv file
csv_file = open('stats.csv', 'w')
csv_writer = csv.writer(csv_file)

# RUN THE APPLET
window = tkinter.Tk()

# NAME OF THE WINDOW
window.title("ESPN DATA SELECTOR")

#YEAR
label_one = ttk.Label(window, text = 'Enter a year (2001-Present)): ')
label_one.grid(row = 0, column = 0)
#User entry 1 box
year = tkinter.IntVar()
user_entry1 = ttk.Entry(window, width = 26, textvariable=year)
user_entry1.grid(row = 0, column = 1)

#REGULAR OR POST SEASON
label_two = ttk.Label(window, text = 'Regular season (R) or Post season (P): ')
label_two.grid(row = 1, column = 0)
#User Entry 2 box
season = tkinter.StringVar()

user_entry2 = ttk.Entry(window, width= 26, textvariable=season)
user_entry2.grid(row = 1, column = 1)

#NUM OF ENTRIES
label_three = ttk.Label(window, text = 'How many entries: ')
label_three.grid(row = 2, column = 0)
#User Entry 3 box
entries = tkinter.IntVar()
user_entry3 = ttk.Entry(window, width= 26, textvariable= entries)
user_entry3.grid(row = 2, column = 1)


def action():

    season_type = 0
    if season.get() == 'R':
        season_type = 2
    if season.get() == 'P':
        season_type = 3

    year_value = year.get()
    entry = entries.get()

    make_csv(year_value, season_type, entry,csv_writer)



btn = ttk.Button(window, text="search", command=action)
btn.grid(row=1, column=2)

def quit():
    window.destroy()

exit_btn = ttk.Button(window, text='Quit', command=quit)
exit_btn.grid(row=2, column=2)

window.mainloop()





