class stack:
    arr=[None]
    size=None
    top=None

def isEmpty(ptr):
    if ptr.top==-1:
        return True
    else:
        return False
    
def isFull(ptr):
    if ptr.top==ptr.size-1:
        return True
    else:
        return False
    
def push(ptr,data):
    if isFull(ptr):
        print("Stack Is Full Now")
        return ptr
    else:
        ptr.top=ptr.top+1
        ptr.arr[ptr.top]=data
        return ptr

def pop(ptr):
    if isEmpty(ptr):
        print("Stack Already Empty")
        return ptr
    else:
        ptr.arr[ptr.top]=None
        ptr.top=ptr.top-1
        return ptr
    
def peek(ptr):
    if ptr.top==-1:
        print("Stack Is Empty")
        return ptr
    else:
        print(ptr.arr[ptr.top])

head=stack()
head.size=10
head.top=-1
head.arr=head.arr*10

head=push(head,10)
head=push(head,20)
head=push(head,30)
head=push(head,40)
head=push(head,50)
head=push(head,60)
head=push(head,70)
head=push(head,80)
head=push(head,90)
head=push(head,100)
head=pop(head)
head=pop(head)
peek(head)




