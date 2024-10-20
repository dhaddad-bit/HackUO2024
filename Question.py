from elements import QuElement, QuEvent, EventKindQuestion


class Question(QuElement):

    def __init__(self, question_text, value : bool):
        super.__init__()
        self.is_qual = value
        # Question text  is determined later in the Survey class
        self.question_text = question_text
        self.response_text = ""

    def check_qual(self):
        return self.is_qual

    def set_question_text(self, new_question_text):
        self.question_text = new_question_text
        event = QuEvent(EventKindQuestion.question_opened, self)  
        self.notify_all(event)  # Notify all listeners that a question has been opened


    def get_question_text(self):
        return self.question_text

    def set_response_text(self, new_response_text):
        self.response_text = new_response_text
        event = QuEvent(EventKindQuestion.question_answered, self)  
        self.notify_all(event)  

    def get_response_text(self):
        return self.response_text

    def __str__(self):
        return self.question_text

    def __repr__(self):
        return self.question_text