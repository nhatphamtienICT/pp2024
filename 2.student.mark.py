class Student:
    def __init__ (self,name,id,dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__Mark = {}
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_mark(self):
        return self.__Mark
    def show(self):
        print(f"Student ID : {self.__id} / Student Name: {self.__name} / DoB: {self.__dob}")
class Course(Student):
    def __init__(self,name,id,dob):
        super().__init__(name,id,dob)
    def show(self):
        print(f"Course ID : {self.get_id()} / Course Name : {self.get_name()}")
    
    
