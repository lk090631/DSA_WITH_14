x=[101,200,220,330,10,20,80]

position=int(input("Enter The Postion b/w 0-length of list "))

for i in range(position,len(x)-1,1):
    x[i]=x[i+1]
    
x.pop()

print(x)