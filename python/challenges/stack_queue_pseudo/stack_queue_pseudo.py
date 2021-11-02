class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
    create a stack class that containes three methods
    push: to add a new node at the top of stack
    pop: to delete the top node in the stack
    peek: to return the value of top node if it exist
    """
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        push: to add a new node at the top of stack
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
        pop: to delete the top node in the stack
        """
        if self.top == None:
            raise Exception("This stack is empty")
        temp=self.top
        self.top=self.top.next
        temp.next=None

        return temp.value

    def peek(self):
        """
        peek: to return the value of top node if it exist
        """
        try:
            return self.top.value
        except:
            return "This stack is empty"


class PseudoQueue:
    """
    PseudoQueue class that implement a standard
    queue interface which containes two methods
    enqueue: which inserts value into the PseudoQueue, using a first-in, first-out approach.
    dequeue: which extracts a value from the PseudoQueue, using a first-in, first-out approach.
    """
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    def enqueue(self, value):
        """
        enqueue: which inserts value into the PseudoQueue,
        using a first-in, first-out approach.
        """
        node = Node(value)
        if not self.rear.top:
            self.front.top = node
            self.rear.top = node
        else:
            temp = self.rear.top
            self.rear.push(value)
            self.rear.top.next = None
            temp.next =  self.rear.top

    def dequeue(self):
        """
        dequeue: which extracts a value from the PseudoQueue,
        using a first-in, first-out approach.
        """
        try:
            temp = self.front.pop()
            return temp
        except:
            return 'This queue is empty'




if __name__ == '__main__':
    a = PseudoQueue()
    a.enqueue(5)
    a.enqueue(6)
    a.enqueue(7)
    print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())
