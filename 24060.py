# 알고리즘 수업 - 병합 정렬 1
count=0
n,cnt=map(int,input().split())
arr=list(map(int,input().split()))
def merge_sort(arr,first,last):

    if first>=last:
        return 
    
    
    merge_sort(arr,first,(first+last)//2)
    merge_sort(arr,((first+last)//2)+1,last)

    return sorting(arr,first,last)

def sorting(arr,first,last):
    global count
    mid=(first+last)//2
    i,j=first,mid+1
    temp=[]

    while i<=mid and j<=last:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1

        else: 
            temp.append(arr[j])
            j+=1

    while i<=mid:
        temp.append(arr[i])
        i+=1

    while j<=last:
        temp.append(arr[j])
        j+=1


    for k in range(first,last+1):
       arr[k]=temp[k-first]
       count+=1
       if count==cnt:
        print(arr[k])
    return arr

a=merge_sort(arr,0,n-1)
if count<cnt: print(-1)

