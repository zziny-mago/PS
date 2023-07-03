import sys
input=sys.stdin.readline

n,s=map(int,input().split())
arr=list(map(int,input().split()))
cnt=0

def check(idx,subSum):

    global cnt

    if idx<n:

        subSum+=arr[idx]

        if subSum==s:
            cnt+=1
            
        
        check(idx+1,subSum)

        check(idx+1,subSum-arr[idx])
    else:
        return

check(0,0)

print(cnt)