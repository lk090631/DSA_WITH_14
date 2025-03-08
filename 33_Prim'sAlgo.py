cost_matrix=[
    [0,3,0,7,8],
    [3,0,1,4,0],
    [0,1,0,2,0],
    [7,4,2,0,3],
    [8,0,0,3,0],
]


def prims_Algorithm(cost_matrix,totalvertex):
    visited=[0]*totalvertex
    visited[0]=1
    totalcost=0

    for i in range(totalvertex-1):
        min_weight=float("inf")
        x=0
        y=0
        for j in range(totalvertex):
            if visited[j]:
                for k in  range(totalvertex):
                    if visited[k]==0 and cost_matrix[j][k]!=0 and cost_matrix[j][k]<min_weight:
                        min_weight=cost_matrix[j][k]
                        x=j
                        y=k
        
        print("Edge",x,y)
        totalcost+=cost_matrix[x][y]
        visited[y]=1
    print("Total Cost of MinimumSpanning Tree Is ",totalcost)



prims_Algorithm(cost_matrix,5)