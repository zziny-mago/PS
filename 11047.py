# 동전 0

N,K=map(int,input().split())
coins=[]
for j in range(N):
    coin=int(input())
    coins.append(coin)

coins.reverse()
coin=0
count=0

while(1):
    if K-coins[coin]>=0:
        cnt=K//coins[coin]
        count+=cnt
        K=K-(cnt*coins[coin])
        if K==0:
            break
    coin+=1

print(count)


