"""* Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific substack.
* """
class StackofPlates(object):
    def __init__(self):
        self.capacity = 3
        self.stacks = []

    def push(self, item):
        if len(self.stacks) == 0 or len(self.stacks[-1]) >= self.capacity:  # if linked list is empty or last stack is empty
            stack = []  # create new stack and push item
            stack.append(item)
            self.stacks.append(stack)
        else:
            stack = self.stacks[-1]
            stack.append(item)  # push into last stack in linked list

    def pop(self):
        if len(self.stacks) == 0:
            print("Stacks is Empty")
            pass
        else:
            stack = self.stacks[-1]
            item = stack.pop()
            if len(stack) == 0:
                del self.stacks[-1]  # remove last stack from ll if last stack is empty

    def popAt(self, index):
        if len(self.stacks) == 0:
            print("Stacks is Empty")  # validate stacks
            pass
        elif index < 0 or index>len(self.stacks):  # validate index value
            print("Invalid Index")
            pass
        else:
            item = self.stacks[index].pop()
            for i in range(index, len(self.stacks)-1):  # keep pushing elements if there are empty spaces in stack
                curr = self.stacks[i]
                next = self.stacks[i+1]
                curr.append(next[0])
                del next[0]
            if len(self.stacks[-1]) == 0:
                del self.stacks[-1]
            return item

    def printstacks(self):
        for stack in self.stacks:
            for item in stack:
                print("Item : "+str(item))
            print("top")


stck = StackofPlates()
stck.push(1)
stck.push(2)
stck.push(3)
stck.push(4)
stck.push(5)
stck.push(6)
stck.push(7)
stck.push(8)
stck.push(9)
stck.popAt(1)
stck.popAt(0)
stck.printstacks()
