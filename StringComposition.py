def StringComposition(k,text):
    reads=[]
    for i in range(len(text)-k+1):
        reads.append(text[i:i+k])
    return reads


with open('dataset_197_3.txt','r') as f:
    content=f.read().split()
    k=int(content[0])
    text=content[1]
answer=StringComposition(k,text)
print(answer)
f=open("answer.txt","w+")
for i in range(len(answer)):
    f.write(answer[i])
    f.write('\n')
f.close()

