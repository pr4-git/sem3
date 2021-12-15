# print(p1 < p2)
# print(p2 < p3)
# print(p1 < p3)
#
# # create a list object
# my_list = [4, 7, 0, 1]
#
# # make the object an iterable
# my_iter = iter(my_list)
#
# # print the first element
# print(next(my_iter))
#
# # print 7
# print(next(my_iter))
#
# # print 0
# print(my_iter.__next__())
#
# # print 1
# print(my_iter.__next__())
#
# # raises StopIteration error as there is no other iterable element
# next(my_iter)


# class PowTwo:
#     def __init__(self, max=0):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#
#
# numbers = PowTwo(3)
#
# i = iter(numbers)
#
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

class InfIter:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


a = iter(InfIter())

print(next(a))
print(next(a))
print(next(a))
print(next(a))
