"""*Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
* Approach:
* have four pointers: beforehead, before, after, afterhead
* Time Complexity: O(N)
* Space Complexity: O(1)
"""
class PartitionList(object):
    def __init__(self):
        self.head = None

    def makepartition(self, head, x):
        beforehead = Node(0)
        before = beforehead
        afterhead = Node(0)
        after = afterhead
        while head:
            if head.data < x:  # if Node lesser than x, move to before list
                before.next = head
                before = before.next
            else:
                after.next = head  # if Node greater than x, move to after list
                after = after.next
            head = head.next
        after.next = None
        before.next = afterhead  # join two lists
        return beforehead.next

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

part = PartitionList()
list1 = PartitionList()
list1.head = Node(1)
e2 = Node(6)
e3 = Node(4)
e4 = Node(2)
e5 = Node(5)
e6 = Node(0)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = None
partnew = part.makepartition(list1.head, 3)
while partnew is not None:
    print(partnew.data)
    partnew = partnew.next
