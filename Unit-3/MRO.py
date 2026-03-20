class Student:
    def student_info(self):
        print("This is Student class")

class Course:
    def course_info(self):
        print("This is Course class")

class Result(Student, Course):
    def result_info(self):
        print("This is Result class")

obj = Result()

obj.student_info()
obj.course_info()
obj.result_info()

print("\nMethod Resolution Order (MRO):")
for cls in Result.__mro__:
    print(cls)
