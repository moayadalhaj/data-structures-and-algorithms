class Dog:
    """
    create Dog class to handle their properties
    """
    def __init__(self,name):
        self.name=name
        self.kind='dog'
        self.next=None

class Cat:
    """
    create Cat class to handle their properties
    """
    def __init__(self,name):
        self.name=name
        self.kind='cat'
        self.next=None


class AnimalShelter:
    """
    Create AnimalShelter class with 
    enqueue: method that takes animal as argument and add it to the queue 
    dequeue: method that takes pref as argument and remove it from its queue 
    """
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,animal):
        """
        enqueue: method that takes animal as argument and add it to the queue 
        """
        if not self.rear:
                self.rear = animal
                self.front = animal
        else:
            self.rear.next = animal
            self.rear = animal

    def dequeue(self,pref=None):
        """
        dequeue: method that takes pref as argument and remove it from its queue 
        """
        if not self.rear:
            return None
        if (pref != 'dog' and pref != 'cat'):
            return None
        else:
            temp = self.front
            if self.front.kind == pref:
                self.front = self.front.next
                temp.next = None
                if not self.front:
                    self.rear = None
                return temp.name
            else:
                while temp.next:
                    if temp.next.kind == pref:
                        to_return = temp.next.name
                        temp.next =  temp.next.next
                        return to_return
                    else:
                        temp = temp.next
                return None
    

if __name__ == "__main__":
    miky = Dog('miky')
    boby=Dog('boby')
    losy=Dog('losy')
    fifo = Cat('fifo')
    kitty=Cat('kitty')
    mshmsh=Cat('mshmsh')
    animalShelter=AnimalShelter()
    animalShelter.enqueue(miky)
    animalShelter.enqueue(boby)
    animalShelter.enqueue(kitty)
    animalShelter.enqueue(losy)
    animalShelter.enqueue(fifo)
    animalShelter.enqueue(mshmsh)
    print(animalShelter.dequeue('cat'))
