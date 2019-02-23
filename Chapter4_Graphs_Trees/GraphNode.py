class GraphNode(object):
    def __init__(self, data=None):
        self.data = data;
        self.isvisited = False
        self.neighbors = []

    def visit(self):
        self.isvisited = True

    def visited(self):
        return self.isvisited

    def addneighbor(self, node):
        self.neighbors.append(node)
        node.neighbors.append(self)

    def getneighbor(self):
        return self.neighbors

    def adddirectneighbor(self, node):
        self.neighbors.append(node)
