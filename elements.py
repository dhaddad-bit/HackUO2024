
from enum import Enum


class EventKindQuestion(Enum):

    question_opened = 1
    question_answered = 2

class QuEvent(object):
    def __init__(self, kind: EventKindQuestion, ):
        self.kind = kind
        self.