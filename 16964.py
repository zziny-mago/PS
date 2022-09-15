import sys
N=int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

order=list(map(int, sys.stdin.readline().split()))
check=[]
j=0

n=len(order)
check.append(order[0])
while j<n:
    k=0
    #for k in range(len(graph[order[j]])):
    while k <len(graph[order[j]]):
        #print(check)
        if graph[order[j]][k] in check:
            graph[order[j]].remove(graph[order[j]][k])
            k-=1
        k+=1
    
    if len(graph[order[j]])==0:
        order.remove(order[j])
        j-=1
        if j<0: 
            print(1)
            break
        continue

    if order[j+1] in graph[order[j]]: 
        graph[order[j]].remove(order[j+1])
        check.append(order[j+1])
        j+=1
    else:
        print(0)
        break
 





