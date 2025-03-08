class stack:
    arr=[None]
    top=None
    topEnd=None
    size=None

def isFull(ptr):
    if ptr.top+1==ptr.topEnd:
        return True
    else:
        return False

def isEmptyB(ptr):
    if ptr.top==-1:
        return True
    else:
        return False
    
def isEmptyEnd(ptr):
    if ptr.topEnd==ptr.size:
        return True
    else:
        return False
    

def pushB(ptr,data):
    if isFull(ptr):
        print("Stack Is Full Now")
        return ptr
    else:
        ptr.top=ptr.top+1
        ptr.arr[ptr.top]=data
        return ptr
    
def pushEND(ptr,data):
    if isFull(ptr):
        print("Stack is Full Now")
        return ptr
    else:
        ptr.topEnd=ptr.topEnd-1
        ptr.arr[ptr.topEnd]=data
        return ptr
    
def popB(ptr):
    if isEmptyB(ptr):
        print("Stack is Empty Now")
        return ptr
    else:
        ptr.arr[ptr.top]=None
        ptr.top=ptr.top-1
        return ptr
    
def popEnd(ptr):
    if isEmptyEnd(ptr):
        print("Stack Is Empty Now")
        return ptr
    else:
        ptr.arr[ptr.topEnd]=None
        ptr.topEnd=ptr.topEnd+1
        return ptr
    

def PeekB(ptr):
    if ptr.top==-1:
        print("Stack is Already Empty")
        return ptr
    print(ptr.arr[ptr.top])
    
def PeekEND(ptr):
    if ptr.topEnd==ptr.size:
        print("Stack is Already Empty")
        return ptr
    print(ptr.arr[ptr.topEnd])
    


head=stack()
head.size=10
head.top=-1
head.topEnd=head.size
head.arr=head.arr*head.size

head=pushB(head,10)
head=pushB(head,20)
head=pushB(head,30)
head=pushB(head,40)

head=pushEND(head,50)
head=pushEND(head,60)
head=pushEND(head,70)
head=pushEND(head,80)
head=pushEND(head,90)
head=pushEND(head,100)


PeekB(head)
PeekEND(head)


