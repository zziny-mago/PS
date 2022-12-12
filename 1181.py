#단어정렬

N=int(input())
word_dict={}
redundancy=[]
for i in range(N):
    word=input()
    if len(word) not in word_dict:
        word_dict[len(word)]=[]
    if word in word_dict[len(word)]:
        continue  
    word_dict[len(word)].append(word)



arr=list(word_dict.keys())
arr=sorted(arr)

for j in arr:
    if len(word_dict[j])>1:
        word_dict[j]=sorted(word_dict[j])
        for k in range(len(word_dict[j])):
            print(word_dict[j][k])
        continue
    print(word_dict[j][0])




