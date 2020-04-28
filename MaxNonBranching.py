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



graph=dict()
with open('dataset.txt','r') as f:
    for line in f:
        content=line.split()
        graph[int(content[0])]=list(map(int,content[2].split(',')))
paths=MaxNonBranching(graph)

with open('answer.txt','w') as f:
    for path in (paths):
        for i in range(len(path)-1):
            f.write(str(path[i]))
            f.write("->")
        f.write(str(path[-1]))
        f.write('\n')


