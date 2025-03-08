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



print(countNode(a))
# print(countHeight(a))
# preOrder(a)
# inOrder(a)
# postOrder(a)
