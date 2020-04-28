def GenomePath(reads):
    k=len(reads[0])
    genome=reads[0]
    for i in range(1,len(reads)):
        temp=reads[i]
        genome=genome+temp[-1]
    return(genome)

with open('dataset_198_3.txt','r') as f:
    reads=f.read().split()
answer=GenomePath(reads)
print(answer)
f=open("answer.txt","w+")
f.write(answer)
f.close()

