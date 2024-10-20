import csv
import datetime
quant_q = "CSV/quantitative.csv"
quant_q_a = "CSV/quantitative_responses.csv"

qual_q = "CSV/qualitative.csv"

from Survey import Survey
s = Survey()

s.reader(quant_q)
s.reader(qual_q)


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
                elif title == 'question_#':
                    value = s.questions[int(value)]

                
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
            data_list.append((row_count, value))
            row_count += 1
        
    return data_list

def rand_quote(q_list: list):
    "used frequently with randint, and returns len(list) value"
    import random
    idx = len(q_list)
    rand = random.randint(0, idx-1)
    res = q_list[rand]
    return res

def save_inputs(words, filename):
    """appends a file with updated list of words"""
    with open(filename, 'a', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(words)


def inpt_as_number(input_string):
    from word2number import w2n

    """Takes quantitative input and extrapolates number value from entry"""
    input_list = input_string.split()
    #print(input_list)

    for i in input_list:
        try:
            return int(i)
        except ValueError:
            try:
                return w2n.word_to_num(i)
            except ValueError:
                raise ValueError(f"We were kind of looking for a quantitative answer, but '{i}' is not...\nDid you mean to write that?")
    
    raise ValueError(f"We were kind of looking for a quantitative answer, but '{i}' is not...\nDid you mean to write that?")

a = load_data(quant_q_a, ["date","question_#","response"])
print(a)