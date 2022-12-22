# 과자 나눠주기
# https://nbalance97.tistory.com/225?category=904496

"""
child,snack=map(int,input().split())
L=list(map(int,input().split()))

if snack>=child:
    L=sorted(L,reverse=True)
    L=L[0:child]
    print(L[-1])
else:
    while len(L)!=child:
        L=sorted(L,reverse=True)
        if L[0]%2==0:
            p1,p2=L[0]/2
        else: 
            p1=L[0]//2
            p2=(L[0]//2)+1
        L.append(p1)
        L.append(p2)
        del L[0]
        L=sorted(L,reverse=True)
    print(L[-1])
"""

child,snack=map(int,input().split())
L=list(map(int,input().split()))
L=sorted(L)
mid=len(L)//2
sum=0

for i in L:
    sum+=(i//mid)
if sum>=child:
    mid+=1
    L=L[mi]
else:


