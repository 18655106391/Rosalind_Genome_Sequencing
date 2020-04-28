import numpy as np
import sys
sys.setrecursionlimit(10000)

def ScoreSingleAA(aa1,aa2):
    if aa1==aa2:
        return 1
    else:
        return 0

def BackTrack(peptide1,peptide2):
    scorematrix=np.zeros(shape=(lengthsequence1+1,lengthsequence2+1))
    backtrack=np.zeros(shape=(lengthsequence1+1,lengthsequence2+1))
    d=1
    h=2
    v=3
    for i in range(lengthsequence1+1):
        scorematrix[i][0]=0
    for j in range(lengthsequence2+1):
        scorematrix[0][j]=0
    for i in range(1,lengthsequence1+1):
        for j in range(1,lengthsequence2+1):
            possibility1=scorematrix[i-1][j-1]+ScoreSingleAA(sequence1[i-1],sequence2[j-1])
            possibility2=scorematrix[i-1][j]
            possibility3=scorematrix[i][j-1]
            scorematrix[i][j]=max(possibility1,possibility2,possibility3)
            if scorematrix[i][j]==possibility3:
                backtrack[i][j]=h
            elif scorematrix[i][j]==possibility2:
                backtrack[i][j]=v
            else:
                backtrack[i][j]=d
    print(scorematrix)
    return backtrack

def OutputLSC(backtrack,sequence1,i,j):
    d=1
    h=2
    v=3
    if i==0 or j==0:
        return ""
    if backtrack[i][j]==d:
        return OutputLSC(backtrack,sequence1,i-1,j-1)+sequence1[i-1]
    if backtrack[i][j]==v:
        return OutputLSC(backtrack,sequence1,i-1,j)
    if backtrack[i][j]==h:
        return OutputLSC(backtrack,sequence1,i,j-1)


with open("dataset_245_5.txt","r") as f:
    content=f.read().split()

sequence1=content[0]
sequence2=content[1]
lengthsequence1=len(sequence1)
lengthsequence2=len(sequence2)
backtrack=BackTrack(sequence1,sequence2)
print(OutputLSC(backtrack,sequence1,lengthsequence1,lengthsequence2))
