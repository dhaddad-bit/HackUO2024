from Question import Question
import csv

class Survey:
    def __init__(self, num_of_questions : int):
        self.num_of_questions = num_of_questions
        self.questions = []

    def Reader(Path : str, field : str) -> []:
    #returns a list of items from the csv in Path, returns the provided field by line in a list
        column = []
        file = open(Path, 'r')
        reader = csv.DictReader(file)
        for i in reader:
            column.append(i[field])
        return column