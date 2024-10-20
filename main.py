import Question
from view import *
from elements import QuElement, QuEvent, EventKindQuestion

first_q = Question(False)



def main():
    app = WellnessTracker()
    app.mainloop()
    print












class QuestionListener(Listener):
    def notify(self, event: QuEvent):
        if event.kind == EventKindQuestion.question_opened:
            print(f"Question opened: {event.q.getQuestionText()}")
        elif event.kind == EventKindQuestion.question_answered:
            print(f"Question answered: {event.q.getResponseText()}")
























        