# multi-level inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")


class Dog(Animal):
    def bark(self):
        print("Dog Barking")


class DogChild(Dog):
    def eat(self):
        print("Eating Food")


d = DogChild()
d.speak()
d.bark()
d.eat()


# multiple inheritance

class Calculation1:
    def Summation(self, a, b):
        return a + b


class Calculation2:
    def Multiplication(self, a, b):
        return a * b


class Calculation3:
    def Division(self, a, b):
        return a / b


class Derived(Calculation1, Calculation2, Calculation3):
    def Subtraction(self, a, b):
        return a - b


d = Derived()
print(d.Summation(5, 10))
print(d.Division(5, 10))
print(d.Multiplication(5, 10))
print(d.Subtraction(5, 10))

# check if it is a subclass
print(issubclass(Derived, Calculation1))
print(issubclass(Calculation3, Calculation2))