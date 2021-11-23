from challenges.hashmap_left_join.hashmap_left_join import left_join
from challenges.hashmap_left_join.hashtable import HashTable

import pytest


def test_left_hash_and_empty(left_hash_fixture):
    expected = [['wrath', 'anger', 'Null'], ['diligent', 'employed', 'Null'],['fond', 'enamored', 'Null']]
    empty = HashTable()
    actual = left_join(left_hash_fixture, empty)
    assert actual == expected


def test_right_hash_and_empty(right_hash_fixture):
    expected = [['wrath', 'delight', 'Null'], ['fond', 'averse', 'Null'] ,['guide', 'follow', 'Null']]
    empty = HashTable()
    actual = left_join(right_hash_fixture, empty)
    assert actual == expected

def test_empty_and_left_hash(left_hash_fixture):
    expected = []
    empty = HashTable()
    actual = left_join(empty, left_hash_fixture)
    assert actual == expected

def test_empty_and_right_hash(right_hash_fixture):
    expected = []
    empty_tree = HashTable()
    actual = left_join(empty_tree, right_hash_fixture)
    assert actual == expected


def test_left_hash_and_right_hash_tables(left_hash_fixture,right_hash_fixture):
    expected = [['wrath', 'anger', 'delight'], ['diligent', 'employed', 'Null'], ['fond', 'enamored', 'averse']]
    actual = left_join(left_hash_fixture, right_hash_fixture)
    assert actual == expected

def test_right_hash_and_left_hash_tables(left_hash_fixture,right_hash_fixture):
    expected = [['wrath', 'delight', 'anger'], ['fond', 'averse', 'enamored'], ['guide', 'follow', 'Null']]
    actual = left_join(right_hash_fixture, left_hash_fixture)
    assert actual == expected

@pytest.fixture
def left_hash_fixture():
    left_hash = HashTable()
    left_hash.add('fond', 'enamored')
    left_hash.add('wrath', 'anger')
    left_hash.add('diligent', 'employed')
    return left_hash

@pytest.fixture
def right_hash_fixture():
    right_hash = HashTable(10)
    right_hash.add('fond', 'averse')
    right_hash.add('wrath', 'delight')
    right_hash.add('guide', 'follow')
    return right_hash
