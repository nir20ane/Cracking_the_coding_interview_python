"""* 4.2 Minimal Tree:
 * Given a sorted (increasing order) array with unique integer elements,
 * write an algorithm to create a binary search tree with minimal height.
* """
from TreeNode import TreeNode
class MinimalTree(object):
    def createBSTT(self, sortedlist):
        return self.createBST(sortedlist, 0, len(sortedlist)-1)


    def createBST(self, sortedlist, start, end):
        if start > end:
            return None
        mid = (start+end)/2
        node = TreeNode(sortedlist[mid])
        node.left = self.createBST(sortedlist, start, mid-1)
        node.right = self.createBST(sortedlist, mid+1, end)
        return node

    def printNode(self, node):
        if node:
            self.printNode(node.left)
            print(node.data),
            self.printNode(node.right)

mt = MinimalTree()
node = mt.createBSTT([1, 2, 3, 4, 5, 6, 7])
mt.printNode(node)
