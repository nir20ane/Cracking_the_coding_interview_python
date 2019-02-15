""" *Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
* """
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = float('Inf')

    def push(self, x):
        if x <= self.min:
            self.stack.append(self.min)  # if x is <=min, push min first and then x, so as to keep track of min for each pop() operation
            self.min = x
        self.stack.append(x)

    def pop(self):
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()  # pop twice is top element is min

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(-2)
obj.pop()
print(obj.getMin())
print(obj.top())
obj.pop()
print(obj.getMin())
print(obj.top())
