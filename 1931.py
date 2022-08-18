s=[]
f=[]
arr=[]
N=int(input(""))
for i in range(N):
    A,B=map(int,input("").split())
    arr.append([A,B])

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])





for x,y in arr:
    s.append(x)
    f.append(y)
A=[0]
j=0


for i in range(1,N):
    if(s[i]>=f[j]):
        A.append(i)
        j=i
print(len(A))

