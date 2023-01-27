# 스택 수열
import sys
N = int(sys.stdin.readline())
number=[i for i in range(1,N+1)]
y=[]

answer=[1]


for i in range(N):
    k=int(sys.stdin.readline())
    y.append(k)

q=0
n_q=q
print('+')
while(len(answer)!=0):
   
    if(y[n_q]!=answer[q]):
        q+=1
        answer.append(number[q])
        print('+')
    else:
        answer.pop()
        n_q+=1
        print('-')



