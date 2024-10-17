from abc import ABC, abstractmethod
#
class Queue(ABC):
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def enqueue(self, obj):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class Node():
    def __init__(self, data, link):
        self.data = data
        self.link = link

    def __repr__(self):
        return f"({self.data}, {self.link})"

class LLQueue(Queue):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.head == None and self.tail == None

    def enqueue(self, obj):
        assert obj != None

        if self.head == None and self.tail == None:
            self.head = Node(obj, None)
            self.tail = self.head
        
        else:
            to_queue = Node(obj, None)
            self.tail.link = to_queue
            self.tail = to_queue

        self.size += 1
    
    def dequeue(self):
        ''' Return head of queue.'''
        data = None

        if self.head:
            dequeued = self.head
            self.head = self.head.link

            if self.head == None:
                self.tail = None

            if dequeued:
                data = dequeued.data
                self.size -= 1

        return data

    def __repr__(self):
        ''' Print the LLQueue's contents'''
        curr = self.head
        content = []

        while curr != None:
            content.append(curr.data)
            curr = curr.link
        
        return str(content)

    def __abs__(self):
        ''' Return size of queue.'''
        assert self.size >= 0
        return self.size
    
    def __len__(self):
        assert self.size >= 0
        return self.size
