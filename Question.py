from elements import QuElement


class Question(QuElement):
    def __init__(self, value : bool):
        self.is_qual = value
        # Question text  is determined later in the Survey class
        self.question_text = ""
        self.response_text = ""

    def checkQual(self):
        return self.is_qual

    def setQuestionText(self, new_question_text):
        self.question_text = new_question_text

    def getQuestionText(self):
        return self.question_text

    def setResponseText(self, new_response_text):
        self.response_text = new_response_text

    def getResponseText(self):
        return self.response_text
