#this runs the binarySearch function with the correct bounds
def search(list,int):

    return binarySearch(list,int,0,len(list)-1,0)




#int represents the element we are searching for
#count represents the number of times the method has run
def binarySearch(list,int,start,stop,count):
    count+=1
#This is a lame hotfix, but it checks to see if the method has run too many times, if it has, it shuts off
    if count==len(list)-1:
        if list[len(list)-1]==int:
            return len(list)
        else:
            return False
    mid=(stop-start)/2+start
    if list[mid]==int:
        return mid
    elif list[mid]>int:
            return binarySearch(list,int,start,mid,count)
    elif list[mid]<int:
            return binarySearch(list,int,mid,stop,count)

q=[17, 20, 26, 31, 44, 54, 55, 77, 93]
print search(q,3)