arr=[53,27,68,14,3,75,87]


for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
            
    t=arr[i]
    arr[i]=arr[min_index]
    arr[min_index]=t


print(arr)