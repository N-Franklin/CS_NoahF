import matplotlib.pyplot as plt
from time import sleep
from random import shuffle
plt.ion()
y = [i for i in range(100)]
x = [i for i in range(len(y))]
def myBarPlot():

    fig = plt.figure(1)
    fig.canvas.set_window_title('myBarPlot')

    for i in range(5):  
        print i
        plt.clf()
        plt.bar(x,y)
        plt.pause(0.01)
        shuffle(y)
    plt.show(block=True)