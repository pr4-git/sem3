# def print_msg(msg):
#     # this is the outer enclosing function
#     def printer():
#         # this is the nested function
#         print(msg)
#     printer()
#
#
# print_msg("Hello world")
#
#
# def print_msg(msg):
#     def printer():
#         print(msg)
#
#     return printer
#
#
# another = print_msg("Hello")
# another()


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


times3 = make_multiplier_of(3)

times5 = make_multiplier_of(5)

print(times3(9))
print(times5(3))
print(times5(times3(2)))
