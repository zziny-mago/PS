N=int(input())
arr=list(map(int,input().split()))
sum=0
psudo=[]
for i in range(N):
    sum+=arr[N-1-i]
    psudo.append(sum)

result=0
for j in range(N-1):
    result+=arr[j]*psudo[N-2-j]
print(result)