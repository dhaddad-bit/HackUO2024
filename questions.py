import csv

quant_q = "CSV/quantitative.csv"
qual_q = "CSV/qualitative.csv"

from survey import Survey



def rand_quote(q_list: list):
    import random
    idx = len(q_list)
    rand = random.randint(0, idx-1)
    return q_list[rand]

        
