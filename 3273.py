# 두 수의 합
# 두 포인터 문제는 정렬이 필수다!!!!!!
N=int(input())
arr=list(map(int,input().split()))
x=int(input())

arr=sorted(arr)
i=0
j=N-1
cnt=0
while i<j:
    if arr[i]+arr[j]==x:
        i+=1
        j-=1
        cnt+=1
    elif(arr[i]+arr[j]<x):
        i+=1
    else:
        j-=1
print(cnt)
    
