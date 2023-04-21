import sys 
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().strip())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

count=0
result=[]
def dfs(i,j):

    global count
    count+=1
    for k in range(4):
        ni=i+dx[k]
        nj=j+dy[k]
        if 0<=ni<n and 0<=nj<n:
            if visited[ni][nj]==False and graph[ni][nj]==1:
                visited[ni][nj]=True
                dfs(ni,nj)
    

for i in range(n):
    for j in range(n):
        if visited[i][j]==False and graph[i][j]==1:
            visited[i][j]=1
            count=0
            dfs(i,j)
            result.append(count)
result=sorted(result)
print(len(result))
for i in range(len(result)):
    print(result[i])
        
