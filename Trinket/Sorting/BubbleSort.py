def bubbleSort(a):
    l=len(a)
    v=0
    for p in range(1,l,1):
        if a[p]<a[p-1]:
            v=a[p]
            a[p]=a[p-1]
            a[p-1]=v
            print a
            bubbleSort(a)