import statistics
student_list = []
lecturer_list = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress or course in self.finished_courses \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_grade(self):
        _sum = 0
        for value in self.grades.values():
            for i in range(len(value)):
                _sum += value[i]
            res_ = _sum / (len(value) * 2)
        return res_

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнии задания: {self.middle_grade()}\n' \
              f'Курсы в процессе изучения: {"".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {"".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        return self.middle_grade() < other.middle_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        lecturer_list.append(self)

    def mid_grade(self):
        _sum = 0
        for value in self.grades.values():
            for i in range(len(value)):
                _sum += value[i]
            res_ = _sum / (len(value) * 2)
        return res_

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_grade()}'
        return res

    def __lt__(self, other):
        return self.mid_grade() < other.mid_grade()


class Reviewers(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def mid_all_lc_grade(lecturer_list=lecturer_list, course='Git'):
    res = []
    for lecturer in lecturer_list:
        if course in lecturer.grades.keys():
            for values in lecturer.grades.values():
                res += values
    return f'Средний балл лекторов по лекции {course}: {statistics.fmean(res)}'

def mid_all_st_grade(student_list=student_list, course='Python'):
    res = []
    for student in student_list:
        if course in student.grades.keys():
            for values in student.grades.values():
                res += values
    return f'Средний балл студентов по лекции {course}: {statistics.fmean(res)}'

#Students
best_student = Student('Ruoy', 'Eman', 'м')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = []
best_student.grades['Python'] = []

second_student = Student('Petr', 'Uchenikov', 'м')
second_student.finished_courses += ['Git']
second_student.courses_in_progress += ['Python']
second_student.grades['Git'] = []
second_student.grades['Python'] = []


#Reviewers
cool_reviewer = Reviewers('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

second_reviewer = Reviewers('Ivan', 'Proveryalov')
second_reviewer.courses_attached += ['Git']


#Lecturer
cool_lecturer = Lecturer('Alexey', 'Chitalov')
cool_lecturer.courses_attached = ['Git']

second_lecturer = Lecturer('Yan', 'Gramotnov')
second_lecturer.courses_attached = ['Python']


#Студенты
best_student.rate_lecturer(cool_lecturer, 'Git', 10)
best_student.rate_lecturer(cool_lecturer, 'Git', 10)
best_student.rate_lecturer(second_lecturer, 'Python', 8)
best_student.rate_lecturer(second_lecturer, 'Python', 9)

second_student.rate_lecturer(cool_lecturer, 'Git', 10)
second_student.rate_lecturer(cool_lecturer, 'Git', 9)
second_student.rate_lecturer(second_lecturer, 'Python', 8)
second_student.rate_lecturer(second_lecturer, 'Python', 7)


#Менторы
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(second_student, 'Python', 9)
cool_reviewer.rate_hw(second_student, 'Python', 10)
cool_reviewer.rate_hw(second_student, 'Python', 8)

second_reviewer.rate_hw(best_student, 'Git', 10)
second_reviewer.rate_hw(best_student, 'Git', 10)
second_reviewer.rate_hw(best_student, 'Git', 10)

second_reviewer.rate_hw(second_student, 'Git', 7)
second_reviewer.rate_hw(second_student, 'Git', 8)
second_reviewer.rate_hw(second_student, 'Git', 8)


print(cool_reviewer)
print()
print(second_reviewer)
print()
print(cool_lecturer)
print()
print(second_lecturer)
print()
print(best_student)
print()
print(second_student)
print()
print(best_student > second_student)
print()
print(cool_lecturer < second_lecturer)

mid_st = mid_all_st_grade()
print(mid_st)

mid_lc = mid_all_lc_grade()
print(mid_lc)





