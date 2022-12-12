#나이순 정렬

N=int(input())
id_dict={}

for i in range(N):
    id,name=input().split()
    id=int(id)
    if id not in id_dict:
        id_dict[id]=[]
    id_dict[id].append(name)

arr=sorted(list(id_dict.keys()))

for j in arr:
    if len(id_dict[j])>1:
        for k in range(len(id_dict[j])):
            print(j,id_dict[j][k])
        continue
    print(j,id_dict[j][0])
    