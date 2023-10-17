# 돈을 최대한 많이 지불해서 N개 카드구매
import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
dp=[0]*(n+2)


for i in range(1,len(arr)+1):
    for j in range(i):
        dp[i]=max(arr[j]+dp[i-j],dp[i])

print(dp[-1])