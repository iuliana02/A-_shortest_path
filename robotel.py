class Node:
    # Initialize the class
    def __init__(self, name: str, parent: str, x, y):
        self.name = name
        self.parent = parent
        self.x = x
        self.y = y
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))


class Graph:
    pass


nodes=[]
n1 = Node('START','A', 0, 1)
n2 = Node('B','C',1,2)
