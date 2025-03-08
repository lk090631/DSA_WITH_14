x=[101,200,220,330,10,20,80]

postion=int(input("Enter The Index Between 0 - len of List"))
x.append(0)

value=int(input("Enter the value "))
for i in range(len(x)-1,postion,-1):
    x[i]=x[i-1]
    
x[postion]=value

print(x)