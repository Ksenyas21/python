import sqlite3

FILENAME = 'student.db'


def getConnection():
    return sqlite3.connect(FILENAME)


def migrateTable():
    with getConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS students")
        cursor.execute("""CREATE TABLE students
                          (first_name text, last_name text, birthday date, education text, faculty text, specialty text,
                           avg_score int)
                       """)

def readData():
    with getConnection() as conn:
        cursor = conn.cursor()
        faculty = input('faculty - ')
        cursor.execute('SELECT MIN(avg_score), first_name FROM students WHERE faculty LIKE ?', (faculty,))
        print("Student with min score: ", cursor.fetchone())

        cursor.execute('SELECT COUNT(first_name) FROM students WHERE faculty LIKE ?', (faculty,))
        print("Sum of Students: ", cursor.fetchone()[0])


def inputData():
    with getConnection() as conn:
        cursor = conn.cursor()

        first_name = input('first_name: ')
        last_name = input('last_name: ')
        birthday = input('birthday (y.m.d): ')
        education = input('education: ')
        faculty = input('faculty: ')
        specialty = input('specialty: ')
        avg_score = int(input('avg_score: '))

        cursor.execute('INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (first_name, last_name, birthday, education, faculty, specialty, avg_score))


def processCommand(cmd):
    if cmd == 'exit':
        return False
    elif cmd == 'migrate':
        migrateTable()
    elif cmd == 'read':
        readData()
    elif cmd == 'write':
        inputData()
    else:
        print('Unknown command')

    return True


print('> Available commands: migrate, read, write, exit')

continueLoop = True
while continueLoop:
    command = input('> Enter command: ')
    continueLoop = processCommand(command)
