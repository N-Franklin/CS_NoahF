
def search(list,int):
    return binarySearch(list,int,0,len(list)-1,0)

def binarySearch(list,int,start,stop,count):
    count+=1
    if count==len(list)-1:
        if list[len(list)-1]==int:
            return len(list)
        else:
            return False
    mid=(stop-start)/2+start
    if list[mid]==int:
        return mid
    elif list[mid]>int:
        if mid==0:
            return False
        else:
            return binarySearch(list,int,start,mid,count)
    elif list[mid]<int:
        if mid==len(list)-1:
            return False
        else:
            return binarySearch(list,int,mid,stop,count)

q=[17, 20, 26, 31, 44, 54, 55, 77, 93]
print binarySearch(q,0,8,0)