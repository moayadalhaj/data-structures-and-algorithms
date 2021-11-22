from Data_structure.tree.trees import BinaryTree, Node
from Data_structure.hashtable.hashtable import HashTable


def tree_intersection(tree1,tree2):
    """
    A function that takes two tree as arguments and return the common values in the two trees

    input: tree1,tree2
    output: set of values found in both trees.
    """
    values = []
    hashtable = HashTable()
    if not tree1.root or not tree2.root:
        return []
    def looping(node):
        nonlocal hashtable
        hashtable.add(str(node.value),1)
        if node.left:
            looping(node.left)
        if node.right:
            looping(node.right)
    def checking(node):
        nonlocal hashtable
        if hashtable.contains(str(node.value)):
            values.append(node.value)
        if node.left:
            checking(node.left)
        if node.right:
            checking(node.right)
    looping(tree1.root)
    checking(tree2.root)
    return values

if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.root = Node(150)
    tree1.root.left = Node(100)
    tree1.root.right = Node(250)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)
    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.right = Node(500)
    tree1.root.right.right.left = Node(300)

    tree2 = BinaryTree()
    tree2.root = Node(42)
    tree2.root.left = Node(100)
    tree2.root.right = Node(600)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)
    tree2.root.left.right.left = Node(125)
    tree2.root.left.right.right = Node(175)
    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)
    tree2.root.right.right.right = Node(500)
    tree2.root.right.right.left = Node(4)

    print(tree_intersection(tree1,tree2))
