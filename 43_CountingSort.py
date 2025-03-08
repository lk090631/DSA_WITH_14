arr=[35,43,25,13,10,43,13,35,17,25,43,5,10,12]
maxNum=max(arr)

count=[0]*(maxNum+1)

newArr=[]

for i in range(len(arr)):
    count[arr[i]]=count[arr[i]]+1


for j in range(len(count)):
    if count[j]!=0:
        for k in  range(count[j]):
            newArr.append(j)


print(newArr)