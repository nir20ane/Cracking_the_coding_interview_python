"""*
 * Check Balanced:
 * Implement a function to check if a binary tree is balanced.
 * For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * """
from TreeNode import TreeNode
class CheckBalanced(object):
    def isbalanced(self, root):
        if self.isbalancedhelper(root) == -1:
            return False
        else:
            return True

    def isbalancedhelper(self, node):

        if node is None:
            return 0

        leftheight = self.isbalancedhelper(node.left)
        if leftheight == -1:
            return -1

        rightheight = self.isbalancedhelper(node.right)
        if rightheight == -1:
            return -1

        if abs(leftheight - rightheight) > 1:
            return -1

        return 1+max(leftheight, rightheight)

cb = CheckBalanced()
root = TreeNode(0)
root.addleftchild(1)
root.left.addleftchild(3)
root.left.left.addleftchild(4)
root.addrightchild(2)
print(cb.isbalanced(root))

root1 = TreeNode(0)
root1.addleftchild(1)
root1.addrightchild(4)
root1.left.addleftchild(3)
root1.left.addrightchild(5)
root1.left.left.addleftchild(10)
root1.right.addleftchild(3)
root1.right.addrightchild(3)
print(cb.isbalanced(root1))
