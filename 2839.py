n=int(input())
count=n//5
L=n%5

if L%3==0: print(count+(L//3))
elif(n%3==0): print(n//3)
else: print(-1)



