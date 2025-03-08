class Node:
    data=None
    next=None
    def __init__(self,data):
        self.data=data


def insertionATB(ptr,data):
    if ptr==None:
        header=Node(1)
        newnode=Node(data)
        newnode.next=None
        header.next=newnode
        return header
    
    qtr=ptr.next
    newnode=Node(data)
    newnode.next=qtr
    ptr.next=newnode
    ptr.data=ptr.data+1
    return ptr

def insertionATEND(ptr,data):
    if ptr==None:
        return insertionATB(ptr,data)
    qtr=ptr
    ftr=qtr.next
    while ftr!=None:
        qtr=qtr.next
        ftr=ftr.next

    newnode=Node(data)
    newnode.next=None
    qtr.next=newnode
    ptr.data=ptr.data+1
    return ptr

def insertionATBT(ptr,data,index):
    if ptr==None:
        return insertionATB(ptr,data)
    if index==0:
        return insertionATB(ptr,data)
    if ptr.data>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        ptr.data=ptr.data+1
        return ptr
    else:
        print("Index Of The Range")
        return ptr


def deletionATB(ptr):
    if ptr==None:
        return None
    qtr=ptr.next
    if qtr.next==None:
        return None
    
    ptr.next=qtr.next
    ptr.data=ptr.data-1
    return ptr

def deletionATEND(ptr):
    if ptr==None:
        return None
    qtr=ptr.next
    if qtr.next==None:
        return deletionATB(ptr)
    ftr=qtr.next
    while ftr.next!=None:
        qtr=qtr.next
        ftr=ftr.next
    
    qtr.next=ftr.next
    ptr.data=ptr.data-1
    return ptr

def deletionATBT(ptr,index):
    if ptr==None:
        return None
    if index==0:
        return deletionATB(ptr)
    if ptr.data>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        
        qtr.next=ftr.next
        ptr.data=ptr.data-1
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr


def Traversal(ptr):
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.next



a=None

a=insertionATEND(a,10)
a=insertionATEND(a,20)
a=insertionATEND(a,30)
a=insertionATEND(a,40)
a=insertionATBT(a,15,0)
a=insertionATBT(a,25,3)
a=insertionATBT(a,35,5)
a=deletionATB(a)
a=deletionATEND(a)
a=deletionATBT(a,0)
a=deletionATBT(a,2)
a=deletionATBT(a,2)
Traversal(a)

