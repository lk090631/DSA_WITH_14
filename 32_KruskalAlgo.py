cost_matrix=[
   [0,2,3,2],
   [2,0,0,5],
   [3,0,0,3],
   [2,5,3,0]
]


def get_edges(cost_matrix):
    edges=[]
    for i in range(len(cost_matrix)):
        for j in range(i+1,len(cost_matrix)):
            if cost_matrix[i][j]!=0:
                edges.append([i,j])

    edges.sort(key=lambda x:cost_matrix[x[0]][x[1]])
    return edges



def kruskal_Algorithm(cost_matrix,edges):
    mst=[]
    total_cost=0
    group=[0,1,2,3]
    
    for u,v in edges:
        if group[u]!=group[v]:
            mst.append([u,v])
            total_cost=total_cost+cost_matrix[u][v]
            old_group=group[v]
            new_group=group[u]

            for i in range(len(group)):
                if group[i]==old_group:
                    group[i]=new_group
    
    print("MST Tree Is ",mst)
    print("Total Cost is ",total_cost)


sorted_edges=get_edges(cost_matrix)

kruskal_Algorithm(cost_matrix,sorted_edges)