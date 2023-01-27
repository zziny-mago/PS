# 제로
import sys
N = int(sys.stdin.readline())
stack=[]
negative=0
positive=0
for i in range(N):
    k=int(sys.stdin.readline())
    if(k==0):
        negative+=stack.pop()
    else:
        positive+=k
        stack.append(k)


print(positive-negative)