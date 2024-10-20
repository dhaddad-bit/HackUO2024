import tkinter as tk 
import tkinter as ttk

from survey import Survey

quant_q = "CSV/quantitative.csv"
qual_q = "CSV/qualitative.csv"


#Create TK window object
def random_survey(parent, data_1, data_2):
    s = Survey()
    s.reader(data_1)
    s.reader(data_2)
    root = tk.Tk()
    root.title("Personal Wellness Tracker")
    txtbox = ttk.Entry(parent, )
    btn = tk.Button(root, text="back to main page")
    btn.pack()


    root.mainloop()

random_survey(qual_q, quant_q)
