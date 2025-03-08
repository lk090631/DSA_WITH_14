arr=[[] for i in range(10)]



def hash_function(key):
    return key % 10

def insert(key,data):
    index=hash_function(key)
    arr[index].append(data)

def display():
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j])

def delete(key,data):
    index=hash_function(key)
    
    for i in range(len(arr[index])):
        if arr[index][i]==data:
            del arr[index][i]
            return
    
    print("Data Not Exist")

insert(10,"Lokesh")
insert(21,"Rakesh")
insert(22,"Raju")
insert(32,"Sukesh1")
insert(42,"Sukesh2")
insert(11,"Sukesh3")
insert(81,"Sukesh4")

# print(arr)
delete(81,"Sukesh4")
delete(32,"Sukesh1")
display()