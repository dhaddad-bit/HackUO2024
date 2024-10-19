from Question import Question
import csv

class Survey:


    def __init__(self, num_of_questions):
        self.num_of_questions = num_of_questions
        self.questions = []



    def Question_pool(num_of_questions : int):
        result = {}
        file = open(PATH, 'r')
        reader = csv.DictReader(file)
        for row in reader:
            read_csv_column(file, "key_field")
        return result
