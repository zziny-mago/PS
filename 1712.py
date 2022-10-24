#손익분기점 
A,B,C=map(int,input().split())
D=C-B
if B>=C:
    print(-1)
else:
    result=int(A/D)
    print(result+1)