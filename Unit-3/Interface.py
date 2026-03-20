class Animal:
    
    def sound(self):
        raise NotImplementedError("Subclass must implement this method")
    
    def eat(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    
    def sound(self):
        print("Dog barks")
    
    def eat(self):
        print("Dog eats food")

d = Dog()
d.sound()
d.eat()
