

def knapsack_memo(weight,profit,capicity,length,dp):

    if length==0 or capicity==0:
        return 0
    
    if dp[length][capicity]!=-1:
        return dp[length][capicity]
    

    if weight[length-1]>capicity:
        dp[length][capicity]=knapsack_memo(weight,profit,capicity,length-1,dp)

    else:
        include=profit[length-1]+knapsack_memo(weight,profit,capicity-weight[length-1],length-1,dp)
        exclude=knapsack_memo(weight,profit,capicity,length-1,dp)

        dp[length][capicity]=max(include,exclude)

    return dp[length][capicity]


def knapsack(weight,profit,capicity):
    length=len(weight)
    dp=[[-1 for i in range(capicity+1)] for j in range(length+1)]
    return knapsack_memo(weight,profit,capicity,length,dp)



weight=[2,3,4]
profit=[3,4,5]

capicity=7

print(knapsack(weight,profit,capicity))