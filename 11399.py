# ATM

N=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
sum=0
last_sum=0

for i in range(N):
    sum+=arr[i]
    last_sum+=sum

print(last_sum)