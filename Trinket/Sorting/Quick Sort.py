from random import randint


def quicksort(list,start,stop):
    if start>stop:
        return list
    else:
        pivot = list[start]
        left = start
        right = stop
        while left <= right:
            while list[left] < pivot:
                left += 1
            while list[right] > pivot:
                right -= 1

            if left <= right:
                list[left], list[right] = list[right], list[left]
                left += 1
                right -= 1
                print('So the list becomes:')
                print(list)
                quicksort(list, start, right)
                quicksort(list, left, stop)
