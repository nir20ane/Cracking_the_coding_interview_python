"""Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
"""
class SortStacks(object):
    def __init__(self):
        self.r = []

    def sortstack(self, s):
        while s:
            tmp = s.pop()
            while self.r and tmp < self.r[-1]: # check for tmp < value
                s.append(self.r.pop())  # pop all greater than tmp
            self.r.append(tmp)  # push tmp

        s = self.r  # copy new stack to old
        return s

ss = SortStacks()
print(ss.sortstack([2, 6, 5, 4, 1, 3, 8, 7]))
