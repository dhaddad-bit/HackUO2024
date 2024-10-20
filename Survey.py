from importlib.metadata import files
from question import Question
import random
import csv

location = 'CSV/qualitative.csv'
location2 = 'CSV/quantitative.csv'


class Survey:

    def __init__(self, num_of_questions: int=0, survey_type: str = "random"):
        self.questions = []
        #self.qual = []
        #self.quant = []
        self.survey_type = survey_type
        self.num_of_questions = num_of_questions
        
    def find_num(self):
        i = 0
        for item in range(len(self.questions)):
            i +=1
        self.num_of_questions = i

    def total_q(self):
        return f"{self.num_of_questions}"
        
    def __str__(self):
        txt = "\n".join(f"{self.questions[i]}" for i in range(self.num_of_questions))
        print(txt)
        return f"{self.questions}"


            
    

    def reader(self, path: str):
        """Read question from a CSV file and appends to survey lists."""
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                question = row[0]  # Assuming first column is the question text
                # if qual:
                #     self.qual.append(question)
                # else:
                #     self.quant.append(question)
                self.questions.append(question)

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

    def question_pool(self) -> list[Question]:
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


    def filter_questions(self, keyword: str) -> list:
        """Returns a list of questions containing the specified keyword."""
        return [q for q in self.questions if keyword in q]


s = Survey()

s.reader(location)
s.reader(location2)
s.find_num()
print(s.questions)
print(s.num_of_questions)