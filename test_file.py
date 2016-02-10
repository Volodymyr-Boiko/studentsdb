#! usr/bin/python


# def exponent(x, n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return x
#     if n % 2:
#         return x * exponent(x * x, (n - 1) / 2)
#     return exponent(x * x, n / 2)


# class Rectangle(object):
#
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#
# def CheckCollision(recA, recB):
#     if (recA.x + recA.width) < recB.x:
#         return True
#     elif (recA.x + recA.width) > recB.x > recA.x:
#         recb_lower_x = recB.x - recB.height
#         recb_lower_y = recB.y
#         if recb_lower_x > (recA.x + recA.width) and recb_lower_y > (recA.y + recA.height):
#             return True
#     return False
#
#
#
#
# ra = Rectangle(1, 1, 6, 4)
# rb = Rectangle(8, 1, 1, 6)
#
# print CheckCollision(ra, rb)


# class Iter(object):
#
#     def __init__(self, start, finish):
#         self.start = start
#         self.finish = finish
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.start > self.finish:
#             raise StopIteration
#         self.start += 2
#         return self.start - 2
#
#
# i = Iter(1, 10)
# for item in i:
#     print item

# from time import time
#
#
# def sort_lst(lst):
#     n = len(lst)
#     while n > 0:
#         for item in range(n - 1):
#             if lst[item] > lst[item + 1]:
#                 lst[item], lst[item + 1] = lst[item + 1], lst[item]
#         n -= 1
#     return lst
#
#
# start = time()
# sort_lst(range(1000, 0, -1))
# end = time()
#
# start1 = time()
# sorted(range(1000, 0, -1))
# end1 = time()
#
#
# print (end - start) * 1000, (end1 - start1) * 1000


class Singleton(object):

    obj = None

    def __new__(cls, *dt):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *dt)
        return cls.obj


