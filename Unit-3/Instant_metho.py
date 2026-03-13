class Student:
    school_name = "ABC School"   

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_student(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("School:", Student.school_name)

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school


s1 = Student("Rahul", 85)
s2 = Student("Anita", 92)

s1.display_student()
print()

Student.change_school("abcd")

s2.display_student()
