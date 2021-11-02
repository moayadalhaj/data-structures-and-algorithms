from challenges.tree_breadth_first.tree_breadth_first import *


import pytest

def test_breadthFirst():
    expected = 'The tree is empty'
    new_tree = Tree()
    actual =breadth_first(new_tree)
    assert  actual == expected

def test_breadthFirst(prepared_tree):
    expected = ['A','B','C','D','E','F']
    actual = breadth_first(prepared_tree)
    assert  actual == expected



@pytest.fixture
def prepared_tree():
    tree = Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree
