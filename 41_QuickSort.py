arr=[72,28,18,19,96,57,2,5,79]


def QuickSort(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    
    pivot=arr[0]
    left_sub=[]
    right_sub=[]

    for i in range(1,len(arr)):
        if arr[i]>pivot:
            right_sub.append(arr[i])
        else:
            left_sub.append(arr[i])

    sorted_left=QuickSort(left_sub)
    sorted_right=QuickSort(right_sub)

    return [*sorted_left,pivot,*sorted_right]


print(QuickSort(arr))