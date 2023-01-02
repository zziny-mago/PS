# 주유소

N=int(input())
distance=list(map(int,input().split()))
oil=list(map(int,input().split()))
result=0

for i in range(N-1):
    if oil[i]>oil[i+1]:
        result+=(oil[i]*distance[i])
    else:
        result+=(oil[i]*distance[i])
        oil[i+1]=oil[i]

print(result)