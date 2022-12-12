#부녀회장이 될테야
import sys


def count(a,b):
        if (a==0):
            return b
        elif(b==1):
            return 1
        elif(arr[a][b]!=0):
            return arr[a][b]
        else:
            arr[a][b]=count(a-1,b)+count(a,b-1)
            return arr[a][b]

N=int(input())

for i in range(N):
    a=int(sys.stdin.readline())
    b=int(sys.stdin.readline())
    arr = [[0 for j in range(b+1)] for i in range(a+1)]
    result=count(a,b)
    print(result)




