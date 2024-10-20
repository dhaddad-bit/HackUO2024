import csv
import datetime

quant_q = "CSV/quantitative.csv"
qual_q = "CSV/qualitative.csv"

# from survey import Survey

def load_data(filename: str, column_titles: list) -> dict:

    data_list = []
    row_count = 0
    with open(filename) as open_file:
        csv_reader = csv.reader(open_file)
        header = next(csv_reader)
    
        for row in csv_reader:
            new_list = []

            for title in column_titles:
                value = row[header.index(title)]
                if title == 'date':
                    value = datetime.datetime.strptime(value, '%Y-%m-%d')
                new_list.append(value)

            data_tuple = tuple(new_list)
            data_list.append(data_tuple)
            row_count +=1
        
        return data_list
        
def load_quotes(filename: str, title) -> list:

    data_list = []
    row_count = 0
    with open(filename) as open_file:
        csv_reader = csv.reader(open_file)
        header = next(csv_reader)

        for row in csv_reader:
            value = row[header.index(title)]
            data_list.append(value)
            row_count += 1
        
    return data_list

def rand_quote(q_list: list):
    import random
    idx = len(q_list)
    rand = random.randint(0, idx-1)
    return q_list[rand]

