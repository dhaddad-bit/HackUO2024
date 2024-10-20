import tkinter as tk
import tkinter.tix as tix
from tkinter import ttk
#from survey import Survey
from tkcalendar import Calendar, DateEntry
import datetime

import csv

from questions import rand_quote, load_data, load_quotes

DIC = {}

PAST_RATES = load_data("csv/rate_day.csv", ["date", "rating"])


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, CalendarPage, RateDayPage, 
                  QualPage, QuanPage, InspQuPage, EditPage, TrendPage):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        self.frames[cont].update()
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10,padx=10)

        self.calendar_frame = None
        button = tk.Button(self, text="View Calendar",
                            command=lambda: controller.show_frame(CalendarPage))

        button.pack(pady=10)

        button = tk.Button(self, text="Rate Your Day",
                           command=lambda: controller.show_frame(RateDayPage))
        button.pack(pady=10)

        button = tk.Button(self, text="Short-Answer Check-In",
                           command=lambda: controller.show_frame(QualPage))
        button.pack(pady=10)

        button = tk.Button(self, text="Numerical Check-In",
                           command=lambda: controller.show_frame(QuanPage))
        button.pack(pady=10)

        button = tk.Button(self, text="Inspirational Quotes",
                            command=lambda: controller.show_frame(InspQuPage))
        button.pack(pady=10)

        button = tk.Button(self, text="Add Your Own Stuff",
                            command=lambda: controller.show_frame(EditPage))
        button.pack(pady=10)

        button = tk.Button(self, text="Trends",
                            command=lambda: controller.show_frame(TrendPage))
        button.pack(pady=10)


class CalendarPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        #label for calendar
        self.label = tk.Label(self, text="CALENDAR")
        self.label.pack(pady=10)

        # Create a Calendar widget
        self.calendar = Calendar(self)
        self.calendar.bind("<<CalendarSelected>>", self.open_new_window)
        self.calendar.pack(fill="both", expand=True)

        for i in range(len(PAST_RATES)):
            self.calendar.calevent_create(date=PAST_RATES[i][0], text="", tags=PAST_RATES[i][1])

        self.calendar.tag_config('1', background='SteelBlue4', foreground='white')
        self.calendar.tag_config('2', background='SteelBlue3', foreground='white')
        self.calendar.tag_config('3', background='SteelBlue2', foreground='white')
        self.calendar.tag_config('4', background='SteelBlue1', foreground='white')
        self.calendar.tag_config('5', background='turquoise', foreground='white')
        self.calendar.tag_config('6', background='aquamarine', foreground='white')
        self.calendar.tag_config('7', background='SpringGreen1', foreground='white')
        self.calendar.tag_config('8', background='SpringGreen2', foreground='white')
        self.calendar.tag_config('9', background='SpringGreen3', foreground='white')
        self.calendar.tag_config('10', background="SpringGreen4", foreground='white')


        # Button to return to the main page
        self.back_button = tk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

    def open_new_window(self, event):
        new_window = tk.Toplevel(self)
        new_window.title("Hey!!")

        label = tk.Label(new_window, text="WHERE TEXT FROM EVENTS GO")
        label.pack()

        close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
        close_button.pack(pady=10)

    def update_calendar(self, date):
        self.calendar.calevent_create(date, text="", tags=DIC["rating"])

class RateDayPage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Rate Your Day!")
        label.pack(pady=10,padx=10)

        self.back_button = tk.Button(self, text = "Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady = 5)

        self.button1 = tk.Button(self, text="1", 
                                 command=lambda: self.button_clicked(1))
        self.button2 = tk.Button(self, text="2", 
                                 command=lambda: self.button_clicked(2))
        self.button3 = tk.Button(self, text="3", 
                                 command=lambda: self.button_clicked(3))
        self.button4 = tk.Button(self, text="4", 
                                 command=lambda: self.button_clicked(4))
        self.button5 = tk.Button(self, text="5", 
                                 command=lambda: self.button_clicked(5)) 
        self.button6 = tk.Button(self, text="6", 
                                 command=lambda: self.button_clicked(6))
        self.button7 = tk.Button(self, text="7", 
                                 command=lambda: self.button_clicked(7))
        self.button8 = tk.Button(self, text="8", 
                                 command=lambda: self.button_clicked(8))
        self.button9 = tk.Button(self, text="9", 
                                 command=lambda: self.button_clicked(9))
        self.button10 = tk.Button(self, text="10", 
                                  command=lambda: self.button_clicked(10))
    
        self.values = [self.button1, self.button2, self.button3, self.button4,
                         self.button5, self.button6, self.button7, self.button8, 
                         self.button9, self.button10]

        for i in range(10):
            self.values[i].pack(side= tk.LEFT, padx=5)
        
    def button_clicked(self, i, event=None):
        self.values[i-1].config(text=f"You selected button {i}")
        DIC["rating"] = str(i)
        self.update_calendar()

    def update_calendar(self):
        cal = self.controller.frames[CalendarPage]
        cal.update_calendar(datetime.date.today())

class QualPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)
        
class QuanPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

        self.label = tk.Label(self, text= rand_quote(load_quotes("csv/quantitative.csv", "Questions")))
        self.label.pack(pady=5)

        self.txt = tk.Text(self, height=10,
                             width=25)
        self.txt.pack()

        self.quote_button = tk.Button(self, text="Save",
                                        command=lambda: self.take_input(self.txt))
        self.quote_button.pack(pady=5)

        self.quote_button = tk.Button(self, text="New Quote",
                                      command=lambda: self.get_new_survey(self.label))
        self.quote_button.pack(pady=5)

    def get_new_survey(self, label):
        label.config(text=rand_quote(load_quotes("csv/quantitative.csv", "Questions")))

    def take_input(self, txt):
        inp = txt.get("1.0", "end-1c")
        txt.delete('1.0', tk.END)
        

class InspQuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

        self.label = tk.Label(self, text= rand_quote(load_quotes("csv/inspirational_quotes.csv", "Quote")))
        self.label.pack(pady=5)

        self.quote_button = tk.Button(self, text="New Quote",
                                      command=lambda: self.get_new_quote(self.label))
        self.quote_button.pack(pady=5)

    def get_new_quote(self, label):
        label.config(text=rand_quote(load_quotes("csv/inspirational_quotes.csv", "Quote")))


class EditPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)   

class TrendPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10) 

if __name__ == '__main__':
    app = App()
    app.mainloop()