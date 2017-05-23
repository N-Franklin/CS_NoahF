class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def parChecker(l):
    c = Stack()
    for i in (len(l)):
        if l[i-1]=='(':
            c.push(i)
        elif l[i-1]==')':
            c.pop()
    return c.isEmpty()
