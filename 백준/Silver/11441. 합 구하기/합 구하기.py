import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
s=[0]
part=0
result=[]
for q in range(n):
    ad=arr[q]
    part+=ad
    s.append(part)

for i in range(m):
    a,b=map(int,input().split()) 
    result.append(s[b]-s[a-1])

for k in range(m):
    print(result[k])