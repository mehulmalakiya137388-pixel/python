class Outer:
    def __init__(self):
        self.msg = "Hello from Outer class!"

    class Inner:
        def display(self):
            print("Hello from Inner class!")

outer_obj = Outer()

inner_obj = outer_obj.Inner()

inner_obj.display()
print(outer_obj.msg)
