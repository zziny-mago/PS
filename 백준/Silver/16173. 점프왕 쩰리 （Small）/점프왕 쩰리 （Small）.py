import sys
input=sys.stdin.readline


def dfs(i,j):

    if i<=-1 or i>=n or j<=-1 or j>=n or visited[i][j]==1:
        return
    if graph[i][j]==-1:
        visited[i][j]=1
        return
    visited[i][j]=1

    dfs(i+graph[i][j],j)
    dfs(i,j+graph[i][j])



n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

dfs(0,0)

if visited[-1][-1] == 1 :
    print('HaruHaru')
else :
    print('Hing')