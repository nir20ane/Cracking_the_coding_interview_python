"""* First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
*"""
from TreeNode import TreeNode
class FirstCommonAncestor(object):
    def commonanc(self, root, p, q):
        if root is None:
            return None
        if p is root or q is root:
            return root
        left = self.commonanc(root.left, p, q)
        right = self.commonanc(root.right, p, q)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root

fcc = FirstCommonAncestor()
root = TreeNode(5)
root.addleftchild(1)
root.left.addleftchild(0)
root.addrightchild(8)
root.right.addleftchild(6)
root.right.addrightchild(9)
print(fcc.commonanc(root, root.left, root.right.right).data)
print(fcc.commonanc(root, root.right, root.right.left).data)