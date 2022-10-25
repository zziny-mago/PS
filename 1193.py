# 분수찾기

N=int(input())
cnt=0
sum=0
while 1:
    if N<=sum: break
    sum+=(1*(cnt+1))
    cnt+=1


step=N-(sum-cnt)


if cnt%2==0: 
    print(str(step)+"/"+str(cnt-step+1))

else:
    print(str(cnt-step+1)+"/"+str(step))
