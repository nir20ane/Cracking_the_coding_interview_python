"""*Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
*"""
class SumLists(object):
    def __init__(self):
        self.head = None

    def sumlists(self, head1, head2):
        dummy = Node(0)
        curr = dummy
        p = head1
        q = head2
        carry = 0
        sum = 0
        while p or q:
            if p:
                x = p.data
            else:
                x = 0
            if q:
                y = q.data
            else:
                y =0
            sum = carry + x + y  # calculate sum
            carry = sum//10
            curr.next = Node(sum%10)  # create node for sum
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            curr.next = Node(carry) # create node for carry
        return dummy.next

class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None

add = SumLists()
list1 = SumLists()
list1.head = Node(7)
e2 = Node(1)
e3 = Node(6)
list1.head.next = e2
e2.next = e3
e3.next = None
list2 = SumLists()
list2.head = Node(5)
e2 = Node(9)
e3 = Node(2)
list2.head.next = e2
e2.next = e3
e3.next = None
noden = add.sumlists(list1.head, list2.head)
while noden:
    print(noden.data)
    noden = noden.next
