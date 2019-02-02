"""*Remove Dups: Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
* Approach:
* Use lists, add node to list and remove false if node is already in list
* Time Complexity: O(N^2)
* Space Complexity: O(1)
"""
class RemoveDuplicates(object):

    def __init__(self):
        self.head = None

    def removeduplicates(self, head):
        curr = head
        while curr:
            runner = curr
            while runner.next:
                if runner.next.val == curr.val:
                    runner.next = runner.next.next  # use runner for every curr node
                else:
                    runner = runner.next
            curr = curr.next

class Node(object):
    def __init__(self, val = None):
        self.val = val
        self.next = None

list1 = RemoveDuplicates()  # create list 1
list1.head = Node(1)
list1.head.next = Node(4)
list1.head.next.next = Node(4)
list1.head.next.next.next = Node(3)
list1.head.next.next.next.next = Node(1)
list1.removeduplicates(list1.head)
while list1.head:
    print list1.head.val
    list1.head = list1.head.next
