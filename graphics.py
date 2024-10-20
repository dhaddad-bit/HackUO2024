import tkinter as tk 
import tkinter as ttk
from questions import rand_quote

from survey import Survey

quant_q = "CSV/quantitative.csv"
qual_q = "CSV/qualitative.csv"

root = tk.Tk()
root.geometry("800x800")
root.title("my tini guy")
root.configure(bg="lightblue")


root.mainloop()

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
#fig, ax = plt.subplots()


def save_updated_word(words, filename):
    """rewrites a file with updated list of words"""
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['morpheme', 'grammar', 'unicode', 'pinyin', 'tone', 'eng_sig', 'score'])
        writer.writeheader()
        writer.writerows(words)