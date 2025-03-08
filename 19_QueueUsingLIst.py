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
        ptr.arr[ptr.front]=None
        return ptr
    
def peek(ptr):
    if ptr==None or ptr.rear==ptr.front:
        return ptr
    print(ptr.arr[ptr.rear])

head=queue()
head.size=10
head.front=-1
head.rear=-1
head.arr=head.arr*head.size


head=enqueue(head,10)
head=enqueue(head,20)
head=enqueue(head,30)
head=enqueue(head,40)
head=enqueue(head,50)
head=enqueue(head,60)
head=enqueue(head,70)
head=enqueue(head,80)
head=enqueue(head,90)
head=enqueue(head,100)

head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)

head=enqueue(head,110)
peek(head)