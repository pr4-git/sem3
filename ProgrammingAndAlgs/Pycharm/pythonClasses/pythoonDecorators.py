# def first(msg):
#     print(msg)
#
#
# first("Good Morning")
# second = first
# second("Good Morning")
#
#
# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# def operator(func, x):
#     result = func(x)
#     return result
#
#
# x = operator(inc, 10)
# y = operator(dec, 10)
#
# print(x)
# print(y)
#
#
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
#
# def simple():
#     print("I am simple")
#
#
# simple()
# # let's decorate this ordinary function
# pretty = make_pretty(simple)
# pretty()
#
#
# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Woah bro! I can't divide that!")
#             return
#         return func(a, b)
#     return inner
#
#
# # using @decoratorfunction in front of the to-be-decorated function
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
#
# divide(2, 5)
# divide(2, 0)


def star(func):
    def inner(*args, **kwargs):
        print("*"*30)
        func(*args, **kwargs)
        print("*"*30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%"*30)
        func(*args, **kwargs)
        print("%"*30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Good Morning")
