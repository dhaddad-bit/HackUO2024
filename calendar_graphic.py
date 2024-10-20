import tkinter as tk
from tkinter import ttk

from tkcalendar import Calendar, DateEntry
import datetime

root = tk.Tk()

cal = Calendar(root, font="Arial 14", cursor="hand1")
current_date = cal.datetime.today()

dates = [(datetime.date(2024, 10, 18), '5'), (datetime.date(2024, 10, 15), '7'),
         (datetime.date(2024, 10, 17), '3'), (datetime.date(2024, 10, 16), '10')]

cal.tag_config('1', background='SteelBlue4', foreground='white')
cal.tag_config('2', background='SteelBlue3', foreground='white')
cal.tag_config('3', background='SteelBlue2', foreground='white')
cal.tag_config('4', background='SteelBlue1', foreground='white')
cal.tag_config('5', background='turquoise', foreground='white')
cal.tag_config('6', background='aquamarine', foreground='white')
cal.tag_config('7', background='SpringGreen1', foreground='white')
cal.tag_config('8', background='SpringGreen2', foreground='white')
cal.tag_config('9', background='SpringGreen3', foreground='white')
cal.tag_config('10', background="SpringGreen4", foreground='white')

for i in range(len(dates)):
    cal.calevent_create(dates[i][0], text="Hey!", tags=dates[i][1])


def on_date_selected(event):
    daylist= []
    selected_date = cal.selection_get()
    events = cal.get_calevents(selected_date)
    devents = list(events)
    for i in devents:
        b = cal.calevent_cget(i, option="text")
        daylist.append(b)
    for item in daylist:
        print(item)

cal.bind("<<CalendarSelected>>", on_date_selected)

cal.pack(fill="both", expand=True)

root.mainloop()