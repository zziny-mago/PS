import sys
input=sys.stdin.readline

n,k=map(int,input().split())

arr=[i for i in range(1,n+1)]

i=0
while arr:
    
    

    if (i+2>len(arr)):
        i=(2-(len(arr)-i))
        print(arr[i])
        arr.remove(arr[i])
        continue
    else:
        print(arr[i+2])
        arr.remove(arr[i+2])
        i+=2



            


