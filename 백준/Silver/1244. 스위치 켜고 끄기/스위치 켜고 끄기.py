import sys
input=sys.stdin.readline

sw_n=int(input())
sw=list(map(int,input().split()))
st_n=int(input())

for i in range(st_n):
    sex,number=map(int,input().split())

    if sex==1:

        for j in range(sw_n):
            if (j+1)%number==0:
                sw[j]=abs(sw[j]-1)

    else:
        number-=1
        sw[number]=abs(sw[number]-1)
        for k in range(1,sw_n//2):

            if (0<=(number-k)<=(sw_n-1)) and (0<=(number+k)<=(sw_n-1)):

                if sw[number-k]==sw[number+k]:
                    sw[number-k]=abs(sw[number-k]-1)
                    sw[number+k]=abs(sw[number+k]-1)
                else:
                    break

for q in range(sw_n):
    if q!=0 and q%20==0: print()
    print(sw[q],end=" ")