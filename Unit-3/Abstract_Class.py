class Animal:

    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def make_sound(self):
        return "Bark"


class Cat(Animal):
    def make_sound(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.make_sound())
print(cat.make_sound())
