import sys
input=sys.stdin.readline

n=int(input())
cnt=0


for i in range(n):
    arr=[]
    text=input()
    
    for j in range(len(text)):
        if text[j] not in arr:
            arr.append(text[j])
        elif(text[j]==arr[j-1]):
            arr.append(text[j])
        else:
            cnt+=1
            break


print(n-cnt)

