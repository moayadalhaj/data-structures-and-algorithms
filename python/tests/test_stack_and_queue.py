from Data_structure.stack_and_queue.stack_and_queue import  Stack, Queue
import pytest


def test_push(stack_values):
    expected='M'
    actual= stack_values.top.value
    assert expected==actual

def test_pop(stack_values):
    expected='M'
    actual= stack_values.pop()
    assert expected==actual

def test_pop_when_stack_is_empty(stack_values):
    expected="This stack is empty"
    stack_values.pop() == 'M'
    stack_values.pop() == 4
    stack_values.pop() == 2
    with pytest.raises(Exception) as actual:
        stack_values.pop()
    assert str(actual.value)==expected

def test_peek(stack_values):
    expected='M'
    actual= stack_values.peek()
    assert expected==actual

def test_is_empty(stack_values):
    expected=False
    actual= stack_values.is_empty()
    assert expected==actual



def test_enqueue_when_queue_is_empty():

    expected=None
    q = Queue()
    actual=q.front
    assert expected==actual
    assert q.rear == None


def test_enqueue(queue_values):
    expected1=10
    expected2=6
    actual1=queue_values.rear.value
    actual2=queue_values.front.value

    assert expected1==actual1
    assert expected2==actual2

def test_dequeue(queue_values):
    excpected=6
    excpected2=None
    data = queue_values.dequeue()
    actual=data.value
    actual2=data.next
    assert actual == excpected
    assert actual2 == excpected2


def test_peek(queue_values):

    expected=6
    actual=queue_values.peek()
    assert expected==actual

def test_peek_when_queue_is_empty():
    expected='This queue is empty'
    q = Queue()
    actual=q.peek()

    assert expected==actual

def test_is_empty(queue_values):
    q = Queue()
    assert q.is_empty() == True
    assert queue_values.is_empty() == False


# Decorator
@pytest.fixture
def stack_values():
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push('M')
    return stack

@pytest.fixture
def queue_values():
    queue = Queue()
    queue.enqueue(6)
    queue.enqueue(8)
    queue.enqueue(10)
    return queue
