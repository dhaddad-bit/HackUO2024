import tkinter as tk 
import tkinter as ttk
from questions import rand_quote

from survey import Survey

quant_q = "CSV/quantitative.csv"
qual_q = "CSV/qualitative.csv"

root = tk.Tk
root.geometry("800x800")
root.title("my tini guy")



from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


#fig, ax = plt.subplots()
