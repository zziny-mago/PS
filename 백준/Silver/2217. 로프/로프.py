import sys 
input=sys.stdin.readline

n=int(input())
rope=[]

for i in range(n):
    r=int(input())
    rope.append(r)

rope=sorted(rope)
result=[]
a=len(rope)
for j in rope:
    result.append(a*j)
    a=a-1
print(max(result))