# 가장 긴 증가하는 부분 수열

N=int(input())

arr=list(map(int,input().split()))

dp=[1 for _ in range(N)]


for i in range(N):
    for j in range(i):
        if arr[i]>arr[j]:
            dmax=dp[i]
            if dmax <(dp[j]+1):
                dmax=dp[j]+1
            dp[i]=dmax

print(max(dp))