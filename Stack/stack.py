class Stack:
    def __init__(self):
        self._items = []
        
    def is_empty(self):
        return not bool(self._items)
    
    def push(self, item):
        self._items.append(item)
        
    def pop(self):
        self._items.pop()
    
    def peek(self):
        return self._items[-1]
    
    def size(self):
        return len(self._items)
    

stck = Stack()

print(stck.is_empty())

stck.push(1)
stck.push('two')

print(stck.peek())
