"""*Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
** Approach: get the length of lists, adjust length to be equal, compare to find intersection
* Time O(n); Space O(1)
*"""
class IntersectionofLinkedList(object):
    def __init__(self):
        self.head = None

    def intersectlist(self, head1, head2):
        len1 = self.length(head1)
        len2 = self.length(head2)

        if len1 > len2:
            head1 = head1.next  # adjust length of lists
            len1 -= 1

        if len2 > len1:
            head2 = head2.next
            len2 -= 1

        while head1 != head2:
            head1 = head1.next  # when they become equal return node
            head2 = head2.next
        return head1

    def length(self, head):
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count

class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None

list1 = IntersectionofLinkedList()  # create list 1
list1.head = Node(4)
list1.head.next = Node(1)
list1.head.next.next = Node(8)
list1.head.next.next.next = Node(4)
list1.head.next.next.next.next = Node(5)

list2 = IntersectionofLinkedList()  # create list 2
list2.head = Node(5)
list2.head.next = Node(1)
list2.head.next.next = Node(0)
list2.head.next.next.next = list1.head.next.next
print(list1.intersectlist(list1.head, list2.head).data)
