class Animal:
    def speak(self):
        print("Speaking")


class Dog(Animal):
    def speak(self):
        print("Barking")


d = Dog()
d.speak()


class Bank:
    def getroi(self):
        return 10


class SBI(Bank):
    def getroi(self):
        return 7


class GlobalIME(Bank):
    def getroi(self):
        return 8


B1 = Bank()
B2 = SBI()
B3 = GlobalIME()
print("Bank rate of interest:", B1.getroi())
print("SBI rate of interest:", B2.getroi())
print("GlobalIME rate of interest:", B3.getroi())