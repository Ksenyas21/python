class Student:
    def __init__(self, first_name, last_name, birthday, education, faculty, specialty, avg_score):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.education = education
        self.faculty = faculty
        self.specialty = specialty
        self.avg_score = avg_score

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}' \
            .format(self.first_name, self.last_name, self.birthday.date(), self.education, self.faculty, self.specialty, self.avg_score)