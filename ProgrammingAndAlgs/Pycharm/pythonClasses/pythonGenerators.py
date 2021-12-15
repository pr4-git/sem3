# # simple generator function
# def my_gen():
#     n = 1
#     print("This is printed first")
#     yield n
#
#     n += 1
#     print("This is printed second")
#     yield n
#
#     n += 1
#     print("this is printed last")
#     yield n
#
#
# a = my_gen()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length-1, -1, -1):
#         yield my_str[i]
#
#
# # for loop to reverse the string
# for char in rev_str("hello"):
#     print(char)
#
# pow2 = [2 ** x for x in range(10)]
# print(pow2)
#
# pow2 = [2 ** x for x in range(10) if x > 5]
# print(pow2)
#
# pow2 = [2 ** x for x in range(10) if x % 2 == 1]
# print(pow2)
#
# a = [x+y for x in ['Python ', 'C '] for y in ['Language', 'Programming']]
# print(a)
#
# # generators are basically lazy lists
#
# # initialize the list
# my_list = [1, 3, 6, 10]
#
# # squaring each term using list comprehension
# list_ = [x ** 2 for x in my_list]
#
# # same thing in generator expression
# generator = (x ** 2 for x in my_list)
#
# print(list_)
# print(generator)
# # generator doesn't print || have to write next
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# # it works now
#

# def fibonacci_number(nums):
#     x, y = 0, 1
#     for _ in range(nums):
#         x, y = y, x + y
#         yield x
#
#
# def square(nums):
#     for num in nums:
#         yield num**2
#
#
# print(sum(square(fibonacci_number(10))))
