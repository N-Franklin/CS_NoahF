def sequentialSearch(alist,item):
    l=len(alist)
    for a in range (l):
        if alist[a]==item:
            return True
    return False

def binarySearch(alist,item):
    l=len(alist)
    if l==0:
        return False
    r=l/2
    if alist[r]==item:
        return True
    else:
        return