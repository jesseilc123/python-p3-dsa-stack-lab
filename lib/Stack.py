class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, item):
        if len(self.items) >= self.limit:
            self.items.append(item)
            self.items.pop()
        else:
            self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def peek(self):
        self.items.peek()
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        else:
            return False

    def search(self, target):
        if target in self.items:
            return (len(self.items) - 1) - self.items.index(target)
        else:
            return - 1

