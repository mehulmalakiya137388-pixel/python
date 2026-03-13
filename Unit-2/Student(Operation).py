students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    students[roll] = {"Name": name, "Age": age}
    print("Student added successfully")

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print("Student Found")
        print("Name:", students[roll]["Name"])
        print("Age:", students[roll]["Age"])
    else:
        print("Student not found")

def list_students():
    if not students:
        print("No students available")
    else:
        print("\nStudent List")
        for roll, data in students.items():
            print("Roll:", roll, "Name:", data["Name"], "Age:", data["Age"])

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter new Name: ")
        age = input("Enter new Age: ")
        students[roll] = {"Name": name, "Age": age}
        print("Student updated successfully")
    else:
        print("Student not found")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully")
    else:
        print("Student not found")

while True:
    print("\n--- Student Management Menu ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. List All Students")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        list_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting program")
        break
    else:
        print("Invalid choice")
