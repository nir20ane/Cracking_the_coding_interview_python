"""* 4.1 Route Between Nodes:
* Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
* """
from GraphNode import GraphNode
from collections import deque

class RouteBetweenNodes(object):
    def routeexists(self, start, end):
        if start == end:
            return True
        q = deque()
        q.append(start)
        start.visit()
        while q:
            r = q.popleft()
            if r == end:
                return True
            for neighbor in r.getneighbor():
                if not neighbor.visited():
                    neighbor.visit()
                    q.append(neighbor)
        return False

rb = RouteBetweenNodes()
node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node6 = GraphNode(6)
node1.addneighbor(node2)
node6.addneighbor(node3)
print(rb.routeexists(node1, node2))
print(rb.routeexists(node6, node3))

node4 = GraphNode(4)
node5 = GraphNode(5)
print(rb.routeexists(node4, node5))
