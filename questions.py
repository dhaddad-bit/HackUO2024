import csv

quant_q = "CSV/quantitative.csv"
qual_q = "CSV/qualitative.csv"


d = {}

def read_q(filename, d, key):
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, fieldnames = key)
        headers = reader.fieldnames

        for i, value in enumerate(reader):
            v = value[0]
            print(d)

        return d


a = read_q(quant_q, d, ["questions"])
print(a)