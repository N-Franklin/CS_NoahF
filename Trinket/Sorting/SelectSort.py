def selectSort(a):
    l=len(a)
    #index of smallest value
    i=0
    #smallest value
    v=100000000000
    #sort as many times as values in list
    for s in range(0,l,1):

        v=100000000000
        #for one sort, go thru the list pick smallest value and swap
        for p in range(s,l,1):
        #if it's the smallest value
            if a[p]<v:
            #change the indices
                i=p
                v=a[p]
                a[i]=a[s]
                a[s]=v
    print a
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l=selectSort(alist)
print(l)