class student:

    
    def AddStudent(self):
        self.roll=int(input("Enter your roll no=>"))
        self.name=input("Enter your Name no=>")
        self.age=int(input("Enter your Age=>"))
        self.gender=input("Enter your Name no=>")

    def DisplayStudent(self):
        print("Roll no",self.roll)
        print("Name",self.name)
        print("Age",self.age)
        print("gender",self.gender)

s1=student()
s1.AddStudent()
s1.DisplayStudent()
