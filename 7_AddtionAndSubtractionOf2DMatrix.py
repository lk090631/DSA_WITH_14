x=[[10,20,30],[40,50,60],[70,80,90]]
y=[[100,120,130],[140,150,160],[170,180,190]]
z=[]
sub=[]
for i in range(len(x)):
    z.append([])
    for j in range(len(x[i])):
        z[i].append(x[i][j]+y[i][j])

for i in range(len(x)):
    sub.append([])
    for j in range(len(x[i])):
        sub[i].append(x[i][j]-y[i][j])    

    




