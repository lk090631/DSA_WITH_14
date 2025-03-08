class stack:
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
    newnode=stack(data)
    if newnode==None:
        return True
    else:
        return False
    
def push(ptr,data):
    if isFull(ptr,data):
        print("Stack Is Full Now")
        return True
    else:
        if ptr==None:
            newnode=stack(data)
            newnode.next=ptr
            return newnode
        qtr=ptr
        ftr=qtr.next
        while ftr!=None:
            qtr=qtr.next
            ftr=ftr.next
        
        newnode=stack(data)
        newnode.next=None
        qtr.next=newnode
        return ptr
    
def pop(ptr):
    if isEmpty(ptr):
        print("Stack is Empty Now")
        return ptr
    else:
        if ptr==None:
            return None
        if ptr.next==None:
            ptr=ptr.next
            return ptr
        qtr=ptr
        ftr=qtr.next
        while ftr.next!=None:
            qtr=qtr.next
            ftr=ftr.next
        qtr.next=ftr.next
        return ptr

def peek(ptr):
    if ptr==None:
        print("Stack is Empty")
        return ptr
    else:
        qtr=ptr
        while qtr.next!=None:
            qtr=qtr.next
        print(qtr.data)   

head=None
head=push(head,10)
head=push(head,20)
head=push(head,30)
head=push(head,40)
head=push(head,50)

head=pop(head)
peek(head)




