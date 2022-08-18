h_list=[]
epoch=int(input(""))
N=int(input(""))
h_list=list(map(int,input().split()))

h_list.sort()
first=[]
second=[]
cnt=0
for i in h_list:
  if cnt%2==0:
    first.append(i)
  else:
    second.append(i)
  cnt+=1
second=list(reversed(second))
h_list=first+second
print(h_list)
max1=h_list[0]-h_list[1]
for j in range(N):

  if j+1==N:
    result=h_list[j]-h_list[0]
  else:
    result=h_list[j]-h_list[j+1]
  if result<max1:
    print(j)
    max1=result
print(abs(max1))
