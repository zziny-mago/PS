import sys
input=sys.stdin.readline
n,l=map(int,input().split())
arr=list(map(int,input().split()))
arr=sorted(arr)
cnt=0

repair=0

for i in arr:
    
    if i>repair:
        cnt+=1
        repair=i
        repair=repair+l-1
    
print(cnt)
