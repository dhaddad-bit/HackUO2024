import tkinter as tk
import tkinter.tix as tix
from tkinter import ttk

from tkcalendar import Calendar, DateEntry
import datetime

#root = tk.Tk()


#open new window (display events?)

# def create_cal():
#     cal = Calendar(root, font="Arial 14", cursor="hand1")

# #test dates
#     dates = [(datetime.date(2024, 10, 18), '5'), (datetime.date(2024, 10, 15), '7'),
#          (datetime.date(2024, 10, 17), '3'), (datetime.date(2024, 10, 16), '10')]
    
#     cal.bind("<<CalendarSelected>>", open_new_window(cal))
#     cal.pack(fill="both", expand=True)

# #tag configs
#     cal.tag_config('1', background='SteelBlue4', foreground='white')
#     cal.tag_config('2', background='SteelBlue3', foreground='white')
#     cal.tag_config('3', background='SteelBlue2', foreground='white')
#     cal.tag_config('4', background='SteelBlue1', foreground='white')
#     cal.tag_config('5', background='turquoise', foreground='white')
#     cal.tag_config('6', background='aquamarine', foreground='white')
#     cal.tag_config('7', background='SpringGreen1', foreground='white')
#     cal.tag_config('8', background='SpringGreen2', foreground='white')
#     cal.tag_config('9', background='SpringGreen3', foreground='white')
#     cal.tag_config('10', background="SpringGreen4", foreground='white')

# #testing-creating events from previous dates
#     for i in range(len(dates)):
#         cal.calevent_create(dates[i][0], text="Hey!", tags=dates[i][1])

DIC = {}

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, CalendarPage, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def store_data(event):
        dic = {}
        print("")

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10,padx=10)

        self.calendar_frame = None
        button = tk.Button(self, text="Calendar",
                            command=lambda: controller.show_frame(CalendarPage))

        button.pack()

        button = tk.Button(self, text="Page Two",
                           command=lambda: controller.show_frame(PageTwo))
        button.pack()

class CalendarPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Create a Calendar widget
        self.calendar = Calendar(self)
        self.calendar.bind("<<CalendarSelected>>", )
        self.calendar.pack(fill="both", expand=True)

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

        # Label to display the selected date
        self.date_label = tk.Label(self, text="")
        self.date_label.pack(pady=10)

        # Button to return to the main page
        self.back_button = tk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

    def open_new_window(self):
        new_window = tk.Toplevel(self)
        new_window.title("Hey!!")

        close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
        close_button.pack(pady=10)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Rate Your Day!")
        label.pack(pady=10,padx=10)

        self.back_button = tk.Button(self, text = "Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady = 10)

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
        print(DIC["rating"])
    

if __name__ == '__main__':
    app = App()
    app.mainloop()