import Queue

import random
#creating a task
class Task:
    def __init__(self,time):
        self.timestamp = time
        #the time at which the task is sent to the printer
        self.pages = random.randrange(1,21)
        #the # of pages the task takes
#getters
    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages
#returns the downtime between the current second and when the task is issued to the printer
    def waitTime(self, currenttime):
        return currenttime - self.timestamp


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        #pages which the printer can print per minute
        self.currentTask = None
        #the task teh printer is working on
        self.timeRemaining = 0
        #the time the printer will take to complete the task it is working on

    def tick(self):
        #set the printer 1 sec closer to completing the current task, finishes the task if there are no pages left to print
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

def simulation(numSeconds, pagesPerMinute):
#make the printer, the queue, and the list of wait times
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append(nexttask.waitTime(currentSecond))
        #record the downtime between the completion of the last task and starting of this one
        labprinter.startNext(nexttask)
        #start the next task

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    #randomly decide if a new task should be issued to the printer.
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)




