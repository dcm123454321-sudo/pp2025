
print("RUNNING VERSION 4")



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
        self.marks = []   #The tupples for student + score are all stored here
    


def enter_score(course):
    for student in student_list:
        score = float(input(f"Enter student {student.name} score"))
        course.marks.append((student,score))




#^This is STORED INSIDE EACH INDIVIDUAL COURSE OBJECT ARRAY, for example Math1 will have student1-2-3 name and score1-2-3 paired together as a tuple


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

def show_mark(course):
    print(f"Marks for course: {course.name}")
    for student, score in course.marks:
        print(f"{student.id} - {student.name}: {score}")




def show_all_marks():
    for course in course_list:
        show_mark(course)







  

def main():

    while True:
        print("\n===== MENU =====")
        print("1. Input number of students + student info")
        print("2. Input number of courses + course info")
        print("3. Enter all marks for all courses")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a given course")
        print("0. Exit")

        choice = input("Enter: ").strip()

        if choice == "1":
            n = input_num_student()
            initialized_student_list(n)
        elif choice == "2":
            c = input_num_course()
            initialized_course_list(c)
        elif choice == "3":
            enter_all_score()




if __name__ == "__main__":
    main()





 
 