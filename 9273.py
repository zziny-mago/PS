N=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)

result_arr=[]
for i in range(1,N+1):
    result_arr.append(arr[i-1]-(N-i))
print(max(result_arr)+N+1)
