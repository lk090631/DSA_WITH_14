x=[[10,20,30],[40,50,60],[70,80,90]]
y=[[1,1,1],[2,2,2],[3,3,3]]

z=[]
for i in range(len(x)):
    z.append([])
    for j in range(len(x[i])):
        z[i].append(0)
        for k in range(len(x[i])):
            z[i][j]+=x[i][k]*y[k][j]
            
print(z)