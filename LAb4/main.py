from datetime import date
from LAb4.Person import Person
from LAb4.Teather import Teacher

def setupProfessor():
    first_name = input('first name - ')
    last_name = input('last name - ')
    third_name = input('third name - ')
    birth = input('Date (Y,m,d) - ')
    faculty = input(' faculty - ')
    position = input('position - ')
    title = input('title - ')
    salary = int(input('salary - '))
    numbersOfCourses = int(input('numbersOfCourses - '))
    print('\n')
    return Teacher(first_name, last_name, third_name, birth, faculty, position, title, salary, numbersOfCourses)

n = int(input('N = '))
print('\n')

professorsArray = [setupProfessor() for i in range(n)]

faculty = input('faculty - ')
countCourses = 0
birthAvg = 0
birthAvgArray = []

for j in range(len(professorsArray)):
    if professorsArray[j].getFaculty() == faculty:
        countCourses = professorsArray[j].countNumberOfCourses(countCourses)
        birthAvgArray.append(professorsArray[j].calculate_age())

birthAvg = sum(birthAvgArray) / len(birthAvgArray)

print(' count courses', countCourses)
print('birth average', birthAvg)