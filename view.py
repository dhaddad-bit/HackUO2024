import tkinter as tk
from tkinter import ttk
from elements import *


#from "elements.py" import Listener

LARGE_FONT = ("Veranda", 12)

class WellnessTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wellness Tracker")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.geometry("800x500")

        #Rating of mood Frame
        rating = RateDay(self)
        rating.grid(column=1, padx=5, pady=5)
        
        menu = Menu(self)
        menu.grid(column=0, row=0, sticky="w")

    # def show_frame(self, cont):
    #     frame = self.frames[cont]
    #     frame.tkraise()

    def notify(self, event: QuElement):
        pass

class Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.open_survey = tk.Button(text="Open Survey")
        self.open_survey.grid(row=0, column=0)

class RateDay(tk.Frame):
    #
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="How are you feeling rn")
        label.grid(padx=10, pady=10)
        #Create Buttons for Mood Rating
        self.button1 = tk.Button(self, text="1", command=lambda: self.button_clicked(1))
        self.button2 = tk.Button(self, text="2", command=lambda: self.button_clicked(2))
        self.button3 = tk.Button(self, text="3", command=lambda: self.button_clicked(3))
        self.button4 = tk.Button(self, text="4", command=lambda: self.button_clicked(4))
        self.button5 = tk.Button(self, text="5", command=lambda: self.button_clicked(5)) 
        self.button6 = tk.Button(self, text="6", command=lambda: self.button_clicked(6))
        self.button7 = tk.Button(self, text="7", command=lambda: self.button_clicked(7))
        self.button8 = tk.Button(self, text="8", command=lambda: self.button_clicked(8))
        self.button9 = tk.Button(self, text="9", command=lambda: self.button_clicked(9))
        self.button10 = tk.Button(self, text="10", command=lambda: self.button_clicked(10))

        #Pack and display buttons)
        self.values = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9, self.button10]
        for i in range(10):
            self.values[i].grid(column=0, row=i+1)

    def button_clicked(self, i, event=None):
        self.values[i-1].config(text=f"You selected button {i}")
        event = QuEvent(EventKindQuestion.question_answered, i)
        event.notify_all() # Notify
        self.destroy()

        #ADD LISTENER QUESTION ANSWERED

    def notify(self, event: QuElement):
        pass

        #Send info to where mood ratings are stored


        
if __name__ == "__main__":
    app = WellnessTracker()
    app.mainloop()



# #Create TK window object



# daily_rating = tk.Frame(root)
# daily_rating.columnconfigure(0, weight=1)
# daily_rating.rowconfigure(0, weight=3)
# mood_score = tk.Entry.daily_rating()

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# frame = tk.Frame(root)
# frame.grid(row=0, column=0, sticky="nsew")
# frame.columnconfigure(0, weight=1)
# frame.rowconfigure(1, weight=1)


# #Create a frame
# entry = tk.Entry(frame)
# entry.grid(row=0, column=0, sticky="ew")

# #Add stuff to frames
# entry_btn = tk.Button(frame, text="Add")
# entry_btn.grid(row=0, column=1)

# lbl = tk.Label(root, text="Label of root")
# lbl.grid()

# btn = tk.Button(root, text="Button 1")
# btn.grid()


# root.mainloop()
