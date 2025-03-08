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


def isPerfectBinaryTree(ptr,totalheight,level=0):
    if ptr==None:
        return True
    elif ptr.left==None and ptr.right==None:
        return totalheight==level+1
    elif ptr.left==None or ptr.right==None:
        return False
    else:
        return isPerfectBinaryTree(ptr.left,totalheight,level+1) and isPerfectBinaryTree(ptr.right,totalheight,level+1)

a=Tree(10)
b=Tree(20)
c=Tree(30)
d=Tree(40)
e=Tree(50)
f=Tree(60)
# g=Tree(70)

a.left=b
a.right=c

b.left=d
b.right=e

c.left=f
# c.right=g



totalheight=countHeight(a)

flag=isPerfectBinaryTree(a,totalheight)
if flag==True:
    print("Yes It Is Perfect Binary Tree")
else:
    print("No It Is Not A Perfect Binary Tree")
