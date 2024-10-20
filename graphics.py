import tkinter as tk 
import tkinter as ttk
#from questions import rand_quote


quant_q = "CSV/quantitative.csv"
qual_q = "CSV/qualitative.csv"


# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
#fig, ax = plt.subplots()




def create_ombre_1(canvas, width, height, color1, color2):
    # Function to create a vertical gradient (ombre) from color1 to color2
    r1, g1, b1 = canvas.ttk.winfo_rgb(color1)
    r2, g2, b2 = canvas.ttk.winfo_rgb(color2)

    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr // 256:02x}{ng // 256:02x}{nb // 256:02x}'
        canvas.create_line(0, i, width, i, fill=color)



root = tk.Tk()

rgb_value = root.winfo_rgb("lightblue")
print(rgb_value) 



# def create_ombre_2(canvas, width, height, colors):
#     # Function to create a vertical gradient (ombre) between multiple colors
#     num_sections = len(colors) - 1  # We create transitions between each adjacent pair of colors
#     section_height = height // num_sections

#     for section in range(num_sections):
#         color1 = colors[section]
#         color2 = colors[section + 1]

#         r1, g1, b1 = canvas.winfo_rgb(color1)
#         r2, g2, b2 = canvas.winfo_rgb(color2)

#         r_ratio = (r2 - r1) / section_height
#         g_ratio = (g2 - g1) / section_height
#         b_ratio = (b2 - b1) / section_height

#         for i in range(section_height):
#             nr = int(r1 + (r_ratio * i))
#             ng = int(g1 + (g_ratio * i))
#             nb = int(b1 + (b_ratio * i))
#             color = f'#{nr // 256:02x}{ng // 256:02x}{nb // 256:02x}'
#             y = section * section_height + i  # Calculate y-position for the current line
#             canvas.create_line(0, y, width, y, fill=color)



# root = tk.Tk()
# root.geometry("800x800")
# root.title("Ombre Background")

# canvas= root()

# # Create an ombre from light blue to light green
# create_ombre_1(canvas, 800, 800, "lightblue", "lightgreen")

# root.mainloop()


        self.button1 = tk.Button(self, text="1", foreground='white',
                                 command=lambda: self.button_clicked(1), background='SteelBlue4')
        self.button2 = tk.Button(self, text="2", foreground='white',
                                 command=lambda: self.button_clicked(2), background='SteelBlue3')
        self.button3 = tk.Button(self, text="3", foreground='white',
                                 command=lambda: self.button_clicked(3), background='SteelBlue2')
        self.button4 = tk.Button(self, text="4", foreground='white',
                                 command=lambda: self.button_clicked(4), background='SteelBlue1')
        self.button5 = tk.Button(self, text="5", foreground='white',
                                 command=lambda: self.button_clicked(5), bg = 'turquoise') 
        self.button6 = tk.Button(self, text="6", foreground='white',
                                 command=lambda: self.button_clicked(6), bg = 'aquamarine')
        self.button7 = tk.Button(self, text="7", foreground='white',
                                 command=lambda: self.button_clicked(7), bg = "SpringGreen1")
        self.button8 = tk.Button(self, text="8", foreground='white',
                                 command=lambda: self.button_clicked(8), bg = "SpringGreen2")
        self.button9 = tk.Button(self, text="9",foreground='white', 
                                 command=lambda: self.button_clicked(9), bg = "SpringGreen3")
        self.button10 = tk.Button(self, text="10", foreground='white',
                                  command=lambda: self.button_clicked(10), bg = "SpringGreen4")
    

"""now for trying to get a background image into the main"""

from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("800x600")

