import sys
input=sys.stdin.readline 
k,n=map(int,input().split())
arr=[]

for _ in range(k):
    line=int(input())
    arr.append(line)

st,en=1,max(arr)#최소/최대 절단 가능한 길이 



while st<=en: 

    t_result=0
    mid=(st+en)//2
    for i in arr:
        #print((i//mid))
        t_result+=(i//mid)

    if t_result>=n:
        st=mid+1
    else:
        en=mid-1
print(en)