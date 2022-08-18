N = int(input())
switch =[-999]+list(map(int, input().split()))
students = int(input())

def change_N(n):
    if n==0:
        return 1
    else:
        return 0

for i in range(students):

    sex,switch_N=map(int,input().split())

    if sex==1:
        for i in range(switch_N,N+1):
            if i%switch_N==0:
                switch[i]=change_N(switch[i])

    elif sex==2:
        switch[switch_N]=change_N(switch_N)
        for i in range(1,N+1):
            if (switch_N-i>=1) and (switch_N+i<=N):
                if switch[switch_N-i]==switch[switch_N+i]:
                    switch[switch_N-i]=change_N(switch[switch_N-i])
                    switch[switch_N+i]=change_N(switch[switch_N+i])
                else:
                    break
            else:
                break


for i in range(1,N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()

