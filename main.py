from Survey import Survey
from elements import Listener, EventKindQuestion, QuEvent
from view import WellnessTracker

s = Survey(10, 'quantitative')
print(s.question_pool())


def main():
    app = WellnessTracker() 
    
     










class ConsoleListener(Listener):
    def notify(self, event: QuEvent):
        if event.kind == EventKindQuestion.question_opened:
            print(f"Question opened: {event.q.getQuestionText()}")
        elif event.kind == EventKindQuestion.question_answered:
            print(f"Question answered: {event.q.getResponseText()}")






















#def init_