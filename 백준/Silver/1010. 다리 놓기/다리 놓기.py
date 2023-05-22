import sys
input=sys.stdin.readline

def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
        n=-1
    return result

n=int(input())
for i in range(n):
    w,e=map(int,input().split())

    print(int(factorial(e)/(factorial(e-w)*factorial(w))))