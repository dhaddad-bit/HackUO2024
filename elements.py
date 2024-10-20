
from enum import Enum


class EventKindQuestion(Enum):

    no_question = 0
    question_opened = 1
    
    question_answered = 2

class QuEvent(object):
    def __init__(self, kind: "EventKindQuestion", question: "Question"):
        self.kind = kind
        self.q = question

    def __repr__(self):
        return f"QuestionEvent({self.kind},{self.q})"
    

class Listener(object):
    def notify(self, event: QuEvent):
        raise NotImplementedError("must implement notify")
    


class QuElement:
        """base class for question elements, supports model
        view controller depiction"""


        def __init__(self):
             self._listeners = []

        def add_listeners(self, listener: Listener):
             self._listeners.append(listener)


        def notify_all(self, event: QuEvent):
             for listeners in self.listeners:
                  listeners.notify(event)