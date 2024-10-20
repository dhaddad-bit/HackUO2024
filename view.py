import tkinter as tk
from tkinter import ttk
import elements

#from "elements.py" import Listener

LARGE_FONT = ("Veranda", 12)

class WellnessTracker(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = RateDay(container, self)
        #NOTIFY LISTENER QUESETION OPPENED
        self.frames[RateDay] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(RateDay)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class RateDay(tk.Frame):
    #
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="How are you feeling rn")
        label.pack(padx=10, pady=10)
        #Create Buttons for Mood Rating
        button_frame = tk.Frame(self)
        button1 = tk.Button(button_frame, text="1", command=lambda: self.button_clicked())
        button2 = tk.Button(button_frame, text="2", command=lambda: self.button_clicked())
        button3 = tk.Button(button_frame, text="3", command=lambda: self.button_clicked())
        button4 = tk.Button(button_frame, text="4", command=lambda: self.button_clicked())
        button5 = tk.Button(button_frame, text="5", command=lambda: self.button_clicked()) 
        button6 = tk.Button(button_frame, text="6", command=lambda: self.button_clicked())
        button7 = tk.Button(button_frame, text="7", command=lambda: self.button_clicked())
        button8 = tk.Button(button_frame, text="8", command=lambda: self.button_clicked())
        button9 = tk.Button(button_frame, text="9", command=lambda: self.button_clicked())
        button10 = tk.Button(button_frame, text="10", command=lambda: self.button_clicked())
        #Pack and display buttons)
        self.values = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10]
        for i in range(10):
            self.values[i].pack()
        button_frame.pack()

    def button_clicked(self, event=None):
        print("Button Clicked")
        buttonconfig("")
        
        #ADD LISTENER QUESTION ANSWERED
        

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
