import numpy as np

with open("dataset_261_10.txt","r") as f:
    content=f.readline().split()
    n=int(content[0])
    m=int(content[1])
    downlist=[]
    rightlist=[]
    for i in range(n):
        downlist.append(list(map(int,f.readline().split())))
    f.readline()
    for i in range(n+1):
        rightlist.append(list(map(int,f.readline().split())))
down=np.array(downlist)
right=np.array(rightlist)

def ManhattanTourist(n,m,down,right):
    weightmatrix=np.zeros(shape=(n+1,m+1))
    weightmatrix[0][0]=0
    for i in range(1,n+1):
        weightmatrix[i][0]=weightmatrix[i-1][0]+down[i-1][0]
    for j in range(1,m+1):
        weightmatrix[0][j]=weightmatrix[0][j-1]+right[0][j-1]
    for i in range (1,n+1):
        for j in range(1,m+1):
            possibility1=weightmatrix[i-1][j]+down[i-1][j]
            possibility2=weightmatrix[i][j-1]+right[i][j-1]
            weightmatrix[i][j]=max(possibility1,possibility2)
    return weightmatrix

print(ManhattanTourist(n,m,down,right))
