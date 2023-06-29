import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
dp=[1]*n

for i in range(1,n): # 2번 병사번호부터 뒤에 본다
    temp=0
    for j in range(i):
        j+=1
        if arr[i-j]>arr[i]: # 오름차순이 될 수 있는 요소가 있는경우

            if temp<dp[i-j]: # 뒤에서 제일 큰 병사의 dp값
                temp=dp[i-j]
            dp[i]=temp+1

        else:
            continue
print(n-max(dp))