import tkinter as tk
import tkinter.tix as tix
from tkinter import ttk

#from survey import Survey
from tkcalendar import Calendar, DateEntry
import datetime
from PIL import Image, ImageTk

#plot imports
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

import csv
import word2number

from questions import *

DIC = {}

PAST_RATES = load_data("csv/rate_day.csv", ["date", "rating"])
QUANT_RES = load_data("csv/quantitative_responses.csv", ["date", "question_#", "response"])
QUALT_RES = load_data("csv/qualitative_responses.csv", ["date", "question_#", "response"])
CURRENT_QNT_RES = {}

LARGE_FONT = ("Comic Sans", 14, "bold")
OVERLAY = ['./overlay/pic_1.jpg', './overlay/pic_2.jpg', './overlay/pic_3.jpg', './overlay/pic_4.jpg', './overlay/pic_5.jpg', './overlay/pic_6.jpg']

a = rand_quote(OVERLAY)

class App(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("700x750")
        container = tk.Frame(self, width=700, height=800)

        container.pack(side="top", fill="both", expand = True)
        container.grid_propagate(False)


        self.image = Image.open(a)
        self.python_image = ImageTk.PhotoImage(self.image)

        ttk.Label(self, image=self.python_image).pack()
        # self.image.pack()

        # container.pack(side="top", fill="both", expand = True)
        # container.grid_propagate(False)

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
        label = tk.Label(self, text="Welcome!", font=LARGE_FONT)
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

        button = tk.Button(self, text="Trends",
                            command=lambda: controller.show_frame(TrendPage))
        button.pack(pady=10)

        button = tk.Button(self, text="Add New Questions",
                            command=lambda: controller.show_frame(EditPage))
        button.pack(pady=10)

        image = Image.open(a)  # Provide the path to your image
        self.photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=self.photo)
        image_label.pack(pady=10)


class CalendarPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        #label for calendar
        self.label = tk.Label(self, text="CALENDAR")
        self.label.pack(pady=10)

        self.d_qn = {}
        self.d_ql = {}

        # Create a Calendar widget
        self.calendar = Calendar(self, date_pattern="yyyy-mm-dd")
        self.calendar.bind("<<CalendarSelected>>", self.open_new_window)
        self.calendar.pack(fill="both", expand=True)

        for i in range(len(PAST_RATES)):
            self.calendar.calevent_create(date=PAST_RATES[i][0], text="", tags=PAST_RATES[i][1])
        
        for i in range(len(QUANT_RES)):
            time = QUANT_RES[i][0].strftime("%Y-%m-%d")
            if time in self.d_qn.keys():
                self.d_qn[time].append((QUANT_RES[i][1], QUANT_RES[i][2]))
            else:
                self.d_qn[time] = []
                self.d_qn[time].append((QUANT_RES[i][1], QUANT_RES[i][2]))

        for i in range(len(QUALT_RES)):
            time = QUALT_RES[i][0].strftime("%Y-%m-%d")
            if time in self.d_qn.keys():
                self.d_qn[time].append((QUALT_RES[i][1], QUALT_RES[i][2]))
            else:
                self.d_qn[time] = []
                self.d_qn[time].append((QUALT_RES[i][1], QUALT_RES[i][2]))
        
        self.calendar.tag_config('1', background='SteelBlue4', foreground='black')
        self.calendar.tag_config('2', background='SteelBlue3', foreground='black')
        self.calendar.tag_config('3', background='SteelBlue2', foreground='black')
        self.calendar.tag_config('4', background='SteelBlue1', foreground='black')
        self.calendar.tag_config('5', background='turquoise', foreground='black')
        self.calendar.tag_config('6', background='aquamarine', foreground='black')
        self.calendar.tag_config('7', background='SpringGreen1', foreground='black')
        self.calendar.tag_config('8', background='SpringGreen2', foreground='black')
        self.calendar.tag_config('9', background='SpringGreen3', foreground='black')
        self.calendar.tag_config('10', background="SpringGreen4", foreground='black')

        #button to return to the main page
        self.back_button = tk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

    def open_new_window(self, event):
        date = self.calendar.get_date()

        new_window = tk.Toplevel(self)

        self.label = tk.Label(new_window, text="Numerical Check-Ins")
        self.label.pack()
        if date in self.d_qn.keys():
            for i in range(len(self.d_qn[date])):
                tup = self.d_qn[date][i]
                self.label = tk.Label(new_window, text=tup[0])
                self.label.pack()
                self.label = tk.Label(new_window, text=tup[1])
                self.label.pack()
        else:
            self.label = tk.Label(new_window, text="Empty")
            self.label.pack()

        self.label = tk.Label(new_window, text= "Short Answer Check-Ins")
        self.label.pack()
        if date in self.d_ql.keys():
            for i in range(len(self.d_ql[date])):
                tup = self.d_ql[date][i]
                self.label = tk.Label(new_window, text=tup[0])
                self.label.pack()
                self.label = tk.Label(new_window, text=tup[1])
                self.label.pack()
        else:
            self.label = tk.Label(new_window, text="Empty")
            self.label.pack()

        close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
        close_button.pack(pady=10)

    def update_calendar(self, date, typ=None, q=None, r=None):
        if typ == "rate":
            self.calendar.calevent_create(date, text="", tags=DIC["rating"])
        if typ == "qn":
            if date in self.d_qn.keys():
                self.d_qn[date].append((q, r))
            else:
                self.d_qn[date] = []
                self.d_qn[date].append((q, r))
        if typ == "ql":
            if date in self.d_ql.keys():
                self.d_ql[date].append((q, r))
            else:
                self.d_ql[date] = []
                self.d_ql[date].append((q, r))

