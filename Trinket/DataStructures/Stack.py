
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def getItem(self,index):
        return self.items[index]

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def matches(self,paren):
        return self.peek() == paren


#l denotes the string of ()'s
def parChecker(l):
    c = Stack()
    for i in range (0,len(l)):
        if l[i]=='(':
            c.push(l[i])
        elif l[i]==')'and not c.isEmpty():
            c.pop()
    return c.isEmpty()



def balSymChecker(l):
    c = Stack()
    for i in range (0,len(l)):
        if l[i]==['(' or '[' or '{']:
            c.push(i)
        elif l[i]==[')' or '}'or ']']:
            if c.matches(l[i]) and not c.isEmpty():
                c.pop()
            else:
                return False
    return c.isEmpty()
#int represente the integer being converted into base two

def divideByTwo(int):
    var=int
    c=Stack()
    while var>0:
        c.push(var%2)
        var/=2
    q=''
    for item in range(c.size()-1,-1,-1):
        q+=str(c.getItem(item))
    print q