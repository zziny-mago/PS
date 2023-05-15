import sys
input=sys.stdin.readline

n,m=map(int,input().split())
A=list(map(int,input().split()))

i=0
j=1
cnt=0
while j<=len(A):
    if sum(A[i:j])==m:
        i+=1
        j+=1
        cnt+=1
    elif(sum(A[i:j])<m):
        j+=1
    else:
        if i==j: 
            j+=1
            continue
        i+=1

print(cnt)