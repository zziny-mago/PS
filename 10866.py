# 덱
import sys
read=sys.stdin.readline
N=int(input())

arr=[]
copy=[]
for i in range(N):
    Dt=read().split()
    
    if (Dt[0]=='push_back'):
        arr.append(int(Dt[1]))
    elif(Dt[0]=='push_front'):
        arr+=[int(Dt[1])]
    elif(Dt[0]=='front'):
        if(len(arr)==0): print(-1)
        print(arr[0])
    elif(Dt[0]=='back'):
        if(len(arr)==0): print(-1)
        print(arr[-1])
    elif(Dt[0]=='size'):
        print(len(arr))
    elif(Dt[0]=='empty'):  
        if(len(arr)==0): 
            print(1)
        else: 
            print(0)
    elif(Dt[0]=='pop_front'): 
        if(len(arr)==0): 
            print(-1)
            continue
        print(arr.pop(0))
    elif(Dt[0]=='pop_back'):   
        if(len(arr)==0): 
            print(-1)
            continue
        print(arr.pop(-1))           
