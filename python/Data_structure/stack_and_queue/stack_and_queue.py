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
    is_empty: to return boolean value if the stack empty or not
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

    def is_empty(self):
        """
        is_empty: to return boolean value if the stack empty or not
        """ 
        return self.top == None

class Queue:
    """
    create a Queue class that containes three methods
    enqueue: to add a new node at the top of stack
    dequeue: to delete the front node in the stack
    peek: to return the value of front node if it exist
    is_empty: to return boolean value if the queue empty or not
    """
        
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        """
        enqueue: to add a new node at the top of stack
        """
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        dequeue: to delete the front node in the stack
        """
        try:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        except:
            return "This queue is empty"
    
    def peek(self):
        """
        peek: to return the value of front node if it exist
        """
        try:
            return self.front.value
        except:
            return "This queue is empty"
    
    def is_empty(self):
        """
        is_empty: to return boolean value if the queue empty or not
        """
        return self.front == None

if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push('d')
    print(stack.top.value)
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.rear.value)
    