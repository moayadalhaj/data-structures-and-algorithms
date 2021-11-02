from Data_structure.linked_list.linked_list import Linked_list, Node, zipLists

def test_Node():
    # Arrange any data that you need to run your test
    expected1=5
    expected2=3
    # Act on the subject of the test to produce some actual output
    a = Node(5,3)
    # Assert
    assert a.value == expected1
    assert a.next == expected2

def test_empety_linked_list():
    # Arrange any data that you need to run your test
    expected=None
    # Act on the subject of the test to produce some actual output
    a = Linked_list()
    # Assert
    assert a.head == expected

def test_the_head_value():
    # Arrange any data that you need to run your test
    expected=7
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(5)
    ll.insert(7)
    actual=ll.head.value
    # Assert
    assert actual == expected

def test_insert_multiple_nodes():
    # Arrange any data that you need to run your test
    expected='{ 8 } -> { 5 } -> None'
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(5)
    ll.insert(8)
    actual=str(ll)
    # Assert
    assert actual == expected

def test_insert():
    # Arrange any data that you need to run your test
    expected1=5
    expected2=None
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(5)
    actual1=ll.head.value
    actual2=ll.head.next
    # Assert
    assert actual1 == expected1
    assert  actual2 == expected2

def test_value_include_in_linjed_list():
    # Arrange any data that you need to run your test
    excepted=True
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(5)
    actual=ll.includes(5)
    # Assert
    assert actual == excepted

def test_value_doesnt_include_in_linked_list():
    # Arrange any data that you need to run your test
    excepted=False
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(3)
    actual=ll.includes(7)
    # Assert
    assert actual == excepted

def test_str():
    # Arrange any data that you need to run your test
    excpected='{ 17 } -> { s } -> { 5 } -> None'
    # Act on the subject of the test to produce some actual output
    ll=Linked_list()
    ll.insert(5)
    ll.insert('s')
    ll.insert(17)
    # Assert
    assert str(ll) == excpected

def test_append_1():
    ll = Linked_list()
    ll.append(1)
    assert ll.head.value is 1
    ll.append(2)
    assert ll.head.next.value is 2
    assert ll.head.next.next is None

def test_insertAfter():
    ll = Linked_list()
    assert ll.insertAfter(5,1) == "No change, method exception"
    ll.append(5)
    ll.insertAfter(5,1)
    assert ll.head.next.value == 1
    assert ll.head.next.next == None
    ll.insertBefore(1,4)
    assert ll.head.next.value == 4
    assert ll.head.next.next.value == 1

def test_insertBefore():
    ll = Linked_list()
    assert ll.insertBefore(5,1) == "No change, method exception"
    ll.append(5)
    ll.insertBefore(5,1)
    assert ll.head.value == 1
    ll.insertBefore(5,2)
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 5

def test_kthFromEnd():
    ll = Linked_list()
    assert ll.kthFromEnd(1) == 'This linked list is not long enough'
    ll.append(5)
    assert ll.kthFromEnd(1) == 'This linked list is not long enough'
    ll.kthFromEnd(0) == 5
    ll.append(17)
    ll.insert('foo')
    ll.append(61)
    assert ll.kthFromEnd(2) == 5
    assert ll.kthFromEnd(3) == 'foo'
    assert ll.kthFromEnd(6) == 'This linked list is not long enough'
    assert ll.kthFromEnd(-1) == 'foo'

def test_two_empty_ll():
    ll1 = Linked_list()
    ll2 = Linked_list()
    h=zipLists(ll1,ll2)
    assert h.head == None

def test_one_empty_ll2():
    ll1 = Linked_list()
    ll2 = Linked_list()
    ll1.append(1)
    ll1.append(3)
    ll1.append(6)
    ll2 = Linked_list()
    assert str(zipLists(ll1,ll2)) == '{ 1 } -> { 3 } -> { 6 } -> None'


def test_one_empty_ll1():
    ll1 = Linked_list()
    ll2 = Linked_list()
    ll2.append(1)
    ll2.append(5)
    ll2.append(9)

    assert str(zipLists(ll1,ll2)) == '{ 1 } -> { 5 } -> { 9 } -> None'

def test_two_equal_length_ll():
    ll1 = Linked_list()
    ll2 = Linked_list()
    ll1.append(1)
    ll1.append(3)
    ll1.append(6)
    ll2.append(1)
    ll2.append(5)
    ll2.append(9)

    assert str(zipLists(ll1,ll2)) == '{ 1 } -> { 1 } -> { 3 } -> { 5 } -> { 6 } -> { 9 } -> None'

def test_ll1_longer_than_ll2():
    ll1 = Linked_list()
    ll2 = Linked_list()
    ll1.append(1)
    ll1.append(3)
    ll1.append(6)
    ll2.append(5)
    ll2.append(9)

    assert str(zipLists(ll1,ll2)) == '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 6 } -> None'

def test_ll2_longer_than_ll1():
    ll1 = Linked_list()
    ll2 = Linked_list()
    ll1.append(1)
    ll1.append(3)
    ll2.append(2)
    ll2.append(5)
    ll2.append(9)
    assert str(zipLists(ll1,ll2)) == '{ 1 } -> { 2 } -> { 3 } -> { 5 } -> { 9 } -> None'
