def binarySearch(list,int,start,stop):
    mid=(stop-start)/2+start
    if list[mid]==int:
        return mid
    elif list[mid]>int:
        if mid==0:
            return False
        else:
            return binarySearch(list,int,start,mid)
    elif list[mid]<int:
        if mid==len(list)-1:
            return False
        else:
            return binarySearch(list,int,mid,stop)

q=[17, 20, 26, 31, 44, 54, 55, 77, 93]
print binarySearch(q,20,0,8)