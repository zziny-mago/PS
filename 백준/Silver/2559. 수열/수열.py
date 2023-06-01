import sys
input=sys.stdin.readline

n,k=map(int,input().split())
temp=list(map(int,input().split()))
temp.insert(0,0)
result=-1000

for i in range(1,len(temp)):
    if i==1:
        a=sum(temp[i:i+k])
    else:
        a=(a-temp[i-1]+temp[i+k-1])
    if result<a:
        result=a
    if i+k==(len(temp)):
        break
print(result)