def RightRotation(arr,n):
    for i in range(n):
        temp=arr.pop()
        arr.insert(0,temp)       
    return arr


x=[1,2,3,4,5,6]

def LeftRotation(arr,n):
    for i in range(n):
        temp=arr.pop(0)
        arr.append(temp)
        
    return arr

# print(RightRotation(x,9))

print(LeftRotation(x,2))