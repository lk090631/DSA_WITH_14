class Node:
    data=None
    next=None
    def __init__(self,data):
        self.data=data

def Traversal(ptr):
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.next

def insertionATB(ptr,data):
    newnode=Node(data)
    newnode.next=ptr
    return newnode

def insertionATEND(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        return newnode

    qtr=ptr
    ftr=qtr.next
    while ftr!=None:
        qtr=qtr.next
        ftr=ftr.next
    
    newnode=Node(data)
    newnode.next=None
    qtr.next=newnode
    return ptr

def insertionATBT(ptr,data,index):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        return newnode
    if index==0:
        newnode=Node(data)
        newnode.next=ptr
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
        qtr.next=newnode
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr


def insertionATSVB(ptr,data,sval):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        return newnode
    if ptr.data==sval:
        newnode=Node(data)
        newnode.next=ptr
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
        qtr.next=newnode
        return ptr
    else:
        print("Search Value Not Found")
        return ptr


def insertionATSVA(ptr,data,sval):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
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
        while qtr.data!=sval:
            qtr=qtr.next
            ftr=ftr.next
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        return ptr
    else:
        print("Search Value Not Found")
        return ptr
    
    

def deletionATB(ptr):
    if ptr==None:
        return None
    
    ptr=ptr.next
    return ptr


def deletionATEND(ptr):
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

def deletionATBT(ptr,index):
    if ptr==None:
        return None
    if index==0:
        ptr=ptr.next
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
        qtr.next=ftr.next
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr
    
def deletionATSV(ptr,sval):
    if ptr==None:
        return None
    if ptr.data==sval:
        ptr=ptr.next
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
        qtr.next=ftr.next
        return ptr
    else:
        print("Search Value Does Not Exist")
        return ptr

def duplicates(ptr):
    arr=[]
    while ptr!=None:
        arr.append(ptr.data)
        ptr=ptr.next
    
    newarr=[]
    for i in arr:
        if i not in newarr:
            newarr.append(i)
    newptr=None

    for i in newarr:
        newptr=insertionATEND(newptr,i)

    return newptr





def SortedLinkedList(ptr):
    arr=[]
    while ptr!=None:
        arr.append(ptr.data)
        ptr=ptr.next
    arr.sort()
    newptr=None
    for i in range(len(arr)):
        newptr=insertionATEND(newptr,arr[i])

    return newptr
def mergeLists(head1, head2):
    qtr=head1
    while qtr.next!=None:
        qtr=qtr.next
    qtr.next=head2
    arr=[]
    while head1!=None:
        arr.append(head1.data)
        head1=head1.next
    arr.sort()
    ptr=None
    for i in range(len(arr)):
        ptr=insertionATEND(ptr,arr[i])
    return ptr        

a=None

a=insertionATEND(a,100)
a=insertionATEND(a,100)
a=insertionATEND(a,300)
a=insertionATEND(a,300)
a=insertionATEND(a,300)
a=insertionATEND(a,300)
a=insertionATEND(a,140)
a=insertionATEND(a,140)
a=insertionATEND(a,140)
a=insertionATEND(a,10)



# a=mergeLists(a,b)

a=duplicates(a)
Traversal(a)

