class queue:
    arr=[None]
    size=None


def isEmpty(ptr):
    if len(ptr.arr)==0:
        return True
    else:
        return False
    
def isFull(ptr):
    if len(ptr.arr)==ptr.size:
        return True
    else:
        return False
    
def enqueueB(ptr,data):
    if isFull(ptr):
        print("Queue Is Full Now")
        return ptr
    else:
        ptr.arr.insert(0,data)
        return ptr
    
def enqueueEnd(ptr,data):
    if isFull(ptr):
        print("Queue is Full Now")
        return ptr
    else:
        ptr.arr.append(data)
        return ptr
    
def dequeueB(ptr):
    if isEmpty(ptr):
        print("Queue Is Already Empty")
        return ptr
    else:
        del ptr.arr[0]
        return ptr
    
def dequeueEND(ptr):
    if isEmpty(ptr):
        print("Queue Is Empty Now")
        return ptr
    else:
        ptr.arr.pop()
        return ptr
    

def peekB(ptr):
    if ptr==None or len(ptr.arr)==0:
        return None
    else:
        print(ptr.arr[0])

def peekEnd(ptr):
    if ptr==None or len(ptr.arr)==0:
        return None
    else:
        print(ptr.arr[len(ptr.arr)-1])



head=queue()
head.size=10
head.arr=[]

head=enqueueB(head,10)
head=enqueueB(head,20)
head=enqueueB(head,30)
head=dequeueEND(head)


peekB(head)
peekEnd(head)