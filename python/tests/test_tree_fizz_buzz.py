from challenges.tree_fizz_buzz.tree_fizz_buzz import *
import pytest


def test_empty_k_ary_tree():
    new_tree = k_ary_tree()
    assert fizz_buzz_tree(new_tree) == None


def test_filled_fizz_buzz_tree(k_arr):
    tree = fizz_buzz_tree(k_arr)
    # for the new tree
    assert tree[0] == 'Fizz'
    assert tree[-1] == 'FizzBuzz'


@pytest.fixture
def k_arr():
    tree = k_ary_tree()
    tree.root = Node(3)
    tree.root.children.append(Node(2))
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(15))
    tree.root.children[0].children.append(Node(4))
    tree.root.children[0].children.append(Node(6))
    tree.root.children[0].children.append(Node(7))
    tree.root.children[1].children.append(Node(9))
    tree.root.children[1].children.append(Node(30))
    return tree
