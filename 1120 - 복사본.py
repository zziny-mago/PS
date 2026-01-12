
A,B=map(str,input().split())

j_list=[]
if (len(A))!=(len(B)):
    for j in range(len(A)):
        if (B.find(A[j])!=-1):
            idx=B.find(A[j])
            j_list.append(idx)

    j_set=set(j_list)  
    for l in j_set:
        s=B
        c=B[l]
        idx_list=[pos for pos, char in enumerate(s) if char == c]  
        print(f"idx_list:{idx_list}") 
        min=100
        print(f"l:{l}")
        for k in range(len(idx_list)):
            cnt=0
            for i in range(l,len(A)):
                if (idx_list[k]>=len(B)): break  
                if A[i]!=B[idx_list[k]]:
                    print(f"A:{A[i]} B:{B[idx_list[k]]}")
                    cnt+=1
                
                idx_list[k]+=1
            print("----------------------------")
            if cnt<min:
                min=cnt
        print(min+l) 
        print("++++++++++++++++++++++++++++")
else:
    cnt=0
    for i in range(len(A)):
        if(A[i]!=B[i]):
            cnt+=1
    print(cnt) 



