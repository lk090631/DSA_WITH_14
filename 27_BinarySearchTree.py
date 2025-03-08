class Tree:
    data=None
    left=None
    right=None
    def __init__(self,data):
        self.data=data


def inOrder(ptr):
    if ptr==None:
        return None
    inOrder(ptr.left)
    print(ptr.data) 
    inOrder(ptr.right)


def insertionInBST(ptr,val):
    if ptr==None:
        newnode=Tree(val)
        return newnode
    elif ptr.data>val:
        ptr.left= insertionInBST(ptr.left,val)
    elif ptr.data<val:
        ptr.right=insertionInBST(ptr.right,val)
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
