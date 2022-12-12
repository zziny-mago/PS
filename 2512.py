#예산
# 참고 코드 https://fre2-dom.tistory.com/m/230
N=int(input())
arr=list(map(int,input().split()))
budget=int(input())
low=1
high=max(arr)

while high>=low:
    mid=(high+low)//2
    res=0
    for i in range(N):
        if arr[i]>mid:
            res+=mid
        else:
            res+=arr[i]
    
    if res>budget:
        high=mid-1
    else:
        low=mid+1
print(high)