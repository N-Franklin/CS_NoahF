#Not quite insert sort but close enough(actually bubble sort)
def insertSort(a):
    l=len(a)
    v=0
    for p in range(1,l,1):
        if a[p]<a[p-1]:
            v=a[p]
            a[p]=a[p-1]
            a[p-1]=v
            print a
            insertSort(a)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l=insertSort(alist)
print(l)


