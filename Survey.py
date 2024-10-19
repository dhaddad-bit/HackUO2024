from Question import Question
import csv

class Survey:
    def __init__(self, num_of_questions : int):
        self.num_of_questions = num_of_questions
        self.questions = []

    def Reader(Path : str, field : str) -> []:

        column = []
        file = open(Path, 'r')
        reader = csv.DictReader(file)
        for i in reader:
            column.append(i[field])
        return column