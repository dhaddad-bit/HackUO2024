from Question import Question
import csv

class Survey:


    def __init__(self, num_of_questions):
        self.num_of_questions = num_of_questions
        self.questions = []



    def Reader(Path : str) -> []:
        result = []
        file = open(Path, 'r')
        reader = csv.DictReader(file)
        for row in reader:
            result.append(row)
        return result
