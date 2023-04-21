import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

arr=deque([i for i in range(1,n+1)])

while len(arr)!=1:
    print(arr.popleft(),end=' ')
    t=arr.popleft()
    arr.append(t)
print(arr[0])