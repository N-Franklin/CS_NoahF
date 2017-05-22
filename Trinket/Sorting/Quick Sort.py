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
    if stop-start<1:
        return list
    else:
        pivot = list[start]
        left = start
        right = stop
        while left < right:
            while list[left] < pivot:
                left += 1
                print 'left: ' + str(left)
            while list[right] > pivot and right>0:
                right -= 1
                print 'right: ' + str(right) +' '+str(pivot)
            print 'Swapping: ' + str(list[left]) + ', ' + str(list[right])
            if list[right] <= pivot and list[left] >= pivot and left<=right:
                print 'Swapping: ' + str(left) + ', ' + str(right)
                list[left], list[right] = list[right], list[left]
                left += 1
                right -= 1
                print(list)

        print 'sortingl ' + str(start) +' '+str(right)
        QuickSort(list, start, right)
        print 'sortingr ' + str(left) + ' ' + str(stop)
        QuickSort(list, left, stop)
#alist = [13, 76, 93, 17, 77, 31, 55, 44, 20,82,99]
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l=QuickSort(alist,0,10)
print(l)
