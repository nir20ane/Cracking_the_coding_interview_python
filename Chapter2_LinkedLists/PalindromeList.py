"""* Palindrome: Implement a function to check if a linked list is a palindrome.
** Approach: get middle of list, and then reverse one half, then compare the nodes
* Time - O(n); Space - O(1)
*"""
class PalindromeList(object):
    def __init__(self):
        self.head = None

    def palindrome(self, head):
        fast = head
        slow = head
        l1 = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if fast:
            slow = slow.next  # find middle

        l2 = self.reverse(slow)  # reverse second half of list

        while l2:
            if l1.data != l2.data:  # if not equal return false
                return False
            l1 = l1.next
            l2 = l2.next
        return True  # return true otherwise

    def reverse(self, head):  # reverse method to reverse list
        prev = None
        curr = head
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

pll = PalindromeList()
pll.head = Node(0)
n2 = Node(1)
n3 = Node(2)
n4 = Node(1)
n5 = Node(0)
pll.head.next = n2
pll.head.next.next = n3
pll.head.next.next.next = n4
pll.head.next.next.next.next = n5
pll.head.next.next.next.next.next = None
print(pll.palindrome(pll.head))