class RateDayPage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Rate Your Day!")
        label.pack(pady=10,padx=10)

        self.back_button = tk.Button(self, text = "Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady = 5)

     
        self.button1 = tk.Button(self, text="1", foreground='black',
                                 command=lambda: self.button_clicked(1), background='SteelBlue4')
        self.button2 = tk.Button(self, text="2", foreground='black',
                                 command=lambda: self.button_clicked(2), background='SteelBlue3')
        self.button3 = tk.Button(self, text="3", foreground='black',
                                 command=lambda: self.button_clicked(3), background='SteelBlue2')
        self.button4 = tk.Button(self, text="4", foreground='black',
                                 command=lambda: self.button_clicked(4), background='SteelBlue1')
        self.button5 = tk.Button(self, text="5", foreground='black',
                                 command=lambda: self.button_clicked(5), bg = 'turquoise') 
        self.button6 = tk.Button(self, text="6", foreground='black',
                                 command=lambda: self.button_clicked(6), bg = 'aquamarine')
        self.button7 = tk.Button(self, text="7", foreground='black',
                                 command=lambda: self.button_clicked(7), bg = "SpringGreen1")
        self.button8 = tk.Button(self, text="8", foreground='black',
                                 command=lambda: self.button_clicked(8), bg = "SpringGreen2")
        self.button9 = tk.Button(self, text="9",foreground='black', 
                                 command=lambda: self.button_clicked(9), bg = "SpringGreen3")
        self.button10 = tk.Button(self, text="10", foreground='black',
                                  command=lambda: self.button_clicked(10), bg = "SpringGreen4")

    
        self.values = [self.button1, self.button2, self.button3, self.button4,
                         self.button5, self.button6, self.button7, self.button8, 
                         self.button9, self.button10]

        for i in range(10):
            self.values[i].pack(side= tk.LEFT, padx=5)
        
    def button_clicked(self, i, event=None):
        self.values[i-1].config(text=f"You selected button {i}")
        DIC["rating"] = str(i)
        self.update_calendar()

        date = datetime.datetime.today().strftime("%Y-%m-%d")

        if search_headercolumn("csv/rate_day.csv", 0, date):
            inp = [date, i]
            replace_line("csv/rate_day.csv", search_headercolumn("csv/rate_day.csv", 0, date)[1], inp)
        else:
            save_inputs([date, i], "csv/rate_day.csv")


    def update_calendar(self):
        cal = self.controller.frames[CalendarPage]
        cal.update_calendar(datetime.date.today(), typ="rate")

class QualPage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller

        tk.Frame.__init__(self, parent)

        self.res_dict = {}

    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

        self.question = rand_quote(load_quotes("csv/qualitative.csv", "Questions"))
        self.label = tk.Label(self, text=self.question[1])
        self.label.pack(pady=5)

        self.txt = tk.Text(self, height=10,
                             width=25)
        self.txt.pack()

        self.quote_button = tk.Button(self, text="Save",
                                        command=lambda: self.take_input(self.txt))
        self.quote_button.pack(pady=5)

        self.quote_button = tk.Button(self, text="New Question",
                                      command=lambda: self.get_new_survey(self.label))
        self.quote_button.pack(pady=5)

    def get_new_survey(self, label):

        if len(self.res_dict[self.question[1]]) > 0:
            res = self.res_dict[self.question[1]]
            csv_inp = [datetime.date.today().strftime("%Y-%m-%d"), self.question[0], res]
            save_inputs(csv_inp, "csv/qualitative_responses.csv")
            self.update_calendar(r=res, q=self.question[1])


        self.question = rand_quote(load_quotes("csv/qualitative.csv", "Questions"))
        label.config(text = self.question[1])

    def take_input(self, txt):
        self.inp = txt.get("1.0", "end-1c")
        self.res_dict[self.question[1]] = self.inp
        txt.delete('1.0', tk.END)

    def update_calendar(self, typ="ql", q=None, r=None):
        cal = self.controller.frames[CalendarPage]
        cal.update_calendar(datetime.date.today(), typ="ql", q=q, r=r)


        
class QuanPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller

        tk.Frame.__init__(self, parent)

        self.res_dict = {}

        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

        self.question = rand_quote(load_quotes("csv/quantitative.csv", "Questions"))
        self.label = tk.Label(self, text=self.question[1], bg="light blue")
        self.label.pack(pady=5)

        self.txt = tk.Text(self, height=5,
                             width=25)
        self.txt.pack()

        self.quote_button = tk.Button(self, text="Save",
                                        command=lambda: self.take_input(self.txt))
        self.quote_button.pack(pady=5)

        self.quote_button = tk.Button(self, text="New Question",
                                      command=lambda: self.get_new_survey(self.label))
        self.quote_button.pack(pady=5)

    def get_new_survey(self, label):

        if self.res_dict[self.question[1]] > 0:
            res = self.res_dict[self.question[1]]
            csv_inp = [datetime.date.today().strftime("%Y-%m-%d"), self.question[0], res]
            save_inputs(csv_inp, "csv/quantitative_responses.csv")
            self.update_calendar(r=res, q=self.question[1])

        self.question = rand_quote(load_quotes("csv/quantitative.csv", "Questions"))
        label.config(text = self.question[1])


    def take_input(self, txt):
        self.inp = txt.get("1.0", "end-1c")
        self.inp = inpt_as_number(self.inp)
        self.res_dict[self.question[1]] = self.inp
        txt.delete('1.0', tk.END)

    def update_calendar(self, typ="qn", q=None, r=None):
        cal = self.controller.frames[CalendarPage]
        cal.update_calendar(datetime.date.today(), typ=typ, q=q, r=r)


class InspQuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

        self.label = tk.Label(self, text= rand_quote(load_quotes("csv/inspirational_quotes.csv", "Quote"))[1])
        self.label.pack(pady=5)

        self.quote_button = tk.Button(self, text="New Quote",
                                      command=lambda: self.get_new_quote(self.label))
        self.quote_button.pack(pady=5)

    def get_new_quote(self, label):
        label.config(text=rand_quote(load_quotes("csv/inspirational_quotes.csv", "Quote"))[1])


class EditPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

        self.label = tk.Label(self, text="ADD YOUR OWN QUESTIONS")  
        self.label.pack(pady=5) 

        self.label = tk.Label(self, text="Enter New Numerical Check-In")
        self.label.pack(pady=5)

        self.qnq_text = tk.Text(self, height=5, width=25)
        self.qnq_text.pack(pady=5)

        self.save_button = tk.Button(self, text="Add Question",
                                     command=lambda: self.save_to_q("num"))
        self.save_button.pack(pady=10)

        self.label = tk.Label(self, text="Enter New Short Answer Check-In")
        self.label.pack(pady=5)

        self.qlq_text = tk.Text(self, height=5, width=25)
        self.qlq_text.pack(pady=5)

        self.save_button = tk.Button(self, text="Add Question",
                                     command=lambda: self.save_to_q("wri"))
        self.save_button.pack(pady=10)
    
    def save_to_q(self, typ):
        if typ == "num":
            txt = self.qnq_text.get("1.0", "end-1c")
            save_inputs([txt], "csv/quantitave.csv")
            self.qnq_text.delete('1.0', tk.END)
        elif typ == "wri":
            txt = self.qlq_text.get("1.0", "end-1c")
            save_inputs([txt], "csv/qualitative.csv")
            self.qnq_text.delete('1.0', tk.END)


class TrendPage(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10) 

        self.plot_button = tk.Button(master = self, command = lambda: self.plot_q_data("CSV/rate_day.csv", ["date", "rating"]),
                     height = 2, 
                     width = 10,
                     text = "Plot Rate Day")
        self.plot_button.pack(pady=10)

        self.plot_numerical_button = tk.Button(master=self, command = lambda: self.plot_q_data())
        self.plot_numerical_button.pack(pady=10)

     def plot_q_data(self, file_name: str, column_titles: list):
        # Creating Figure Widget
        fig = Figure(figsize = (5, 5))
        # Pull Ratings from File
        data_list = sorted(load_data(file_name, column_titles)) #Sort by datetime
        y = [data_list[i][0] for i in range(len(data_list))]
        dates = [int(data_list[i][1]) for i in range(len(data_list))]
        #print(data_list)

        # Adding plots
        plot1 = fig.add_subplot()

        plot1.plot(y, dates)
        plot1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

        # Creating canvass using FigureCanvasTkAgg()
        canvas = FigureCanvasTkAgg(fig,
                               master = self)  
        canvas.draw()

        canvas.get_tk_widget().pack()

        # Creating Toolbar using Matplotlib
        toolbar = NavigationToolbar2Tk(canvas,
                                   self)
        toolbar.update()

        canvas.get_tk_widget().pack()



if __name__ == '__main__':
    app = App()
    app.mainloop()