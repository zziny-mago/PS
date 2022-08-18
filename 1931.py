arr=[]
arr_gap=[]
N=int(input(""))
for i in range(N):
    A,B=map(int,input("").split())
    arr.append([A,B])
    gap=abs(A-B)
    arr_gap.append(gap)
