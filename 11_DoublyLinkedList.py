class Node:
    data=None
    prev=None
    next=None
    def __init__(self,data):
        self.data=data

def insertionATB(ptr,data):
    newnode=Node(data)
    newnode.next=None
    newnode.prev=None
    ptr.prev=newnode
    return newnode

def insertionATEND(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        return newnode
    qtr=ptr
    ftr=qtr.next
    while ftr!=None:
        qtr=qtr.next
        ftr=ftr.next
    newnode=Node(data)
    newnode.next=None
    newnode.prev=qtr
    qtr.next=newnode
    return ptr


def insertionATBT(ptr,data,index):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        return newnode
    if index==0:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        ptr.prev=newnode
        return newnode
    
    count=0
    copyptr=ptr
    while copyptr!=None:
        count=count+1
        copyptr=copyptr.next
    
    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        newnode=Node(data)
        newnode.next=ftr
        newnode.prev=qtr
        qtr.next=newnode
        ftr.prev=newnode
        return ptr

    else:
        print("Index out of range")
        return ptr


def insertionATSVB(ptr,data,sval):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        return newnode
    if ptr.data==sval:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        ptr.prev=newnode
        return newnode
    
    flag=False
    copyptr=ptr
    while copyptr!=None:
        if copyptr.data==sval:
            flag=True
            break
        copyptr=copyptr.next

    if flag==True:
        qtr=ptr
        ftr=qtr.next
        while ftr.data!=sval:
            qtr=qtr.next
            ftr=ftr.next
        newnode=Node(data)
        newnode.next=ftr
        newnode.prev=qtr
        qtr.next=newnode
        ftr.prev=newnode
        return ptr
    else:
        print("Search Value not found")
        return ptr

def insertionATSVA(ptr,data,sval):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        return newnode
    
    if ptr.data==sval and ptr.next==None:
        newnode=Node(data)
        newnode.next=None
        newnode.prev=ptr
        ptr.next=newnode
        return ptr

    if ptr.data==sval:
        qtr=ptr.next 
        newnode=Node(data)
        newnode.next=qtr
        newnode.prev=ptr
        ptr.next=newnode
        qtr.prev=newnode
        return ptr

    flag=False
    copyptr=ptr
    while copyptr!=None:
        if copyptr.data==sval:
            flag=True
            break
        copyptr=copyptr.next
    
    if flag==True:
        qtr=ptr
        ftr=qtr.next
        while qtr.data!=sval:
            qtr=qtr.next
            ftr=ftr.next

        if ftr==None:
            newnode=Node(data)
            newnode.next=None
            newnode.prev=qtr
            qtr.next=newnode
            return ptr
        newnode=Node(data)
        newnode.next=ftr
        newnode.prev=qtr
        qtr.next=newnode
        ftr.prev=newnode
        return ptr
    else:
        print("Search Value not found")
        return ptr
        

def deletionATB(ptr):
    if ptr==None:
        return None
    ptr=ptr.next
    ptr.prev=None
    return ptr


def deletionATEND(ptr):
    if ptr==None:
        return None
    if ptr.next==None:
        return None

    qtr=ptr
    ftr=qtr.next
    while ftr.next!=None:
        qtr=qtr.next
        ftr=ftr.next
    
    qtr.next=ftr.next
    return ptr
           


def Traversal(ptr):
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.next


def deletionATBT(ptr,index):
    if ptr==None:
        return None
    if index==0:
        ptr=ptr.next
        ptr.prev=None
        return ptr

    count=0
    copyptr=ptr
    while copyptr!=None:
        count=count+1
        copyptr=copyptr.next

    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        if ftr.next==None:
            qtr.next=None
            return ptr
        qtr.next=ftr.next
        ftr.next.prev=qtr
        return ptr
    else:
        print("Index out of range")
        return ptr


def deletionATSV(ptr,sval):
    if ptr==None:
        return None
    if ptr.data==sval and ptr.next==None:
        return None
    if ptr.data==sval:
        ptr=ptr.next
        ptr.prev=None
        return ptr
    
    flag=False
    copyptr=ptr
    while copyptr!=None:
        if copyptr.data==sval:
            flag=True
            break
        copyptr=copyptr.next

    if flag==True:
        qtr=ptr
        ftr=qtr.next
        while ftr.data!=sval:
            qtr=qtr.next
            ftr=ftr.next
        if ftr.next==None:
            qtr.next=None
            return ptr
        qtr.next=ftr.next
        ftr.next.prev=qtr
        return ptr
    else:
        print("Search Value not found")
        return ptr

def TraversalReverse(ptr):
    if ptr==None:
        return None
    while ptr.next!=None:
        ptr=ptr.next
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.prev




a=None


a=insertionATEND(a,10)
a=insertionATEND(a,20)
a=insertionATEND(a,30)
a=insertionATEND(a,40)
a=insertionATEND(a,50)

a=deletionATSV(a,10)
a=deletionATSV(a,30)
a=deletionATSV(a,50)

Traversal(a)