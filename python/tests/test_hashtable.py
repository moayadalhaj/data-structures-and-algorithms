from Data_structure.hashtable.hashtable import HashTable
import pytest

@pytest.fixture
def hashtable():
    return HashTable()

def test_hash(hashtable):
    expected = 700
    actual = hashtable._HashTable__hash("d")
    assert actual == expected

def test_hash_word(hashtable):
    expected = 349
    actual = hashtable._HashTable__hash("moayad")
    assert actual == expected

def test_get_method(hashtable):
    expected = 21
    hashtable.add('moayad',21)
    actual = hashtable.get("moayad")
    assert actual == expected

def test_get_method_for_key_does_not_exist_in_hashtable(hashtable):
    expected = None
    hashtable.add('moayad',21)
    actual = hashtable.get("Emad")
    assert actual == expected

def test_get_when_there_collision(hashtable):
    expected = 21
    hashtable.add('moayad',21)
    hashtable.add('dayaom',10)
    actual = hashtable.get("moayad")
    assert actual == expected

def test_get_when_there_collision(hashtable):
    expected = 21
    expected2 = 10
    hashtable.add('moayad',21)
    hashtable.add('dayoam',10)
    actual = hashtable.get("moayad")
    actual2 = hashtable.get("dayoam")
    assert actual == expected
    assert actual2 == expected2

