class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    def calculate(self):
        avg = float(sum(self.scores))/len(self.scores)
        if avg < 40 :
            return 'T'
        elif avg < 55:
            return 'D'
        elif avg < 70 :
            return 'P'
        elif avg < 80 :
            return 'A'
        elif avg < 90 :
            return 'E'
        elif avg <= 100:
            return 'O'
        