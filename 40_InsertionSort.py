arr=[53,27,68,14,3,75,87]


for i in range(1,len(arr)):
    val=arr[i]
    j=i-1
    while j>=0 and val<arr[j]:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=val


print(arr)