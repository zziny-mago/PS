import sys
input=sys.stdin.readline

n=int(input())
m=0
for i in range(n):
    klass=list(map(int,input().split()))
    k=klass[0]
    klass.pop(0)
    klass=sorted(klass,reverse=True)
    for j in range(len(klass)):
        if j==len(klass)-1:
            break
        m<(klass[j]-klass[j+1])
        m=klass[j]-klass[j+1]
    print()
    print('Class ',i+1)
    print("Max ",max(klass),"Min ",min(klass),"Largest gap ",m)
