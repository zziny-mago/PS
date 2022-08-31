N=int(input())
arr=list(map(int,input().split()))
arr.sort()
cnt=0
for i in range(N):
    l,r=0,N-2
    tmp=arr[0:i]+arr[i+1:N]
    sum=tmp[l]+tmp[r]

    while l<r:
        sum=tmp[l]+tmp[r]
        if sum==arr[i]:
            cnt+=1
            break
        
        if sum<arr[i]:
            l+=1
        else:
            r-=1
print(cnt)
    