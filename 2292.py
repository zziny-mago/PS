#벌집
N=int(input())

sum=1
count=0
while 1:
    if N==1: 
        print(1)
        break
    else:
        count+=1
        sum=sum+(6*count)
        if sum>=N:
            print(count+1)
            break
