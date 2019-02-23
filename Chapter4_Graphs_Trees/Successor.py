"""* Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
Hint:
in-order traversal, left, node, right
if there is no right, then we have to find the parent,
if there is right, we have to find the leftmost child of node
* """
from TreeNode import TreeNode

class Successor(object):
    def findsuccessor(self, node):
        if node.right is None:
            return self.properparent(node)
        else:
            return self.findleftmost(node.right)

    def findleftmost(self, node):
        if node is None:
            return None
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def properparent(self, node):
        if node is None:
            return None
        parent = node.parent
        child = node
        while parent is not None and parent.left is not child:
            child = parent
            parent = child.parent
        return parent

root = TreeNode(5)
root.addleftchild(1)
root.left.addleftchild(0)
root.addrightchild(8)
root.right.addleftchild(6)
root.right.addrightchild(9)

suc = Successor()
print(suc.findsuccessor(root).data)
print(suc.findsuccessor(root.left).data)
print(suc.findsuccessor(root.right.right))
