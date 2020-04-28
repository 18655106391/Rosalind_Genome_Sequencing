def DeBruijnKmer(kmers):
    graph=dict()
    for item in kmers:
        temp=item[:-1]
        if temp in graph:
            graph[temp].append(item[1:])
        else:
            graph[temp]=[item[1:]]
    return graph

def GraphStructure(graph):
    nodelist=list(graph)
    length=len(nodelist)
    indegree=[0]*length*2
    outdegree=[0]*length*2
    for i in range(length):
        key=nodelist[i]
        outdegree[i]=len(graph[key])
        if outdegree[i]==1:
            temp=graph[key][0]
            if graph[key][0] not in nodelist:
                nodelist.append(temp)
            indegree[nodelist.index(temp)]+=1
        else:
            for item in graph[key]:
                if item not in nodelist:
                    nodelist.append(item)
                indegree[nodelist.index(item)]+=1
    del indegree[len(nodelist):]
    del outdegree[len(nodelist):]
    return [nodelist,indegree,outdegree]

def GraphStr2Num(graphstring,nodelist):
    graphnumber=dict()
    for key in graphstring:
        keyindex=nodelist.index(key)
        if keyindex not in graphnumber:
            graphnumber[keyindex]=[nodelist.index(graphstring[key][0])]
        if keyindex in graphnumber:
            for i in range(1,len(graphstring[key])):
                graphnumber[keyindex].append(nodelist.index(graphstring[key][i]))
    return graphnumber

def MaxNonBranching(graph):
    graphinformation=GraphStructure(graph)
    nodelist=graphinformation[0]
    indegree=graphinformation[1]
    outdegree=graphinformation[2]
    flag=[0]*len(nodelist)
    pathlist=list()    
    for i in range(len(nodelist)):
        if indegree[i]!=1 or outdegree[i]!=1:
            if outdegree[i]>0:
                node=nodelist[i]
                for nextnode in graph[node]:
                    path=[node]
                    flag[i]=1
                    path.append(nextnode)
                    index=nodelist.index(nextnode)
                    flag[index]=1
                    while indegree[index]==1 and outdegree[index]==1:
                        nextnode=graph[nextnode][0]
                        index=nodelist.index(nextnode)
                        flag[index]=1
                        path.append(nextnode)
                    pathlist.append(path)
    for i in range(len(flag)):
        if flag[i]==0 and indegree[i]==1 and outdegree[i]==1:
            node=nodelist[i]
            path=[node]
            flag[i]=1
            nextnode=graph[node][0]
            path.append(nextnode)
            index=nodelist.index(nextnode)
            flag[index]=1
            while indegree[index] and outdegree[index]==1 and graph[nextnode][0] not in path:
                nextnode=graph[nextnode][0]
                index=nodelist.index(nextnode)
                path.append(nextnode)
                flag[index]=1
            path.append(graph[nextnode][0])
            pathlist.append(path)
    return pathlist

def GenomePaths(pathlist,nodelist):
    contigs=list()
    for path in pathlist:
        contig=nodelist[path[0]]
        for i in range(1,len(path)):
            contig+=nodelist[path[i]][-1]
        contigs.append(contig)
    return contigs 



with open('dataset.txt','r') as f:
    reads=f.read().split()

graphstring=DeBruijnKmer(reads)
graphinformation=GraphStructure(graphstring)
nodelist=graphinformation[0]
indegree=graphinformation[1]
outdegree=graphinformation[2]
graphnumber=GraphStr2Num(graphstring,nodelist)
paths=MaxNonBranching(graphnumber)
contiglist=GenomePaths(paths,nodelist)

with open('answer.txt','w') as f:
    for item in contiglist:
        f.write(item)
        f.write(' ')

