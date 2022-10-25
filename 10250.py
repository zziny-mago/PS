#ACM호텔
n=int(input())

for i in range(n):

    H,W,N=map(int,input().split())

    if (N%H==0):
        Y=(int((N-1)%H)+1)*100
        X=int(N/H)
        room=0
        room=Y+X
        print(room)
    else:
        Y=int(N%H)*100
        X=int(N/H)+1
        room=0
        room=Y+X
        print(room)
        

   
