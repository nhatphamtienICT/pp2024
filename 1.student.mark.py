# Function 
def numberofstudents():
    while(True):
        try:
            num1 = int(input("The number of student:" ))
            if num1 > 0:
                return num1
            else:
                print("Error!! Enter a valid number. ")
        except ValueError:
            print("Invalid. Enter a valid number. ")        

def numberofcourses():
    while(True):
        try:
            num2 = int(input("The number of courses:" ))
            if num2 > 0:
                return num2
            else:
                print("Error!! Enter a valid number. ")
        except ValueError:
            print("Invalid. Enter a valid number. ")     

def studentinfo():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    #if(name[0].islower()):
    name = name.capitalize()
    dob = input("Enter date of birth : ")
    return {"id": student_id, "name": name, "dob": dob}

def coursesinfo():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}

def checkID(course_id,courses):
    return course_id in courses

def input_student_marks(students, course_id):
    marks = {}
    for student in students:
        mark = float(input(f"Enter marks for {student['name']} (Student ID: {student['id']}) in course {course_id}: "))
        marks[student['id']] = mark
    return marks


# List
def list_students(students):
    print("\nStudents information:")
    for index, student in enumerate(students):
        print(f"====>>>> Student {index + 1}\n- ID: {student['id']},\n- Name: {student['name']},\n- DoB: {student['dob']}\n")
        
def list_courses(courses):
    print("Courses information:")
    for course in courses:
        print(f"- Course ID: {course['id']},\n- Name: {course['name']}\n")

def show_student_marks(students, marks, course_id):
    print(f"\nStudent Marks for Course {course_id}:")
    for student in students:
        student_id = student['id']
        if student_id in marks:
            print(f"Student ID: {student_id}, Name: {student['name']}, Marks: {marks[student_id]}")
        else:
            print(f"Student ID: {student_id}, Name: {student['name']}, Marks: N/A")



def main():
    students = []
    courses = []

    
    students_num = numberofstudents()

    for _ in range(students_num):
        student_info = studentinfo()
        students.append(student_info)

    courses_num = numberofcourses()
    for _ in range(courses_num):
        course_info = coursesinfo()
        courses.append(course_info)   
    

    
    list_students(students)
    list_courses(courses)
    print("\nList of Courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Name: {course['name']}")
    while(True):
        selected_course_id = input("Enter a course ID: ")
        if checkID(selected_course_id,courses):
            marks_for_selected_course = input_student_marks(students, selected_course_id)
            show_student_marks(students, marks_for_selected_course, selected_course_id)
            break
        else:
            print("Invalid! Please try again")

        


if __name__ == "__main__":
    main()


