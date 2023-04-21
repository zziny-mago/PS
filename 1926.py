import sys
input=sys.stdin.readline

n,m=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*5 for _ in range(n)]
cnt=0
maxval=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(i,j):
    
    rs=1
    q=[(i,j)]

    while q:
        x,y=q.pop()

        for k in range(4):

            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and visited[nx][ny]==0:
                    rs+=1
                    visited[nx][ny]=1
                    q.append((nx,ny))

    return rs


for i in range(n):
    for j in range(m):

        if graph[i][j]==1 and visited[i][j]==0:

            fracture=bfs(i,j)
            cnt+=1
            maxval=max(maxval,fracture)

print(cnt)
print(maxval)
        
