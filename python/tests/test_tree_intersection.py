from challenges.tree_intersection.tree_intersection import tree_intersection
from Data_structure.tree.trees import BinaryTree, Node
import pytest

def test_tree1_and_empty_tree(tree1):
    expected = []
    empty_tree = BinaryTree()
    actual = tree_intersection(tree1, empty_tree)
    assert actual == expected


def test_tree2_and_empty_tree(tree2):
    expected = []
    empty_tree = BinaryTree()
    actual = tree_intersection(tree2, empty_tree)
    assert actual == expected


def test_regular_complicated_trees(tree1, tree2):
    expected = [100,160,125,175,200,350,500]
    actual = tree_intersection(tree1, tree2)
    assert actual == expected

@pytest.fixture
def tree1():
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
    return tree1

@pytest.fixture
def tree2():
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
    return tree2

