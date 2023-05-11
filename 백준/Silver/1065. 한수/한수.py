import sys
input=sys.stdin.readline

n=int(input())
cnt=0


if n<100:
        print(n)


else:
    for i in range(100,n+1):


        str_i=str(i)
        list_i=list(map(int,str_i))
        
        if ((list_i[0]+list_i[2])/2)==list_i[1]:
            cnt+=1
    print(cnt+99)