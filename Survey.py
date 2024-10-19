from Question import Question
import csv

class Survey_All:
    def __init__(self, num_of_questions : int):
        self.num_of_questions = num_of_questions
        self.questions = []

    def Reader(Path : str) -> []:
        result = []
        file = open(Path, 'r')
        reader = csv.DictReader(file)
        for row in reader:
            result.append(row)
        return result
    
    def __str__(self):
        return self.questions
    

class Survey:
    def __init__(self, question, answer, quant_qual):
        self.question = question        
        self.answer = answer
        self.q = quant_qual

    def checker(self):
        


    def __str__(self):
        return f"{self.question}:\n{self.answer}"

    



def load_questions(filename, survey_all):
    with open(filename):
        reader = csv.DictReader()
        #check if value is quanti