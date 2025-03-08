arr=[0]*10

def hash_function(key):
    return key % 10

def insert(key,data):
    index=hash_function(key)

    i=1
    while arr[index]!=0:
        index=(index+1)%10
        i=i+1

    arr[index]=data


def delete(key,data):
    index=hash_function(key)
    i=1

    while arr[index]!=0:
        if arr[index]==data:
            arr[index]=0
            return
        index=(index+1)%10
        i=i+1
    
    print("Hash Key Not Found")

insert(55,"A")
insert(65,"B")
insert(63,"C")
insert(64,"D")
insert(75,"E")

print("Before deletion")
print(arr)


delete(55,"A")
delete(65,"B")

print("After Deletion")
print(arr)

