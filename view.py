import tkinter as tk
from tkinter import ttk

#Create TK window object
root = tk.Tk()
root.title("Personal Wellness Tracker")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)


#Create a frame
entry = tk.Entry(frame)
entry.grid(row=0, column=0, sticky="ew")

#Add stuff to frames
entry_btn = tk.Button(frame, text="Add")
entry_btn.grid(row=0, column=1)

lbl = tk.Label(root, text="Label of root")
lbl.grid()

btn = tk.Button(root, text="Button 1")
btn.grid()


root.mainloop()
