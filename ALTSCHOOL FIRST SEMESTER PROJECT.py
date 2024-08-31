class Person:
    def __init__(self, name, id_number):
    self.name = name
    self.id_number = id_number

    def __str__(self):
    return f"name: {self.name}, ID: {self.id_number}"

class Student(Person):
    def __init__(self, name, id_number, major): super()__init__(name, id_number)
    self.major = major

    def __str__(self):
    return f"{super().__str__()}, Major:{self.major}"

class instructor(Person):
    def __init__(self, name, in_number, department):
    super().__init__(name, id_number)
    self.department = department

    def __str__(self):
    return f"{super().__str__()}, Department: {self.department}"

class Course:
    def __init__(self, course_name, course_id):
    self.course_name = course_name
    self.course_id = course_id
    self.enrolled_students = []

    def add_student(self, student):
    self.enrolled_students.append(student)
    def remove_student(self, student):

    self.enrolled_students.remove(student)

    def __str__(self):
    return f"course Name: {self.course_name}, ID: {self.course_id} Enrolled Students:{[student.name for student in self.enrolled_students]}"

class Enrollment:
    def __init__(self, student, course, grade = None):
    self.student = student
    self.course = course
    self.grade = grade

    def assign_grade(self, grade):
    self.grade = grade

    def __str__(self):
    return f"student:{self.student.name}, Course: {self.course.course_name}, Grade: {self.grade}"
class StudemtManagementSystem:
    def __init__(self):
    self.student = []
    self.instructor = []
    self.courses = []
    self.enrollments = []

    def add_student(self, student):
    self.students.append(student)

    def remove_student(self, student):
            self.students.remove(student)

            def update_student(self, student, new_name,= None, new_id = None):
                if new_name:
                    student.name = new_name
                    if new_id:
                        student.id_number = new_id
                        if new_major:
                            student.major = new_major

                             def add_instructor(self, instructor):
                            self.instructors.append(instructor)

                            def remove_instructor(self, instructor):
                                self.instructors.remove(instructor)
                            def update_instructor(self, instructor, new_name,= None, new_id = None, new_department = None):
                                if new_name:
                                    instructor.name = new_name
                                    if new_id:
                                        instructor.id_number = new_id
                                        if new_department:
                                            instructor.department = new_department

                                            def add_course(self, course):
                                                self.courses.append(course)

                                                def remove_course(self, course):
                                                    self.courses.remove(course)

                                                    def update_course(self, course, new_name = None, new_id = None):
                                                        if new_name:
                                                            course.course_name = new_name
                                                            if new_id:
                                                                course.course_id = new_id

                                                                def enroll_student(self, student, course):
                                                                    course.add_student(student)
                                                                    enrollment=Enrollment(student, course)
                                                                    self.enrollments.append(enrollment) [None]

                                                                    def assign_grade(self, student, course, grade):
                                                                        for enrollment in self.enrollments:
                                                                            if enrollment.student == student
                                                                                and enrollment.course == course:
                                                                                enrollment.assign_grade(grade)

                                                                                def get_students_in_course(self, course):
                                                                                    return course.enrolled_students

                                                                                def get_courses_for_student(self, student):;
                                                                                return[enrollment.course for enrollment in self.enrollments if enrollment.student==student]



