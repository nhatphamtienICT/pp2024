class Student:
    def __init__(self, name, student_id, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
    def show(self):
        print(f"-- Student ID: {self.__id} / Student Name: {self.__name} / DoB: {self.__dob}")

    def input_marks(self, course_id, marks):
        self.__marks[course_id] = marks

    def display_marks(self):
        if not self.__marks:
            print("No marks available for this student.")
        else:
            print("==>Marks:")
            for course_id, marks in self.__marks.items():
                print(f"--Course ID: {course_id} / Marks: {marks}")
    
class Course:
    def __init__(self, name, course_id):
        self.__id = course_id
        self.__name = name
        

    def show(self):
        print(f"--Course ID: {self.__id} / Course Name: {self.__name}")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Error!! Enter a valid positive number.")
        except ValueError:
            print("Invalid. Enter a valid number.")
def number_of_students():
    return get_positive_integer("Enter the number of students: ")

def number_of_courses():
    return get_positive_integer("Enter the number of courses: ")


def student_info(num_students):
    student_info_list = []
    print("Student list:")
    for i in range(num_students):
        print(f"- Student {i + 1}")
        student_id = input("Enter Student id: ")
        name = input("Enter Student's name: ")
        dob = input("Enter Student's Dob: ")
        student = Student(name, student_id, dob)
        student_info_list.append(student)
    return student_info_list


def course_info(num_courses):
    course_info_list = []
    print("Course list:")
    for i in range(num_courses):
        print(f"- Course number {i + 1}")
        course_id = input("Enter Course id: ")
        name = input("Enter Course's name: ")
        course = Course(name, course_id)
        course_info_list.append(course)
    return course_info_list

def input_student_marks(students, courses):
    for student in students:
        for course in courses:
            prompt = f"==>Enter marks for Student ID: {student._Student__id} ({student._Student__name}) in Course ID: {course._Course__id} ({course._Course__name}): "
            marks = get_positive_integer(prompt)
            student.input_marks(course_id=course._Course__id, marks=marks)


def display_student_info_and_marks(students):
    for student in students:
        student.show()
        student.display_marks()
        print("\n") 

def display_student_marks(students):
    for student in students:
        student.display_marks()

def student_list(student_info_list):
    if not student_info_list:
        print("No student info")
    else:
        for i, student in enumerate(student_info_list):
            print(f"==>Student {i + 1}:")
            student.show()


def course_list(course_info_list):
    if not course_info_list:
        print("No course info")
    else:
        for i, course in enumerate(course_info_list):
            print(f"Course {i + 1}:")
            course.show()


def main():
    num_students = number_of_students()
    students = student_info(num_students)

    num_courses = number_of_courses()
    courses = course_info(num_courses)

    student_list(students)
    print("\n")
    course_list(courses)
    print("\n")

    input_student_marks(students,courses)
    #display_student_marks(students) 
    print("\n")
    display_student_info_and_marks(students)




    

if __name__ == "__main__":
    main()