x=[20,10,40,60,91,31,28,96,76]

for i in range(len(x)//2):
    t=x[i]
    x[i]=x[len(x)-1-i]
    x[len(x)-1-i]=t
    
print(x)


