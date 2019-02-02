"""* Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
 * Approach:
 * Have fast and slow pointer, moving fast till k and moving both till fast != null
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 *"""

class ReturnKthtoLast(object):
    def __init__(self):
        self.head = None

    def returnKth(self, head, k):
        fast = head
        slow = fast
        i = 0
        while i <= k:
            fast = fast.next  # move fast till k
            i += 1
        while fast:  # move both so difference is k nodes
            fast = fast.next
            slow = slow.next
        return slow.next  # remove Kth to last

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

kth = ReturnKthtoLast()
list1 = ReturnKthtoLast()
list1.head = Node(0)
e2 = Node(1)
e3 = Node(2)
e4 = Node(3)
e5 = Node(4)
e6 = Node(5)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = None

listnew = ReturnKthtoLast()
print(kth.returnKth(list1.head, 3).data)
