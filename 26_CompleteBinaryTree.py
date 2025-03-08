class Tree:
    data=None
    left=None
    right=None
    def __init__(self,data):
        self.data=data

def preOrder(ptr):
    if ptr==None:
        return None
    print(ptr.data)
    preOrder(ptr.left)
    preOrder(ptr.right)

def inOrder(ptr):
    if ptr==None:
        return None
    inOrder(ptr.left)
    print(ptr.data) 
    inOrder(ptr.right)

def postOrder(ptr):
    if ptr==None:
        return None
    postOrder(ptr.left)
    postOrder(ptr.right) 
    print(ptr.data)

def countHeight(ptr,h=0):
    if ptr==None:
        return h
    return 1+max(countHeight(ptr.left),countHeight(ptr.right)) 

def countNode(ptr,count=0):
    if ptr==None:
        return count
    return 1+countNode(ptr.left)+countNode(ptr.right)


def isCompleteBinaryTree(ptr,totalNode,index):
    if ptr==None:
        return True
    elif index>=totalNode:
        return False
    else:
        return isCompleteBinaryTree(ptr.left,totalNode,2*index+1) and isCompleteBinaryTree(ptr.right,totalNode,2*index+2)

a=Tree(10)
b=Tree(20)
c=Tree(30)
d=Tree(40)
e=Tree(50)
f=Tree(60)
g=Tree(70)

a.left=b
a.right=c

b.left=d
b.right=e

c.left=f
c.right=g




totalNode=countNode(a)

flag=isCompleteBinaryTree(a,totalNode,0)
if flag==True:
    print("Yes It Is Complete Binary Tree")
else:
    print("No It Is Not Complete Binary Tree")