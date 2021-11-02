"""
Tests for Binary Tree
"""
import pytest
from Data_structure.tree.trees import BinaryTree, Node ,BinarySearchTree


def test_pre_order_empty_tree():
    tree = BinaryTree()
    assert tree.pre_order() == 'Tree is empty'

def test_in_order_empty_tree():
    tree = BinaryTree()
    assert tree.in_order() == 'Tree is empty'

def test_post_order_empty_tree():
    tree = BinaryTree()
    assert tree.post_order() == 'Tree is empty'

def test_pre_order(tree_values):
    # set expected list
    expected = ["A", "B", "D", "E", "C", "F"]
    # set actual to return value of pre_order call
    actual = tree_values.pre_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_pre_order_ passed")

def test_post_order(tree_values):
    # set expected list
    expected = ["D", "E", "B", "F", "C", "A"]
    # set actual to return value of post_order call
    actual = tree_values.post_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_post_order_ passed")

def test_in_order(tree_values):
    # set expected list
    expected = ["D", "B", "E", "A", "F", "C"]
    # set actual to return value of in_order call
    actual = tree_values.in_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_in_order_ passed")

def test_bfs(tree_values):
    # set expected list
    expected = ["A", "B", "C", "D", "E", "F"]
    # set actual to return value of bfs call
    actual = tree_values.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs passed")

def test_bfs_2(tree_values2):
    # set expected list
    expected = ["1", "2", "3", "4"]
    # set actual to return value of bfs call
    actual = tree_values2.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs_2 passed")

def test_Binary_Search_Tree_pre_order(binery):
    # set expected list
    expected = [23,8,4,16,42,27,85]
    # set actual to return value of bfs call
    actual = binery.pre_order()
    # assert actual is same as expected
    assert actual == expected

def test_Binary_Search_Tree_in_order(binery):
    # set expected list
    expected = [4,8,16,23,27,42,85]
    # set actual to return value of bfs call
    actual = binery.in_order()
    # assert actual is same as expected
    assert actual == expected

def test_Binary_Search_Tree_post_order(binery):
    # set expected list
    expected = [4,16,8,27,85,42,23]
    # set actual to return value of bfs call
    actual = binery.post_order()
    # assert actual is same as expected
    assert actual == expected

def test_tree_max_with_empty_tree():
    expected = 'Tree is empty'
    tree = BinaryTree()
    actual = tree.tree_max()
    assert actual == expected

def test_tree_max(max_values):
    expected = 11
    actual = max_values.tree_max()
    assert actual == expected

@pytest.fixture
def tree_values():
    a_node = Node('A')
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    e_node = Node('E')
    f_node = Node('F')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left= d_node
    b_node.right = e_node
    c_node.left = f_node
    tree=BinaryTree()
    tree.root = a_node
    return tree

@pytest.fixture
def tree_values2():
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    return tree

@pytest.fixture
def binery():
    newTree = BinarySearchTree()
    newTree.add(23)
    newTree.add(42)
    newTree.add(8)
    newTree.add(4)
    newTree.add(16)
    newTree.add(27)
    newTree.add(85)
    return newTree

@pytest.fixture
def max_values():
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
    return tree
