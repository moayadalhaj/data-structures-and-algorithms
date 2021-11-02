class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

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

class BinaryTree:
    """
    Create a Binary Tree class
    Define a method for each of the depth first traversals:
    - pre order
    - in order
    - post order which returns an array of the values, ordered appropriately.
    """
    def __init__(self):
        self.root = None
        self.maximum = 0

    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains

        input: None

        output: tree items

        sub method : walk () to make the recursion staff
        """
        try:
            if not self.root:
                return 'Tree is empty'
            list_of_items = []
            def walk(node):
                list_of_items.append(node.value)
                
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
            walk(self.root)
            return list_of_items 
        except:
            return "Pre_order method failed"
    
    def in_order(self):
        """
        A binary tree method which returns a list of items that it contains

        input: None

        output: tree items

        sub method : walk () to make the recursion staff
        """
        try:
            if not self.root:
                return 'Tree is empty'
            list_of_items = []
            def walk(node):
                
                if node.left:
                    walk(node.left)

                list_of_items.append(node.value)

                if node.right:
                    walk(node.right)
            walk(self.root)
            return list_of_items 
        except:
            return "in_order method failed"

    def post_order(self):
        """
        A binary tree method which returns a list of items that it contains

        input: None

        output: tree items

        sub method : walk () to make the recursion staff
        """
        try:
            if not self.root:
                return 'Tree is empty'
            list_of_items = []
            def walk(node):
                
                if node.left:
                    walk(node.left)


                if node.right:
                    walk(node.right)

                list_of_items.append(node.value)
            walk(self.root)
            return list_of_items 
        except:
            return "post_order method failed"
    
    def bfs(self):
        """
        A binary tree method which returns a list of items that it contains

        input: None

        output: tree items
        """
        # Queue breadth <-- new Queue()
        breadth = Queue()
        # breadth.enqueue(root)
        breadth.enqueue(self.root)

        list_of_items = []

        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.value]

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_of_items
    
    def tree_max(self):
        """
        A method to find the maximum value in the tree
        
        arguments: None
        output: number maximum value in the tree
        """
        try:
            if not self.root:
                return 'Tree is empty'
            def walk(node):
                if node.value > self.maximum:
                    self.maximum = node.value
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
            walk(self.root)
            return self.maximum 
        except:
            return "tree max method failed"


class BinarySearchTree(BinaryTree):
    """
    
    Binary Search Tree class
    This class is a sub-class of the Binary Tree Class, with the following additional methods:

    - Add method: Adds a new node with that value in the correct location in the binary search tree.
        - Arguments: value
        - Return: nothing
    - Contains:
        - Argument: value
        - Returns: boolean indicating whether or not the value is in the tree at least once.
    """
    def __init__(self):
        super().__init__()

    def add(self,value):
        """
        - Add method: Adds a new node with that value in the correct location in the binary search tree.
        - Arguments: value
        - Return: nothin
        """
        if not self.root:
            self.root = Node(value)
            return
        def assigns(node):
            if value > node.value:
                if not node.right:
                    node.right = Node(value)
                    return    
                assigns(node.right)
            else:
                if not node.left:
                    node.left = Node(value)
                    return
                assigns(node.left)
        assigns(self.root)

    def Contains(self,value):
        """
        - Contains method: to check if the value is in tree or not
        - Argument: value
        - Returns: boolean indicating whether or not the value is in the tree at least once.
        """
        bool = False
        if not self.root:
            return False
        def check(node):
            nonlocal bool
            if node.value == value:
                bool = True
                return
            elif value > node.value:
                if not node.right:
                    return
                check(node.right)
            else:
                if not node.left:
                    return
                check(node.left)

        check(self.root)
        return bool

if __name__=='__main__':
    a_node = Node(2)
    b_node = Node(7)
    c_node = Node(5)
    d_node = Node(2)
    e_node = Node(6)
    f_node = Node(9)
    f_node_left = Node(4)
    e_left_node = Node(5)
    e_right_node = Node(11)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left= d_node
    b_node.right = e_node
    c_node.right = f_node
    e_node.left = e_left_node
    e_node.right = e_right_node
    f_node.left = f_node_left
    tree=BinaryTree()
    tree.root = a_node
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())
    print(tree.tree_max())