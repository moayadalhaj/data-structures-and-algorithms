"""
The implementation of Node class, Linked list class, and Hashmap class.
"""


class Node:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table

        """
        self.size = size
        self._buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value
        Return : No return value
        """

        index = self.__hash(key)

        if not self._buckets[index]:
          self._buckets[index] = LinkedList()
        my_value = [key,value]
        self._buckets[index].insert(my_value)

    def get(self, key):
        """
        Retrieve the most recent value of in oour hasmap for the given key

        :param key str
        :rvalue any
        """
        # calculate index
        index = self.__hash(key)
        # check if there is a non empty bucket at the index
        if self._buckets[index]:
            # iterate over linked list
            linked_list = self._buckets[index]
            current = linked_list.head
            while current:
            # check if the key in each node matches
                if current.value[0] == key:
                    # return the value of the node with the mathcing key
                    return current.value[1]
                current = current.next

        # return None
        return None

    def contains(self, key):
        """
        check if the key exists in hashtable or not
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        """
        index = self.__hash(key)
        # check if there is a non empty bucket at the index
        if self._buckets[index]:
            # iterate over linked list
            linked_list = self._buckets[index]
            current = linked_list.head
            while current:
            # check if the key in each node matches
                if current.value[0] == key:
                    # return the value of the node with the mathcing key
                    return True
                current = current.next

        # return None
        return False


if __name__ == '__main__':
    hashtable = HashTable()
    hashtable.add('moayad',21)
    hashtable.add('dayaom',10)
    print(hashtable.contains('moayad'))
    print(hashtable._buckets[349].head.value)
    print(hashtable._buckets[349].head.next.value)
