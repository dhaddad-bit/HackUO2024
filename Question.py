class Question:
    def __init__(self, question_text, value : bool):
        self.is_qual = value
        # Question text  is determined later in the Survey class
        self.question_text = question_text
        self.response_text = ""

    def check_qual(self):
        return self.is_qual

    def set_question_text(self, new_question_text):
        self.question_text = new_question_text

    def get_question_text(self):
        return self.question_text

    def set_response_text(self, new_response_text):
        self.response_text = new_response_text

    def get_response_text(self):
        return self.response_text

    def __str__(self):
        return self.question_text

    def __repr__(self):
        return self.question_text