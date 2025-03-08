class queue:
    data=None
    next=None
    def __init__(self,data):
        self.data=data

def isEmpty(ptr):
    if ptr==None:
        return True
    else:
        return False
    
def isFull(ptr,data):
    newnode=queue(data)
    if newnode==None:
        return True
    else:
        return False

def enqueue(ptr,data):
    if isFull(ptr,data):
        print("Queue Is Full Now")
        return ptr
    else:
        if ptr==None:
            newnode=queue(data)
            newnode.next=ptr
            return newnode
        qtr=ptr
        ftr=qtr.next
        while ftr!=None:
            qtr=qtr.next
            ftr=ftr.next
    
        newnode=queue(data)
        newnode.next=None
        qtr.next=newnode
        return ptr
    
def dequeue(ptr):
    if isEmpty(ptr):
        print("Queue Is Empty Now")
        return ptr
    else:
        if ptr==None:
            return None
        ptr=ptr.next
        return ptr
        
    
def peek(ptr):
    if ptr==None:
        return None
    while ptr.next!=None:
        ptr=ptr.next
    print(ptr.data)



        
head=None
head=enqueue(head,10)
head=enqueue(head,20)
head=enqueue(head,30)


peek(head)

