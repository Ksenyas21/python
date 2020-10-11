from datetime import datetime
import math
class Person():

    def __init__(self, firsName, lastName, thirdName, birth):
        self.firsName = firsName
        self.lastName = lastName
        self.thirdName = thirdName
        self.birth = datetime.strptime(birth, '%Y,%m,%d')

    def printDAta(self):
        name = str(self.firsName + ' ' + self.lastName + ' ' + self.thirdName)
        return name.title()

    def calculate_age(self):
        today = datetime.today()
        return today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))

