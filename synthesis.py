def DeBruijnKmer(kmers):
    graph=dict()
    for item in kmers:
        temp=item[:-1]
        if temp in graph:
            graph[temp].append(item[1:])
        else:
            graph[temp]=[item[1:]]
    return graph

def GenerateCycle(graph,start):
    unexplored_edges=graph
    route=[]
    lastnode=start
    nownode=unexplored_edges[lastnode][0]
    if len(unexplored_edges[lastnode])!=1:
        del unexplored_edges[lastnode][0]
    else:
        del unexplored_edges[lastnode]
    route.append(lastnode)
    route.append(nownode)
    while nownode in unexplored_edges:
        lastnode=nownode
        nownode=unexplored_edges[lastnode][0]
        route.append(nownode)
        if len(unexplored_edges[lastnode])==1:
            del unexplored_edges[lastnode]
        else:
            del unexplored_edges[lastnode][0]
    return[route,unexplored_edges]

def EulerianCycle(graph):
    edges_remained=graph
    startnode=list(edges_remained)[0]
    [route,edges_remained]=GenerateCycle(edges_remained,startnode)
    while edges_remained:
        del route[-1]
        length=len(route)
        temp=[]
        for i in range(length):
            if route[i] in edges_remained:
                for j in range(length):
                    temp.append(route[(i+j)%length])   
                route=temp
                break
        [newroute,edges_remained]=GenerateCycle(edges_remained,route[0])
        route.extend(newroute)
    return route

def GenomePath(reads):
    k=len(reads[0])
    genome=reads[0]
    for i in range(1,len(reads)):
        temp=reads[i]
        genome=genome+temp[-1]
    return(genome)

reads=[]
with open('dataset_203_7.txt','r') as f:
    content=f.read().split()
    k=content[0]
    for i in range(1,len(content)):
        reads.append(content[i])
graphstring=DeBruijnKmer(reads)
graphnumber=dict()
nodelist=list(graphstring)
nodenumber=len(nodelist)+1
indegree=[0]*nodenumber
outdegree=[0]*nodenumber
for key in graphstring:
    startnode=nodelist.index(key)
    for value in graphstring[key]:
        if value not in nodelist:
            nodelist.append(value)
        endnode=nodelist.index(value)
        if startnode in graphnumber:
            graphnumber[startnode].append(endnode)
        else:
            graphnumber[startnode]=[endnode]    
        outdegree[startnode]+=1
        indegree[endnode]+=1
for i in range(nodenumber):
    if outdegree[i]>indegree[i]:
        fakeend=i
    if outdegree[i]<indegree[i]:
        fakestart=i
if fakestart in graphnumber:
    graphnumber[fakestart].append(fakeend)
else:
    graphnumber[fakestart]=[fakeend]
temp=EulerianCycle(graphnumber)
del temp[-1]
answer=[]
length=len(temp)
if temp[0]!=fakeend or temp[-1]!=fakestart:
    for i in range(1,length):
        if temp[i]==fakeend and temp[i-1]==fakestart:
            for j in range(length):
                answer.append(temp[(i+j)%length])
kmersinorder=[]
for item in answer:
    kmersinorder.append(nodelist[item])
text=GenomePath(kmersinorder)
print(text)
with open('answer.txt','w') as f:
    f.write(text)















