def fibnacci(n,memo={}):
    if n==1 or n==0:
        return n
    
    if n in memo:
        return memo[n]
    else:
        memo[n]=fibnacci(n-1,memo) + fibnacci(n-2,memo)
        return memo[n]

for i in range(6):
    print(fibnacci(i))