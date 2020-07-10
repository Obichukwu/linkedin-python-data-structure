
class Deque:
    def __init__(self):
        self.items= []
    
    def add_front(self, item):
        self.items.insert(0,item)
    
    def add_rear(self, item):
        self.items.append(item)
    
    def remove_front(self):
        return self.items.pop(0)
    
    def remove_rear(self):
        return self.items.pop()
    
    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    
    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == [] 
