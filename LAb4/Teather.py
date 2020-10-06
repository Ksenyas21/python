from datetime import date
import math

from LAb4.Person import Person


class Teacher(Person):
    def __init__(self, firsName, lastName, thirdName, birth, faculty, position, title, salary, numbersOfCourses):
        super().__init__(firsName, lastName, thirdName, birth)
        self.faculty = faculty
        self.position = position
        self.title = title
        self.salary = salary
        self.numbersOfCourses = numbersOfCourses
    def count(self):
        return sum(self.numbersOfCourses)