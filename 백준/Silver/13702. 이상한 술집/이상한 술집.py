import sys
input=sys.stdin.readline

n,k=map(int,input().split())
al_arr=[]

for i in range(n):
    pot=int(input())
    al_arr.append(pot)

st,en=1,max(al_arr)

while st<=en: 

    result=0
    mid=(st+en)//2
    for j in al_arr:
        result+=(j//mid)

    if result>=k:
        st=mid+1
    
    else:
        en=mid-1
print(en)