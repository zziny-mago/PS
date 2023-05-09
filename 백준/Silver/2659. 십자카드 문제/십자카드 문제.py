from collections import deque
find_ = deque(map(int,input().split()))
 
def find_clock_num(number):
    find_ = deque(number)
    clock_number = 10000
    for _ in range(4):
        now = find_[0]*1000+find_[1]*100+find_[2]*10+find_[3]*1
        if now < clock_number:
            clock_number = now
        find_.rotate(1)
    return clock_number
 
clock_number = find_clock_num(find_)
    
answer = 0
start = 1111
while start<=clock_number:
    if find_clock_num(list(map(int,list(str(start))))) == start:
        answer+=1
    start+=1
print(answer)
