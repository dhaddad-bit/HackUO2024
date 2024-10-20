import tkinter as tk 
import tkinter as ttk
#from questions import rand_quote


quant_q = "CSV/quantitative.csv"
qual_q = "CSV/qualitative.csv"


# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
#fig, ax = plt.subplots()


# def save_updated_word(words, filename):
#     """rewrites a file with updated list of words"""
#     with open(filename, 'w', encoding='utf-8', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=['morpheme', 'grammar', 'unicode', 'pinyin', 'tone', 'eng_sig', 'score'])
#         writer.writeheader()
#         writer.writerows(words)



# def create_ombre_1(canvas, width, height, color1, color2):
#     # Function to create a vertical gradient (ombre) from color1 to color2
#     r1, g1, b1 = canvas.tk.winfo_rgb(color1)
#     r2, g2, b2 = canvas.tk.winfo_rgb(color2)

#     r_ratio = (r2 - r1) / height
#     g_ratio = (g2 - g1) / height
#     b_ratio = (b2 - b1) / height

#     for i in range(height):
#         nr = int(r1 + (r_ratio * i))
#         ng = int(g1 + (g_ratio * i))
#         nb = int(b1 + (b_ratio * i))
#         color = f'#{nr // 256:02x}{ng // 256:02x}{nb // 256:02x}'
#         canvas.create_line(0, i, width, i, fill=color)



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



# # Create an ombre from light blue to light green
# create_ombre_1(canvas, 800, 800, "lightblue", "lightgreen")

# root.mainloop()


p = "twenty imes"
from word2number import w2n

def inpt_as_number(input_string):
    """Takes quantitative input and extrapolates number value from entry"""
    input_list = input_string.split()
    print(input_list)

    for i in input_list:
        try:
            return int(i)
        except ValueError:
            try:
                return w2n.word_to_num(i)
            except ValueError:
                raise ValueError(f"We were kind of looking for a quantitative answer, but '{i}' is not...\nDid you mean to write that?")
    
    raise ValueError(f"We were kind of looking for a quantitative answer, but '{i}' is not...\nDid you mean to write that?")

print(inpt_as_number(p))