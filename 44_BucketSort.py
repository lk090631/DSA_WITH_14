arr=[0.78,0.12,0.68,0.65,0.94,0.15,0.82,0.84]

bucket=[[] for i in range(10)]
newaArr=[]

for i in range(len(arr)):
    index=int(arr[i]*10)
    bucket[index].append(arr[i])

for i in range(len(bucket)):
    bucket[i].sort()


for i in range(len(bucket)):
    for j in range(len(bucket[i])):
        newaArr.append(bucket[i][j])


print(newaArr)
