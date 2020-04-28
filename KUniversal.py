def GenerateKmers(n):
    if n==1:
        reads=['0','1']
        return reads
    else:
        reads=[]
        for item in GenerateKmers(n-1):
            reads.append("0"+item)
            reads.append("1"+item)                 
        return reads

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

n=8
reads=GenerateKmers(n)
graphstring=DeBruijnKmer(reads)
nodelist=list(graphstring)
graphnumber={}
for key in graphstring:
    startnode=nodelist.index(key)
    for value in graphstring[key]:
        endnode=nodelist.index(value)
        if startnode in graphnumber:
            graphnumber[startnode].append(endnode)
        else:
            graphnumber[startnode]=[endnode]    
temp=EulerianCycle(graphnumber)
kmersinorder=[]
for item in temp:
    kmersinorder.append(nodelist[item])
text=GenomePath(kmersinorder)
answer=text[:pow(2,n)]
print(answer)
with open('answer.txt','w') as f:
    f.write(answer)
