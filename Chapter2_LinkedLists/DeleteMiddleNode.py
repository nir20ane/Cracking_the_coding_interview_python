"""*Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a ->b->d->e->f
** Approach: if given node is null or last node return false, else delete node and return true
* Time Complexity: O(1)
* Space Complexity: O(1)
*"""
class DeleteMiddleNode(object):
    def __init__(self):
        self.head = None

    def deletemiddle(self, node):
        if node is None or node.next is None:
            return False  # return false when node is at end or None
        node.data = node.next.data
        node.next = node.next.next  # delete node and true
        return True

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

dml = DeleteMiddleNode()
dml.head = Node(0)
n2 = Node(1)
n3 = Node(2)
n4 = Node(1)
n5 = Node(0)
dml.head.next = n2
dml.head.next.next = n3
dml.head.next.next.next = n4
dml.head.next.next.next.next = n5
dml.head.next.next.next.next.next = None
print(dml.deletemiddle(dml.head))
