def GenerateGraph(readpairs):
    graph=dict()
    k=int(len(readpairs[0])/2)
    for read in readpairs:
        startnode=read[:(k-1)]+read[k:-1]
        endnode=read[1:k]+read[(k+1):]
        if startnode in graph:
            graph[startnode].append(endnode)
        else:
            graph[startnode]=[endnode]
    return graph

def GenerateCycle(graph,start):
    import random
    unexplored_edges=graph
    route=[]
    lastnode=start
    length=len(unexplored_edges[lastnode])
    if length!=1:
        randomnumber=random.randint(0,length-1)
        nownode=unexplored_edges[lastnode][randomnumber]
        del unexplored_edges[lastnode][randomnumber]
    else:
        nownode=unexplored_edges[lastnode][0]
        del unexplored_edges[lastnode]
    route.append(lastnode)
    route.append(nownode)
    while nownode in unexplored_edges:
        lastnode=nownode
        length=len(unexplored_edges[lastnode])
        if length!=1:
            randomnumber=random.randint(0,length-1)
            nownode=unexplored_edges[lastnode][randomnumber]
            del unexplored_edges[lastnode][randomnumber]
        else:
            nownode=unexplored_edges[lastnode][0]
            del unexplored_edges[lastnode]
        route.append(nownode)
    return[route,unexplored_edges]

def EulerianCycle(graph):
    import random
    edges_remained=graph
    keylist=list(edges_remained)
    if len(keylist)>1:
        startnode=keylist[random.randint(0,len(keylist)-1)]
    else:
        startnode=keylist[0]
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

def Assembly(readpairs,k,d):
    textprefix=readpairs[0][:(k-1)]
    textsuffix=readpairs[0][(k-1):]
    length=len(readpairs)
    for i in range(1,length):
        textprefix=textprefix+readpairs[i][k-2]
        textsuffix=textsuffix+readpairs[i][-1]
    text=textprefix+textsuffix[-(k+d):]
    return text



with open('dataset.txt','r') as f:
    content=f.read().split()
    k=int(content[0])
    d=int(content[1])
readpairs=[]
for i in range(2,len(content)):
    readpairs.append(content[i].replace("|",""))
graphstring=GenerateGraph(readpairs)
nodelist=list(graphstring)
nodenumber=len(nodelist)+1
indegree=[0]*nodenumber
outdegree=[0]*nodenumber
graphnumber=dict()
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

flag=0
while flag==0:
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
    flag=1
    for i in range(len(kmersinorder)-k-d):
        if kmersinorder[i][k-1:]!=kmersinorder[i+k+d][:k-1]:
            flag=0
text=Assembly(kmersinorder,k,d)
print(text)
with open('answer.txt','w') as f:
    f.write(text)




