<<<<<<< HEAD
import Question
from view import *
from elements import QuElement, QuEvent, EventKindQuestion

first_q = Question(False)
Question.


def main():
    app = WellnessTracker()
    app.mainloop()
    print
=======
from Survey import Survey
from view import WellnessTracker

s = Survey(10, 'quantitative')
print(s.question_pool())


def main():
    #app = WellnessTracker() 
>>>>>>> 6762cf08560808f2166d75ff38fef3de9398c912












class QuestionListener(Listener):
    def notify(self, event: QuEvent):
        if event.kind == EventKindQuestion.question_opened:
            print(f"Question opened: {event.q.getQuestionText()}")
        elif event.kind == EventKindQuestion.question_answered:
            print(f"Question answered: {event.q.getResponseText()}")

























#def init_