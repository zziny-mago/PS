import sys
input=sys.stdin.readline

n=int(input())

dp=[0]*1000000
dp[1]=1
def dps(dp):

    if n==1:
        return 1

    dp[n]=dp[n-1]+1

    if dp[n]%3==0:
        dp[n]=min(dp[n],dp[n//3]+1)
    
    elif dp[n]%2==0:
        dp[n]=min(dp[n],dp[n//2]+1)
    
    return dp[n]

result=dps(dp)
print(result)