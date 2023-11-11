class Stack:
    items = []
    def __init__(self, items):
        for i in items:
            self.items.append(i)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if (self.is_empty() == False):
            return(self.items.pop(len(self.items)-1))
    def is_empty(self):
        return(self.items == [])
class Queue:
    items = []
    def __init__(self, items):
        for i in items:
            self.items.append(i)
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if (self.is_empty() == False):
            return(self.items.pop(0))
    def is_empty(self):
        return(self.items == [])