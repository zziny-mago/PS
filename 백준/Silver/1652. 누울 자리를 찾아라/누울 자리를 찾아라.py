import sys

n=int(input())
graph=[list(input()) for _ in range(n)]
horizon,vertical=0,0

for i in range(n):
    cnt=0
    for j in range(n):

        if graph[i][j]=='.':
            cnt+=1
        else:
            cnt=0

        if cnt==2:
            horizon+=1

for i in range(n):
    cnt=0
    for j in range(n):

        if graph[j][i]=='.':
            cnt+=1
        else:
            cnt=0

        if cnt==2:
            vertical+=1



print(horizon,vertical)