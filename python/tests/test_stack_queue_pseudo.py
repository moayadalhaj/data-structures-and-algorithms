from challenges.stack_queue_pseudo.stack_queue_pseudo import *
import pytest


def test_enqueue_when_it_is_empty():
    expected=None
    expected2=None
    q = PseudoQueue()
    actual = q.front.top
    actual2=q.rear.top
    assert  actual == expected
    assert actual2 == expected2

def test_enqueue():
    expected=5
    expected2=5
    q = PseudoQueue()
    q.enqueue(5)
    actual = q.front.top.value
    actual2=q.rear.top.value
    assert  actual == expected
    assert actual2 == expected2

def test_enqueue(queue_values):
    expected=8
    actual=queue_values.front.top.value
    assert actual==expected

def test_dequeue(queue_values):
    expected=6
    queue_values.dequeue()
    q = queue_values.dequeue()
    actual=q

    assert actual==expected

@pytest.fixture
def queue_values():
    queue = PseudoQueue()
    queue.enqueue(8)
    queue.enqueue(6)
    queue.enqueue(4)
    return queue
