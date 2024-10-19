import csv
import elements
import os



class InitQuestion(Question):
    def __init__(self, input, answer):
        

















def csv_file_exists(filename):
    """
    This function checks if a CSV file exists or not.
    :param filename: The name of the CSV file to check.
    :return: True if the file exists, False otherwise.
    """
    return os.path.exists(filename) and filename.endswith('.csv') 



    #read_word reads from csv file, takes a Words object
    # and turns ine into word, and appends to all.

def read_word(filename, lst: "Survey", key):
    """reads line in file converts to Word saves to Words.all"""
    if csv_file_exists(filename):
            
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames

            for line in reader:


                new = q_class(key)

                lst.append_main(new)#saving to .all
            return lst
    else:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['morpheme', 'grammar', 'unicode', 'pinyin', 'tone', 'eng_sig','score'])
            writer.writeheader()
            return lst

def q_class(key):
    for item in range(len(key)):


key=['time', 'answer']
def save_initq(question, filename, key):
    """rewrites a file with updated list of words"""
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, key)
        writer.writeheader()
        writer.writerows(question)


def save_initq(question, filename, key):
    """"""
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, key)
        if f.tell() == 0:           #find out more about tell
            writer.writeheader()  
        writer.writerow(question.to_dict())



 