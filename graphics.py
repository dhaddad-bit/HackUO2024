import tkinter as tk 
import tkinter as ttk
from questions import rand_quote

from survey import Survey

quant_q = "CSV/quantitative.csv"
qual_q = "CSV/qualitative.csv"

root = tk.Tk()
root.title("Personal Wellness Tracker")
k = "hey Josie love your hair"
btn = tk.Button(root, text="back to main page")
btn.pack()

k = tk.StringVar()
k.set(f"{k}")  # Set some initial text

txtbox = ttk.Entry(root, width=50, text=k)
txtbox.pack("top")

class RandSurvey(tk, ):
# #Create TK window object
# def random_survey(parent, data_1, data_2):
#     s = Survey()
#     s.reader(data_1)
#     s.reader(data_2)
#     btn = tk.Button(root, text="back to main page")
#     btn.pack()
#     while True:
#         q = rand_quote(s.questions)
#         print(q)
#         # txtbox = ttk.Entry(parent, q)
#         # txtbox.pack("top")




class InspQuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        self.back_button = tk.Button(self, text="Back to Main Page",
                                     command=lambda: controller.show_frame(StartPage))
        self.back_button.pack(pady=10)

        self.label = tk.Label(self, text= rand_quote(s.quant))
        self.label.pack(pady=5)

        self.quote_button = tk.Button(self, text="New Quote",
                                      command=lambda: self.get_new_quote(self.label))
        self.quote_button.pack(pady=5)

    def get_new_survey(self, label):
        label.config(text=rand_quote(s.quant))
# # random_survey(root, qual_q, quant_q)

# s = Survey()
# s.reader(qual_q)
# s.reader(quant_q)
# q = rand_quote(s.questions)