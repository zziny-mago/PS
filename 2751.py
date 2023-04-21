import heapq
import sys
input = sys.stdin.readline
n=int(input())
arr=[]

for i in range(n):
    op=int((input()))
    arr.append(op)


def heap_sort(arr):

    h=[]
    result=[]
    for j in arr:
        heapq.heappush(h,j)

    for _ in range(len(arr)):
        result.append(heapq.heappop(h))
    return result
result=heap_sort(arr)
for l in result:
    print(l)
