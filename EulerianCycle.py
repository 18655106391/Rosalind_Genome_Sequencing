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
        print(route)
        print(edges_remained)
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
with open('dataset_203_2.txt','r') as f:
    for line in f:
        content=line.split()
        graph[int(content[0])]=list(map(int,content[2].split(',')))

answer=list(map(str,EulerianCycle(graph)))
print(answer)

with open('answer.txt','w') as f:
    for i in range(len(answer)-1):
        f.write(answer[i])
        f.write("->")
    f.write(answer[-1])






