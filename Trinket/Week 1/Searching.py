def sequentialSearch(alist,item):
    l=len(alist)
    for a in range (l):
        if alist[a]==item:
            return True
    return False

def binarySearch(alist,item, start,stop):
    l=start-stop
    if stop<=start:
        return False
    r=(start+l/2)
    if alist[r]==item:
        return True
    elif alist[r]<item:
        return binarySearch(alist,item,start,r)
    elif alist[r]>item:
        return binarySearch(alist,item,r,stop)