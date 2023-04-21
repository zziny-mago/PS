import sys 
input=sys.stdin.readline

n=int(input())
arr=[]
l_arr=[]
result=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))

arr=sorted(arr,reverse=True)

for j in range(n):
    l_arr.append(list(arr[j]))


for k in range(n):
    cnt=0
    for q in range(n):
        if l_arr[k][1]< l_arr[q][1]: 
            cnt+=1
            result.append(cnt)




print(l_arr)