distance_matrix=[
    [0,2,3,4],
    [2,0,3,6],
    [3,3,0,5],
    [4,6,5,0]
]

def dijkta_algorithm(distance_matrix,start):
    distance=[float("inf")]*len(distance_matrix)
    visited=[0]*len(distance_matrix)
    distance[start]=0

    for i in range(len(distance_matrix)):
        min_distance=float("inf")
        min_node=None
        for j in range(len(distance_matrix)):
            if not visited[j] and distance[j]<min_distance:
                min_distance=distance[j]
                min_node=j
        
        visited[min_node]=1

        for k in range(len(distance_matrix)):
            if distance_matrix[min_node][k]>0:
                newdistance=distance[min_node]+distance_matrix[min_node][k]
                if newdistance<distance[k]:
                    distance[k]=newdistance

    return distance



print(dijkta_algorithm(distance_matrix,0))