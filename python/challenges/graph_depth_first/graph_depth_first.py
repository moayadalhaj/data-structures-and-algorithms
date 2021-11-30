from collections import deque


class Vertex:
    """
    Class for Adding a node to the graph
    Arguments: value
    Returns: The added node
    """
    def __init__(self, value):
        """
        Initalization for a Vertex to hold a value.
        """
        self.value = value

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendLeft(value)

    def dequeue(self):
        self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Stack:
    def __init__(self):
        """
        The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
        """
        self.dq = deque()

    def push(self, value):
        """
        Store the passed value in a node and then push the node on top of the stack.

        PARAMETERS
        ----------
        value: any
        The value that will get stored in a node to be pushed on top of the stack.
        """
        self.dq.append(value)

    def pop(self):
        """
            Return the top node in a stack.
            """
        self.dq.pop()

class Edge:
    """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    """
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        """
        Initalization for a hashmap to hold the vertices
        """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
        Method for Adding a node to the graph
        Arguments: value
        Returns: The added node
        """
        # new node
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
        Method to get all nodes in Graph
        Arguments: None
        return: All nodes
        """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """ """
        return self.__adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action=(lambda vertex: None)):
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)

        neighbors = self.get_neigbors(current_vertex)

        for edge in neighbors:
            neighbour =  edge.vertex

            if neighbour not in visited:
                visited.add(neighbour)
                queue.enqueue(neighbour)


    def depth_first(self, node):
        """
        A method that return the nodes values in pre-order depth first traversal

        input: node
        output: nodes values in pre-order
        """
        list = []
        def walk(vertex):
            list.append(vertex.value)
            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                if neighbor.vertex.value not in list:
                    walk(neighbor.vertex)
        walk(node)
        return list


if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')

    graph.add_edge(a,b)
    graph.add_edge(a,d)
    graph.add_edge(b,c)
    graph.add_edge(b,d)
    graph.add_edge(c,g)
    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)
    graph.add_edge(f,h)


    print(graph.depth_first(a))
