class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotpotatoQ(list,count,start):
    q= Queue
    for element in list:
        q.enqueue(element)
    return eliminate

def eliminate(q,count):
    if q.size==1:
        return q.dequeue
    else:
        for i in range(0,count,1):
            q.enqueue(q.dequeue)
        q.dequeue
        return eliminate(q,count)

def hotpotato(list,count,start):
    if len(list)==1:
        return list[0]
    else:
        q=(count+start)%len(list)
        del list[q]
        hotpotato(list,count,q%len(list))