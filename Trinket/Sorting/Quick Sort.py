from random import randint
'''
def swap(list,pivot,start,stop,pivoti):
    Thing1=findLeft(list,pivot,start,stop,pivoti)
    Thing2=findRight(list,pivot,start,stop,pivoti)
    list[Thing1],list[Thing2]=list[Thing2],list[Thing1]
    if Thing1==pivoti:
        pivoti=Thing2
    elif Thing2==pivoti:
        pivoti=Thing1


def findLeft(list,pivot,start,stop,pivoti):
    for index in (start, pivoti+1,1):
        if list[index]>=pivot:
            return index;
    return 0;

def findRight(list,pivot,start,stop,pivoti):
    for index in (start, pivoti-1,1):
        if list[index]<=pivot:
            return index;
    return 0;

def QuickSort(list,start,stop):
    pivoti=start
    if start<stop:
        pivot=list[start]
        swap(list,pivot,start,swap,pivoti)
'''

def QuickSort(list,start,stop):
    if start>=stop:
        i=0;
    else:
        pivot = list[start]
        left = start
        right = stop-1
        while left < right:
            while list[left] < pivot:
                left += 1
            while list[right] >= pivot:
                right -= 1

            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
            print('So the list becomes:')
            print(list)
            print str(right)+','+str(left)
        QuickSort(list, start, right)
        QuickSort(list, left, stop)
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l=QuickSort(alist,0,9)
print(l)