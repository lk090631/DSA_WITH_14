def BinarySearch(arr,sval):
    arr.sort()
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==sval:
            return True
        elif arr[mid]>sval:
            high=mid-1
        elif arr[mid]<sval:
            low=mid+1
            
    return False


x=[20,10,40,60,91,31,28,98,76]

if BinarySearch(x,0)==True:
    print("Element Found")
else:
    print("Element Not Found")    