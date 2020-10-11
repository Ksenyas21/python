import shelve
from datetime import datetime
from LAB_5.Student import Student

FILENAME = "students_data"


def printData():
    try:
        with shelve.open(FILENAME) as db:
            students = db.values()

            student_min_score = min(students, key=lambda s: float(s.avg_score))

            if students:
                print('Student with min Score: ', student_min_score)
                print('Students: ', len(students))
            else:
                print('Database is empty')
    except FileNotFoundError:
        print('Database file not found')


def inputData():
    first_name = input('first_name: ')
    last_name = input('last_name: ')
    birthday = input('birthday (y.m.d): ').split('.')
    education = input('education: ')
    faculty = input('faculty: ')
    specialty = input('specialty: ')
    avg_score = input('avg_score: ')

    student = Student(
        first_name,
        last_name,
        datetime(year=int(birthday[0]), month=int(birthday[1]), day=int(birthday[2])),
        education,
        faculty,
        specialty,
        float(avg_score)
    )

    with shelve.open(FILENAME) as students:
        students[str(hash(student))] = student

    print('Record saved')


def processCommand(cmd):
    if cmd == 'exit':
        return False
    elif cmd == 'read':
        printData()
    elif cmd == 'write':
        inputData()
    else:
        print('Unknown command')

    return True


print('> Available commands: read, write, exit')

continueLoop = True
while continueLoop:
    command = input('> Enter command: ')
    continueLoop = processCommand(command)
