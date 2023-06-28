import sys
input=sys.stdin.readline

n=int(input())
arr=[]
dp=[0]*(n+1)

for i in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])

for j in range(n-1,-1,-1): # j는 날짜 인덱스 
    if arr[j][0]+j<=n: # 안넘어 괜찮아
        dp[j]=max(dp[j+1],arr[j][1]+dp[j+arr[j][0]])

    else:
        dp[j]=dp[j+1]

print(dp[0])