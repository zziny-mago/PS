# 최소 힙
#input=sys.stdin.readline

import sys
import heapq

import sys
import heapq

N = int(sys.stdin.readline())
data = []

for i in range(N):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(data, a)
    else:
        if not data:
            print(0)
        else:
            print(heapq.heappop(data))


#for q in range(len(result)):
    #print(result[q],end=" ")