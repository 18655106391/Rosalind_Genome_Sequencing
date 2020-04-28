def DeBruijnKmer(kmers):
    graph=dict()
    for item in kmers:
        temp=item[:-1]
        if temp in graph:
            graph[temp].append(item[1:])
        else:
            graph[temp]=[item[1:]]
    return graph
with open('dataset_200_8.txt','r') as f:
    kmers=f.read().split()

answer=DeBruijnKmer(kmers)
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
