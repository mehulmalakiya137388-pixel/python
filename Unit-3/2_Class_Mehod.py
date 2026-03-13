class MyClass:

    def message(self):
        print("Hello! This is the first method.")

    def multiply(self, a, b):
        result = a * b
        print("Multiplication of", a, "and", b, "is:", result)


obj = MyClass()
obj.message()
obj.multiply(4,10)
