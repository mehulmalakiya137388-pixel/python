class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("Access granted. You are eligible.")
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
finally:
    print("Program execution completed.")
