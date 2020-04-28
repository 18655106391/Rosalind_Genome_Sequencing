def DeBruijn(n,text):
    k=n-1
    adjacency_list=dict()
    for i in range(len(text)-k):
        temp=text[i:i+k]
        if temp in adjacency_list:
            adjacency_list[temp].append(text[i+1:i+k+1])
        else: 
            adjacency_list[temp]=[text[i+1:i+k+1]]               
    return adjacency_list

with open('dataset_199_6.txt','r') as f:
    content=f.read().split()
    n=int(content[0])
    text=content[1]

answer=DeBruijn(n,text)
f=open("answer.txt","w+")
for keys,values in answer.items():
    f.write(keys)
    f.write("->")
    for i in range(len(values)):
        f.write(values[i])
        if i<len(values)-1:
            f.write(",")
    f.write("\n")
f.close()
