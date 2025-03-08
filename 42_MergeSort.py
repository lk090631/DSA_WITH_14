
arr=[72,28,18,19,96,57,2,5,79]

def merge_sort(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    
    mid=len(arr)//2
    left_sub=[arr[i] for i in range(mid)]
    right_sub=[arr[i] for i in range(mid,len(arr))]
    left_portion=merge_sort(left_sub)
    right_portion=merge_sort(right_sub)
    merge=[]
    i=0
    j=0
    while i<len(left_portion) and j<len(right_portion):
        if left_portion[i]<right_portion[j]:
            merge.append(left_portion[i])
            i=i+1
        else:
            merge.append(right_portion[j])
            j=j+1
    while i<len(left_portion):
        merge.append(left_portion[i])
        i=i+1
    
    while j<len(right_portion):
        merge.append(right_portion[j])
        j=j+1

    return merge




print(merge_sort(arr))