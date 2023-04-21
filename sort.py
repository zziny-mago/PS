
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot=arr[0]
    tail=arr[1:]

    left_arr=[i for i in tail if i<=pivot]
    right_arr=[i for i in tail if i>pivot]

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

print(quick_sort(array))

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else: break

print(array)