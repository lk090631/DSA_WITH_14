class queue:
    arr=[None]
    size=None
    front=None
    rear=None

def isEmpty(ptr):
    if ptr.front==ptr.rear:
        return True
    else:
        return False

def isFull(ptr):
    if ptr.rear==ptr.size-1:
        return True
    else:
        return False
    
def enqueue(ptr,data):
    if isFull(ptr):
        print("Queue Is Full Now")
        return ptr
    else:
        ptr.rear=ptr.rear+1
        ptr.arr[ptr.rear]=data
        return ptr
    
def dequeue(ptr):
    if isEmpty(ptr):
        print("Queue Is Empty")
        return ptr
    else:
        ptr.front=ptr.front+1
        temp=ptr.arr[ptr.front]
        ptr.arr[ptr.front]=None
        return temp
    

matrix=[
    [0,1,1,0,0],
    [1,0,0,1,1],
    [1,0,0,1,0],
    [0,1,1,0,1],
    [0,1,0,1,0]
]

head=queue()
head.rear=-1
head.front=-1
head.size=10
head.arr=head.arr*head.size

visited=[0,0,0,0,0]

position=3
print(position)
visited[position]=1

head=enqueue(head,3)

while not isEmpty(head):
    uv=dequeue(head)
    for i in range(len(visited)):
        if matrix[uv][i]==1 and visited[i]==0:
            print(i)
            visited[i]=1
            head=enqueue(head,i)