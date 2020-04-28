def ColoredEdges(genome):
    colorededges=[]
    for chromosome in genome:
        lengthchromosome=len(chromosome)
        for i in range(lengthchromosome):
            next=chromosome[(i+1)%lengthchromosome]
            if chromosome[i]>0:
                if next>0:
                    colorededges.append([2*chromosome[i],2*next-1])
                else:
                    colorededges.append([2*chromosome[i],-2*next])
            else:
                if next>0:
                    colorededges.append([-2*chromosome[i]-1,2*next-1])
                else:
                    colorededges.append([-2*chromosome[i]-1,-2*next])
    return colorededges

def FindCycleNum(graph):
    graph.sort(key=lambda x: x[0])
    grapheasy=[]
    for item in graph:
        grapheasy+=item
    count=0
    useddirectededges=[]
    newstart=1
    while grapheasy:
        flag=0
        for undirectededge in graph:
            if newstart in undirectededge:
                newstart=undirectededge[1-undirectededge.index(newstart)]
                index=graph.index(undirectededge)
                graph.remove(undirectededge)
                del grapheasy[2*index]
                del grapheasy[2*index]
                flag=1
        if flag==1 and grapheasy:
            pass
        else:
            count+=1
            if grapheasy:
                newstart=grapheasy[0]
    return count
    

def BreakDistance(genomelist):
    genome1=genomelist[0]
    genome2=genomelist[1]
    graph=ColoredEdges(genome1)+ColoredEdges(genome2)
    cyclenum=FindCycleNum(graph)
    blocknum=0
    for item in genome1:
        blocknum+=len(item)
    return blocknum-cyclenum


with open("data.txt","r") as f:
    temp=f.read().split("\n")
if "" in temp:
    temp.remove("")
genomelist=[]
for genome in temp:
    chromosome=[]
    chromosomeinstring=genome.replace(")","").split("(")
    chromosomeinstring.remove("")
    for item in chromosomeinstring:
        chromosome.append(list(map(int,item.split(" "))))
    genomelist.append(chromosome)
print(BreakDistance(genomelist))
    


    
