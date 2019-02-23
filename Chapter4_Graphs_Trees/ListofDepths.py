"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""
from TreeNode import TreeNode
class ListofDepths(object):
    def createlists(self, root):
        lists = []

        # initially pass level as 0 to helper
        self.createlistshelper(root, lists, 0)

        # return lists
        return lists

    def createlistshelper(self, node, lists, level):
        # if node is none, return none
        if node is None:
            return None

        # if len is equal to  level, time to create new lis
        if len(lists) == level:
            lists.append([])

        # get current list from lists
        list = lists[level]

        # add current data
        list.append(TreeNode(node.data))

        # iterate to both left and right of next level
        self.createlistshelper(node.left, lists, level+1)
        self.createlistshelper(node.right, lists, level+1)

        # return lists
        return lists

ld = ListofDepths()
root = TreeNode(0)
root.addleftchild(1)
root.addrightchild(2)
root.left.addleftchild(3)
root.right.addleftchild(4)
ls = ld.createlists(root)
print ls
for l in ls:
    for ll in l:
        print ll.data,
    print("")

