
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        item, *self.items = self.items
        return item
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == [] 