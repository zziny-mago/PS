import sys
n,length = map(int,input().split())
input = sys.stdin.readline
d = {}
for _ in range(n) :
    voca = input().rstrip()
    if len(voca) < length :
        continue
    else :
        if voca in d.keys() :
            d[voca] += 1
        else :
            d[voca] = 1

result = sorted(d.items(),key= lambda x : (-x[1],-len(x[0]),x[0]))  
for i in result :
    print(i[0])