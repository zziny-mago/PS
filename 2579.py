import sys
input=sys.stdin.readline

n=int(input())
stair=[0]
for i in range(n):
    op=int(input())
    stair.append(op)

arr=[0]*(n+1)

if n==1:
    arr[1]=stair[1]
    print(stair[1])
elif n==2:
    print(stair[2]+stair[1])

else:
    arr[1]=stair[1]
    arr[2]=stair[2]+stair[1]
    for k in range(3,n+1):

        
        arr[k]=max(arr[k-3]+stair[k-1]+stair[k],arr[k-2]+stair[k])

    print(arr[-1])
