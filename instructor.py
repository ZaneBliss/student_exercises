from exercise import Exercise

class Instructor():
    
    def __init__(self, fname, lname, slack, cohort, specialty):
        self.fname = fname
        self.lname = lname
        self.slack = slack
        self.cohort = cohort
        self.specialty = specialty

    def assignExercise(self, student, exercise):
        student.exercises.append(exercise)
    