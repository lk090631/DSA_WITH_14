class Tree:
    data=None
    left=None
    right=None
    height=1
    def __init__(self,data):
        self.data=data


def inOrder(ptr):
    if ptr==None:
        return None
    inOrder(ptr.left)
    print(ptr.data) 
    inOrder(ptr.right)

def getHeight(ptr):
    if ptr==None:
        return 0
    return ptr.height

def getBalanceFactor(ptr):
    if ptr==None:
        return 0
    else:
        return getHeight(ptr.left)-getHeight(ptr.right)
    

def leftRotation(x):
    y=x.right
    t2=y.left
    y.left=x
    x.right=t2
    y.height=max(getHeight(y.left),getHeight(y.right))+1
    x.height=max(getHeight(x.left),getHeight(x.right))+1
    return y


def rightRotation(x):
    y=x.left
    t2=y.right
    y.right=x
    x.left=t2
    y.height=max(getHeight(y.left),getHeight(y.right))+1
    x.height=max(getHeight(x.left),getHeight(x.right))+1
    return y

def insertionInBST(ptr,val):
    if ptr==None:
        newnode=Tree(val)
        return newnode
    elif ptr.data>val:
        ptr.left= insertionInBST(ptr.left,val)
    elif ptr.data<val:
        ptr.right=insertionInBST(ptr.right,val)

    ptr.height=1+max(getHeight(ptr.left),getHeight(ptr.right))
    

    if getBalanceFactor(ptr)>1:
        if getBalanceFactor(ptr.left)==-1:
            ptr.left=leftRotation(ptr.left)
            return rightRotation(ptr)
        else:
            return rightRotation(ptr)
        
    if getBalanceFactor(ptr)<-1:
        if getBalanceFactor(ptr.right)==1:
            ptr.right=rightRotation(ptr.right)
            return leftRotation(ptr)
        else:
            return leftRotation(ptr)
    
    return ptr

def getBSTData(ptr,arr):
    if ptr==None:
        return None
    getBSTData(ptr.left,arr)
    arr.append(ptr.data)
    getBSTData(ptr.right,arr)

def searchingInBST(ptr,sval):
    if ptr==None:
        return False
    elif ptr.data==sval:
        return True
    elif ptr.data>sval:
        return searchingInBST(ptr.left,sval)
    elif ptr.data<sval:
        return searchingInBST(ptr.right,sval)


def successor(ptr):
    while ptr.left!=None:
        ptr=ptr.left
    return ptr

def deletionInBST(ptr,sval):
    if ptr==None:
        return None
    elif ptr.data>sval:
        ptr.left=deletionInBST(ptr.left,sval)
    elif ptr.data<sval:
        ptr.right=deletionInBST(ptr.right,sval)

    else:
        if ptr.left==None:
            temp=ptr.right
            ptr=None
            return temp
        
        if ptr.right==None:
            temp=ptr.left
            ptr==None
            return temp
        
        temp=successor(ptr.right)
        ptr.data=temp.data
        ptr.right=deletionInBST(ptr.right,temp.data)

        ptr.height=1+max(getHeight(ptr.left),getHeight(ptr.right))
    

        if getBalanceFactor(ptr)>1:
            if getBalanceFactor(ptr.left)==-1:
                ptr.left=leftRotation(ptr.left)
                return rightRotation(ptr)
            else:
                return rightRotation(ptr)
            
        if getBalanceFactor(ptr)<-1:
            if getBalanceFactor(ptr.right)==1:
                ptr.right=rightRotation(ptr.right)
                return leftRotation(ptr)
            else:
                return leftRotation(ptr)

    return ptr


def isBST(arr):
    newarr=[]
    for i in range(len(arr)):
        if arr[i] not in newarr:
            newarr.append(arr[i])

    if len(newarr)!=len(arr):
        print("Not It Is Not A BST")
        return arr

    flag=True

    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            flag=True
        else:
            flag=False
            break
    
    if flag==True:
        print("Yes It Is BST")
    else:
        print("No It Is Not A BST")


head=None
head=insertionInBST(head,10)
head=insertionInBST(head,5)
head=insertionInBST(head,4)
head=insertionInBST(head,14)
head=insertionInBST(head,25)
head=insertionInBST(head,21)
head=insertionInBST(head,33)
head=insertionInBST(head,15)

arr=[]

getBSTData(head,arr)

isBST(arr)
