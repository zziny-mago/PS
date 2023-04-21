n=int(input())
rope=[]
w=0
for i in range(n):
    r=int(input())
    rope.append(r)

for j in range(n):
    delta=n*min(rope)
    if w<delta: w=delta
    n-=1

print(w)