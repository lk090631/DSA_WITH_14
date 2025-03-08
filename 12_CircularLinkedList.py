class Node:
    data=None
    next=None
    def __init__(self,data):
        self.data=data


def Traversal(ptr):
    qtr=ptr
    print(qtr.data)
    qtr=qtr.next
    while qtr!=ptr:
        print(qtr.data)
        qtr=qtr.next


def insertionATB(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=newnode
        return newnode
    if ptr.next==ptr:
        newnode=Node(data)
        newnode.next=ptr
        ptr.next=newnode
        return newnode
    
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        qtr=qtr.next
        ftr=ftr.next

    newnode=Node(data)
    newnode.next=ftr
    qtr.next=newnode
    return newnode

def insertionATEND(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=newnode
        return newnode
    if ptr.next==ptr:
        newnode=Node(data)
        newnode.next=ptr
        ptr.next=newnode
        return ptr
    
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        qtr=qtr.next
        ftr=ftr.next

    newnode=Node(data)
    newnode.next=ftr
    qtr.next=newnode
    return ptr

def insertionATBT(ptr,data,index):
    if ptr==None:
        newnode=Node(data)
        newnode.next=newnode
        return newnode
    if ptr.next==ptr:
        newnode=Node(data)
        newnode.next=ptr
        ptr.next=newnode
        return newnode
    if index==0:
        return insertionATB(ptr,data)
    count=1
    copyptr=ptr
    copyptr=copyptr.next
    while copyptr!=ptr:
        count=count+1
        copyptr=copyptr.next
    
    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1 and ftr!=ptr:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        return ptr
    else:
        print("Index out of range")
        return ptr

def deletionATB(ptr):
    if ptr==None:
        return None
    if ptr.next==ptr:
        return None
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    
    qtr.next=ftr.next
    return qtr.next

def deletionATEND(ptr):
    if ptr==None:
        return None
    if ptr.next==ptr:
        return None
    qtr=ptr
    ftr=qtr.next
    while ftr.next!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    
    qtr.next=ftr.next
    return qtr.next

def deletionATBT(ptr,index):
    if ptr==None:
        return None
    if index==0:
        return deletionATB(ptr)
    
    count=1
    copyptr=ptr
    copyptr=copyptr.next
    while copyptr!=ptr:
        count=count+1
        copyptr=copyptr.next
    
    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1 and ftr!=ptr:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        
        qtr.next=ftr.next
        return ptr
    else:
        print("Index out of range")
        return ptr

a=None

a=insertionATEND(a,10)
a=insertionATEND(a,20)
a=insertionATEND(a,30)
a=insertionATEND(a,40)
a=insertionATEND(a,50)

a=insertionATBT(a,5,0)
a=deletionATB(a)
a=deletionATEND(a)
a=deletionATBT(a,2)
Traversal(a)