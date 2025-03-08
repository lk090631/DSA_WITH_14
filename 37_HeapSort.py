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


def Heap_Sort(arr):

    newArr=[]
    for i in range(len(arr)):
        t=arr[0]
        arr[0]=arr[len(arr)-1]
        arr[len(arr)-1]=t
        
        newArr.insert(0,arr.pop())
        build_heap(arr)

    print(newArr)


arr=[4,15,36,18,79,66,7,23,98,19]

build_heap(arr)

Heap_Sort(arr)