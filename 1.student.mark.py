# 1.student.mark.py
# Student mark management system (NO classes/objects)
# Use only: lists, dicts, tuples

student_list = []
course_list = []

def input_num_student():
    return int(input("Enter number of students: "))

def input_num_course():
    return int(input("Enter number of courses: "))

def initialized_student_list(n):
    global student_list
    student_list = []
    for i in range(n):
        print(f"\nStudent {i+1}/{n}")
        sid = input("Enter student id: ").strip()
        name = input("Enter student name: ").strip()
        dob = input("Enter student dob: ").strip()

        # store as dict (no objects)
        student = {"id": sid, "name": name, "dob": dob}
        student_list.append(student)

def initialized_course_list(n):
    global course_list
    course_list = []
    for i in range(n):
        print(f"\nCourse {i+1}/{n}")
        cid = input("Enter course id: ").strip()
        name = input("Enter course name: ").strip()

        # each course keeps its own marks dictionary
        course = {"id": cid, "name": name, "marks": {}}
        course_list.append(course)

def enter_score(course):
    # course is a dict: {"id","name","marks"}
    for student in student_list:
        s = input(f"Enter student {student['name']} score: ").strip()
        score = float(s)
        course["marks"][student["id"]] = score  # store by student id

def enter_all_score():
    for course in course_list:
        print(f"\nEnter all the student scores in {course['name']}")
        enter_score(course)

def list_students():
    if len(student_list) == 0:
        print("No students.")
        return

    print("\nSTUDENTS")
    print("-" * 50)
    print(f"{'ID':<12}{'Name':<25}{'DoB':<12}")
    print("-" * 50)
    for st in student_list:
        print(f"{st['id']:<12}{st['name']:<25}{st['dob']:<12}")

def list_courses():
    if len(course_list) == 0:
        print("No courses.")
        return

    print("\nCOURSES")
    print("-" * 40)
    print(f"{'ID':<12}{'Name'}")
    print("-" * 40)
    for c in course_list:
        print(f"{c['id']:<12}{c['name']}")

def find_course_by_id(cid):
    for c in course_list:
        if c["id"] == cid:
            return c
    return None

def find_student_by_id(sid):
    for st in student_list:
        if st["id"] == sid:
            return st
    return None

def show_student_marks_for_course():
    if len(course_list) == 0:
        print("No courses.")
        return
    if len(student_list) == 0:
        print("No students.")
        return

    list_courses()
    cid = input("\nEnter course id to view marks: ").strip()
    course = find_course_by_id(cid)
    if course is None:
        print("Course not found.")
        return

    print(f"\nMARKS for {course['id']} - {course['name']}")
    print("-" * 60)
    print(f"{'Student ID':<12}{'Name':<25}{'Mark':>8}")
    print("-" * 60)

    # print marks in student order
    for st in student_list:
        sid = st["id"]
        name = st["name"]
        if sid in course["marks"]:
            mark = course["marks"][sid]
            mark_str = f"{mark:.2f}"
        else:
            mark_str = "N/A"
        print(f"{sid:<12}{name:<25}{mark_str:>8}")

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

        choice = input("Choose: ").strip()

        if choice == "1":
            n = input_num_student()
            initialized_student_list(n)
        elif choice == "2":
            n = input_num_course()
            initialized_course_list(n)
        elif choice == "3":
            enter_all_score()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_student_marks_for_course()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
