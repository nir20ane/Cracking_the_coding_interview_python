"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""
class QueueviaStacks(object):
    def __init__(self):
        self.newest = []
        self.oldest = []

    def enqueue(self, item):
        self.newest.append(item)  # push item into new stack

    def dequeue(self):
        self.shiftstacks()
        print self.oldest
        return self.oldest.pop()  # get top element, first shift and then pop from oldest

    def size(self):
        return len(self.oldest)+len(self.newest)

    def peek(self):
        self.shiftstacks()
        return self.oldest[-1]  # get top element, first shift and then peek from oldest

    def shiftstacks(self):
        if len(self.oldest) == 0:
            while len(self.newest) != 0:
                self.oldest.append(self.newest.pop())  # shift from new to old

questck = QueueviaStacks()
questck.enqueue(1)
questck.enqueue(2)
questck.enqueue(3)
questck.enqueue(4)
questck.enqueue(5)
questck.enqueue(6)
questck.enqueue(7)
questck.enqueue(8)
questck.enqueue(9)
print(questck.dequeue())
print(questck.dequeue())
print(questck.dequeue())
print(questck.size())
print(questck.peek())
print(questck.dequeue())
