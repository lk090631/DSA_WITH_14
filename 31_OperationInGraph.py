matrix=[
    [0,1,1,0,1,0],
    [1,0,0,1,0,1],
    [1,0,0,1,1,0],
    [0,1,1,0,0,1],
    [1,0,1,0,0,0],
    [0,1,0,1,0,0]
]


visited=[0,0,0,0,0,0]

def addVertices():
    visited.append(0)
    for i in range(len(matrix)):
        matrix[i].append(0)
    matrix.append([0]*(len(matrix)+1))

def addEdge(v1,v2):
    if v1<len(matrix) and v2<len(matrix):
        matrix[v1][v2]=1
        matrix[v2][v1]=1
    else:
        print("Vertex out Of the range")

def deleteEdge(v1,v2):
    if v1<len(matrix) and v2<len(matrix):
        matrix[v1][v2]=0
        matrix[v2][v1]=0
    else:
        print("Vertex out Of the range")

def deleteVertices():
    visited.pop()
    for i in range(len(matrix)):
        matrix[i].pop()
    matrix.pop()

def dfs(postion):
    print(postion)
    visited[postion]=1
    for i in range(len(visited)):
        if matrix[postion][i]==1 and visited[i]==0:
            dfs(i)




addVertices()
addVertices()


addEdge(2,6)
addEdge(3,6)
addEdge(0,3)
addEdge(4,7)
addEdge(2,7)
addEdge(7,6)

deleteEdge(2,7)
deleteEdge(4,7)
deleteEdge(7,6)

print(matrix)

deleteVertices()
print(matrix)
