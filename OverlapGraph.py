def OverlapGraph(reads):
    overlap_graph=dict()
    for i in range(len(reads)):
        temp=reads[i]
        for j in range(len(reads)):
            if j!=i:
                target=reads[j]
                if temp[1:]==target[:-1]:
                    if temp in overlap_graph:
                        overlap_graph[temp].append(target)
                    else:
                        overlap_graph[temp]=[target]
    return overlap_graph
                    
with open('dataset_198_10.txt','r') as f:
    reads=f.read().split()
answer=OverlapGraph(reads)
f=open("answer.txt","w+")
for keys,values in answer.items():
    f.write(keys)
    f.write("->")
    for items in values:
        f.write(items)
    f.write("\n")
f.close()

