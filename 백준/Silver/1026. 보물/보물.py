import sys

input=sys.stdin.readline
result=0
n=int(input())

A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())),reverse=True)

for i,j in zip(A,B):
    result+=(i*j)
print(result)