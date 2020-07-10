class Stack:

    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        """
        This method returns the length of the list that represents the stack

        This method runs in constant time
        """
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    