"""* 4.5 Validate BST:
 * Implement a function to check if a binary tree is a binary search tree.
 * """
z

class ValidateBST(object):
    def validatebst(self, root):
        return self.validatebsthelper(root, -2**31, 2**31)

    def validatebsthelper(self, node, min, max):
        if node is None:
            return True
        if node.data <= min or node.data > max:
            return False
        return self.validatebsthelper(node.left, min, node.data) and self.validatebsthelper(node.right, node.data, max)

vbst = ValidateBST()
root = TreeNode(3)
root.addleftchild(1)
root.left.addleftchild(0)
root.left.left.addleftchild(-1)
root.addrightchild(4)
print(vbst.validatebst(root))

root1 = TreeNode(20)
root1.addleftchild(10)
root1.addrightchild(40)
root1.left.addleftchild(9)
root1.left.addrightchild(11)
root1.left.left.addleftchild(8)
root1.right.addleftchild(30)
root1.right.addrightchild(100)
print(vbst.validatebst(root1))
