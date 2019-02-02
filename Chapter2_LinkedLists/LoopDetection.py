"""*Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input:
Output:
SOLUTION
A -> B -> C -> D -> E -> C [the same C as earlier]
C
** Approach: Use fast and and slow runners, have while for slow != fast
* Time Complexity: O(N)
* Space Complexity: O(1)
*"""
class LoopDetection(object):
    def __init__(self):
        self.head = None

    def loopdetect(self, head):
        if head is None or head.next is None:
            return False
        fast = head.next  # this is important
        slow = head
        while slow != fast:
            if fast is None or fast.next is None:
                return False  # return False when fast is None
            slow = slow.next
            fast = fast.next.next
        return True  # return True if there is a loop

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


list1 = LoopDetection()
list1.head = Node('A')
list1.head.next = Node('B')
list1.head.next.next = Node('C')
list1.head.next.next.next = Node('D')
list1.head.next.next.next.next = Node('E')
list1.head.next.next.next.next.next = list1.head.next.next
print(list1.loopdetect(list1.head))
