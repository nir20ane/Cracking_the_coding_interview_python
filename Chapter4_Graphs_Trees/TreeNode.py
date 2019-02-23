class TreeNode(object):
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data

    def addleftchild(self, data=None):
        node = TreeNode(data)
        self.left = node
        node.parent = self

    def addrightchild(self, data=None):
        node = TreeNode(data)
        self.right = node
        node.parent = self
