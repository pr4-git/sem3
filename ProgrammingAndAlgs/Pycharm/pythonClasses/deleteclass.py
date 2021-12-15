# # # This does not run
#
# class Employee:
#     id = 10
#     name = "Hari"
#
#     def display(self):
#         print("ID: %d \nName: %s" % (self.id, self.name))
#
#
# emp = Employee()
#
# del emp.id
#
# del emp
#
# emp.display()


# class Employee:
#     def __init__(self, name, id):
#         self.id = id
#         self.name = name
#
#     def display(self):
#         print("ID: %d \nName: %s" % (self.id, self.name))
#
#
# emp1 = Employee("Ram", 101)
# emp2 = Employee("Shyam", 102)
#
# emp1.display()
# emp2.display()
#
#
# class Student:
#     count = 0
#
#     def __init__(self):
#         Student.count = Student.count + 1
#
#
# s1 = Student()
# s2 = Student()
# s3 = Student()
# s4 = Student()
#
# print("The number of students:", Student.count)
#
#
# class Student:
#
#     def __init__(self):
#         print("This is non parametrized constructor.")
#
#     def show(self, name):
#         print("Hello", name)
#
#
# student = Student()
# student.show("Govinda")
#
#
# class Student:
#     def __init__(self):
#         print("The first constructor.")
#
#     def __init__(self):
#         print("The second constructor.")
#
#
# st = Student()



