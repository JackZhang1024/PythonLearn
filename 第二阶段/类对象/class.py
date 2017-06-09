# -*- coding:utf-8 -*-

# s = "abc"
# it = iter(s)
# for char in s:
#     print(next(it))

# class Reverser:
#     """Iterator for looping over a sequence backwards"""
#     def __int__(self,data):
#         self.data = data
#         self.index = len(data)
#      def __iter__(self):
#          return self
#      def __next__(self):
#          if self.index == 0:
#             raise  StopIteration
#          self.index -= 1
#          return self.data[self.index]
#
# rev = Reverser("spam")
# for char in rev:
#     print(char)

# def reverse(data):
#     for index in range(len(data)-1,-1,-1):
#         yield data[index]
# for char in reverse("golf"):
#     print(char)


def my_function():
    """ Do nothing

    No,really, it does't make any sense
    """
    pass

print(my_function.__doc__)