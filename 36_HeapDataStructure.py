

def heapify(arr,length,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<length and arr[left]>arr[largest]:
        largest=left
    if right<length and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        t=arr[i]
        arr[i]=arr[largest]
        arr[largest]=t
        heapify(arr,length,largest)


def build_heap(arr):
    for i in range((len(arr)//2)-1,-1,-1):
        heapify(arr,len(arr),i)

def insert(arr,num):
    arr.append(num)
    currentIndex=len(arr)-1
    while currentIndex>0:
        parentIndex=(currentIndex-1)//2
        if arr[currentIndex]>arr[parentIndex]:
            t=arr[currentIndex]
            arr[currentIndex]=arr[parentIndex]
            arr[parentIndex]=t
            currentIndex=parentIndex
        else:
            break

def deletion(arr,num):

    i=0
    while i<len(arr):
        if arr[i]==num:
            break
        i=i+1

    t=arr[i]
    arr[i]=arr[len(arr)-1]
    arr[len(arr)-1]=t

    arr.pop()

    build_heap(arr)
    


arr=[4,15,36,18,79,66,7,23,98,19]

build_heap(arr)

print(arr)

deletion(arr,36)
deletion(arr,79)

print(arr)




         
