
class Car:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname, self.year)


c1 = Car("Toyota", 2000)
c1.display()

# class Employee:
#     id = 7
#     name = "Ramesh"
#     designation = "Cyber Security Expert"
#     Expr = "3 yrs"
#
#     def display(self):
#         print("ID: %d\nName: %s\nDesignation: %s\nExpr: %s" %(self.id, self.name, self.designation, self.Expr))
#
#
# emp = Employee()
# emp.display()
