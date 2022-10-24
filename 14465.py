N,K,B=map(int,input().split())
mal=[]
sign=[1]*(N+2)
sign[0]=0
sum_list=[]
origin_k=K
for n in range(B):
    a=int(input())
    mal.append(a)

for j in mal:
    sign[j]=0

for i in range(1,N-K+2):
    if i==1:
        sum_list.append(sum(sign[i:K+1]))
        tmp=sum(sign[i:K+1])
        print(tmp,111)
        print(sign[i:K+1])
        #print(K)
        K+=1
        continue

    sum_list.append(tmp+sign[K+1]-sign[i-1])
    tmp=tmp+sign[K+1]-sign[i-1]
    print(tmp,222)
    print(i,K)
    print(sign[i:K+1])
    #print(K)
    K+=1

print(sum_list)
print(origin_k-max(sum_list))