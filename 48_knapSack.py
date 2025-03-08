def knapsack(weight,profit,capicity,index):
    if index==len(weight) or capicity==0:
        return 0
    
    if weight[index]>capicity:
        return knapsack(weight,profit,capicity,index+1)
    
    include=profit[index]+knapsack(weight,profit,capicity-weight[index],index+1)
    exculde=knapsack(weight,profit,capicity,index+1)

    return max(include,exculde)



weight=[2,3,4]
profit=[3,4,5]

capicity=7

print(knapsack(weight,profit,capicity,0))



