class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

class Queue:
    def __init__(self, collection=[]):
        self.value = collection

    def peek(self):
        if len(self.value):
            return True
        return False

    def enqueue(self,item):
        self.value.append(item)

    def dequeue(self):
        return self.value.pop(0)

def breadth_first(tree):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """
    # Queue breadth <-- new Queue()
    if not tree.root:
        return 'The tree is empty'
    breadth = Queue()
    # breadth.enqueue(root)
    breadth.enqueue(tree.root)

    list_of_items = []

    while breadth.peek():
        front = breadth.dequeue()
        list_of_items += [front.value]

        if front.left:
            breadth.enqueue(front.left)

        if front.right:
            breadth.enqueue(front.right)

    return list_of_items

if __name__ == "__main__":
    tree = Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    print(breadth_first(tree))
