from view import *




def main():
    app = WellnessTracker()
    app.mainloop()
    print
=======
from survey import Survey
from view import WellnessTracker

s = Survey(10, 'quantitative')
print(s.question_pool())


def main():
    s = Survey() 
    s.reader(location)
    s.reader(location2)
































#def init_