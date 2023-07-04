class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self,item) -> None: 
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0 

    def size(self):
        return len(self.items) 

    def pop(self): 
        if not self.is_empty():
            return self.items.pop()
    
    