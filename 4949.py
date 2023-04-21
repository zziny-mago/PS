a={'[':1,']':2,'(':4,')':5}
while 1:
    stack=[]
    text=input()
    if text=='.': break
    for i in text:
        if i=='[' or i=='(':
            stack.append(i)
        elif(i==']' or i==')'):
            if len(stack)==0: 
                stack.append(i)
                break
            if a[stack[-1]]-a[i]==-1:
                stack.pop()
            else:
                break
    if len(stack)==0: print('yes')
    else: print('no')
