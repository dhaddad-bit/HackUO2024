from importlib.metadata import files
from Question import Question
import random
import csv

location = 'CSV/qualitative.csv'
location2 = 'CSV/quantitative.csv'

class Survey:

    def __init__(self, num_of_questions : int, type : str):
        self.num_of_questions = num_of_questions
        self.type = type
        self.questions = []

    def reader(self, Path : str) -> [str]:
        column = []
        file = open(Path, 'r')
        reader = csv.reader(file)
        for row in reader:
            column.append(row)
        return column

    def field_reader(self, Path : str, field : str) -> [str]:
        column = []
        file = open(Path, 'r')
        reader = csv.reader(file)
        for row in reader:
            column.append(row[field])
        return column


    def writer(self, Path : str, update : str):
        file = open(Path, 'a+')
        w = csv.writer(file)
        w.writerow(update)
        file.close()

    def generateQuestions(self, questionPool):
        questionList = []

        for i in range(self.num_of_questions):
            index = random.randint(0, len(questionPool) - 1)
            questionList.append(questionPool[index][0])

        for i in range(self.num_of_questions):
            questionList[i] = Question(questionList[i], self.type == 'qualitative')

        return questionList

    def question_pool(self) -> [Question]:
        #gathers questions into a list initially as strings then it initializes and returns the question objects in a list
        pool = []

        if self.type == 'quantitative' or self.type == 'random':
            for i in range(self.num_of_questions):
                pool = self.reader(location2)
            return self.generateQuestions(pool)
        if self.type == 'qualitative' or self.type == 'random':
            for i in range(self.num_of_questions):
                pool = self.reader(location)
            return self.generateQuestions(pool)

    def add_question(self, question):
        self.questions.append(question)