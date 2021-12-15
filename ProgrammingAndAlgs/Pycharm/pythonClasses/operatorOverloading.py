# # This doesn't work
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(1, 2)
# p2 = Point(2, 3)
#
# print(p1 + p2)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "({}, {})".format(self.x, self.y)
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)
#
#
# p1 = Point(1, 2)
# p2 = Point(2, 3)
#
# print(p1 + p2)

#
# class Point:
#     def __init__(self, x = 0, y =0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)
#
#     def __lt__(self, other):
#         self_mag = (self.x ** 2) + (self.y ** 2)
#         other_mag = (other.x ** 2) + (other.y ** 2)
#         return self_mag < other_mag
#
#
# p1 = Point(1, 1)
# p2 = Point(-2, -3)
# p3 = Point(1, -1)
#
#

