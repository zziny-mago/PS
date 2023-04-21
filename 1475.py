import sys
input=sys.stdin.readline

n=list(map(int,input().strip()))
check=[0 for _ in range(10)]

for j in n:
    if j==6 or j==9:
        check[6]+=1
    else: 
        check[j]+=1
if max(check) == check[6]:
    
    temp=check[6]
    check[6]=0

    if temp==max(check):
        print(max(check))

    elif check[6]%2==0: 
        check[6]=temp
        print(int(check[6]/2))
    else: 
        check[6]=temp
        print(int(check[6]/2)+1)

else: print(max(check))




