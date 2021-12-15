from abc import ABC, abstractmethod
# abstract base class


class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30mph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25mph")


class Duster(Car):
    def mileage(self):
        print("The mileage is 35mph")


class Renault(Car):
    def mileage(self):
        print("The mileage is 20mph")


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()
