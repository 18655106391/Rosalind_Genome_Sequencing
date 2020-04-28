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
    startnode=0
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
        
graph=dict()
fakestart=0
fakeend=0
indegree=[0]*3000
outdegree=[0]*3000
with open('dataset_203_6.txt','r') as f:
    for line in f:
        content=line.split()
        startnode=int(content[0])
        endnodelist=list(map(int,content[2].split(',')))
        graph[startnode]=endnodelist
        outdegree[startnode]=outdegree[startnode]+len(endnodelist)
        for item in endnodelist:
            indegree[item]+=1
for i in range(3000):
    if indegree[i]>outdegree[i]:
        fakestart=i
    elif indegree[i]<outdegree[i]:
        fakeend=i
if fakestart in graph:
    graph[fakestart].append(fakeend)
else:
    graph[fakestart]=[fakeend]
        
temp=EulerianCycle(graph)
del temp[-1]
answer=[]
length=len(temp)
if temp[0]!=fakeend or temp[-1]!=fakestart:
    for i in range(1,length):
        if temp[i]==fakeend and temp[i-1]==fakestart:
            for j in range(length):
                answer.append(temp[(i+j)%length])             
with open('answer.txt','w') as f:
    for i in range(len(answer)-1):
        f.write(str(answer[i]))
        f.write("->")
    f.write(str(answer[-1]))






