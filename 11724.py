from collections import deque 


def bfs(linked_list,start,visited):
    queue=deque([start])

    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end='')

        for i in linked_list[v]:
            print('u',end='')
            if visited[i]==False:
                queue.append(i)
                visited[i]=True


v,e=map(int,input().split())
graph=[]
linked_list=[[] for _ in range(v+1)]
for i in range(e):
    u=list(map(int,input().split()))
    graph.append(u)


for a,b in graph:
    linked_list[a].append(b)
    linked_list[b].append(a)

print(linked_list)

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * (v+1)
visited[0]=True
# 정의된 BFS 함수 호출
count=0
while False in visited:
    bfs(linked_list, 2, visited)
    count+1
print(count)