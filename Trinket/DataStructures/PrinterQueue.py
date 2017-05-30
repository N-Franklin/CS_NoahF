from random import randint
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

class Task:

    def __init__(self,time):
        #the time the task is sent to printer
        self.time=time

        self.page= randint(0,20)



class TaskList:
    def __init__(self,classnum):
        self.tasks=[]

    def buildclass(self,time):
        self.append(Task(time))


