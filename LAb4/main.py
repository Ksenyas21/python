from datetime import date
from LAb4.Person import Person
from LAb4.Teather import Teacher
def professor():
    first_name = input('first name - ')
    last_name = input('last name - ')
    third_name = input('third name - ')
    birth = input('Date (Y,m,d) - ')
    faculty = input(' faculty - ')
    position = input('position - ')
    title = input('title - ')
    salary = int(input('salary - '))
    numbersOfCourses = int(input('numbersOfCourses -'))
    return Teacher(first_name, last_name, third_name, birth, faculty, position, title, salary, numbersOfCourses)
n= int(input('N = '))
Professors =[professor() for i in range(n)]
print(Professors)
faculty = input('faculty - ')
# Для заданого користувачем факультету обчисліть загальну кількість курсів,
# що читаються викладачами і середній вік викла дачів цього факультету.



most_popular = max(filter(lambda c:
                          c.faculty == faculty, Professors), key=lambda c: c.count())
