N=int(input())
indice=list(map(int,input().split()))
indice.sort()
right=0
left=0
if N%2==1:
    print(indice[int((N/2))])
else:
    avg=sum(indice)/len(indice)
    for i in range(N):
        r=indice[int(((N/2)))]
        l=indice[int((N/2)-1)]
        right+=abs(indice[i]-r)
        left+=abs(indice[i]-l)
    if right>=left:
        print(l)
    else: 
        print(r)