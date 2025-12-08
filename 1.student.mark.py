

student_list = []
course_list = []


def input_num_student():
    n = int(input("Enter number of student: "))
    return n

def input_num_course():
    n = int(input("Enter number of course: "))
    return n


class Entity:
    def __init__(self,id, name):
        self.id = id
        self.name = name

class Student(Entity):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob
        


class Course(Entity):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.marks = []
    


def enter_score(course):
    for student in student_list:
        score = float(input(f"Enter student {student.name} score"))
        course.marks.append((student,score))

def enter_all_score():
     
    for course in course_list:
        print(f"Enter all the student score in {course.name}")
        enter_score(course)



def initialized_student_list(n):
    for i in range(n):
        name = input("Enter student name ")
        id = input("Enter student id ")
        dob = input("Enter student dob ")

        student = Student(id, name, dob)
        student_list.append(student)



def initialized_course_list(n):
    for i in range(n):
        name = input("Enter course name ")
        id = input("Enter course id ")
         

        course = Course(id,name)
        course_list.append(course)



  

def main():
    n = input_num_student()
    initialized_student_list(n)
    c = input_num_course()
    initialized_course_list(c)
    enter_all_score()




 
 