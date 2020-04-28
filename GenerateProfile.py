def GenerateProfile(motifmatrix):
    i3=0
    j3=0
    temp=""
    t=len(motifmatrix)
    k3=len(motifmatrix[0])
    probabilityA=[1/(t+4)]*k3
    probabilityC=[1/(t+4)]*k3
    probabilityG=[1/(t+4)]*k3
    probabilityT=[1/(t+4)]*k3
    for i3 in range(t):
        temp=motifmatrix[i3]
        for j3 in range(k3):
            if temp[j3]=="A":
                probabilityA[j3]=probabilityA[j3]+1/(t+4)
            elif temp[j3]=="C":
                probabilityC[j3]=probabilityC[j3]+1/(t+4)
            elif temp[j3]=="G":
                probabilityG[j3]=probabilityG[j3]+1/(t+4)
            elif temp[j3]=="T":
                probabilityT[j3]=probabilityT[j3]+1/(t+4)
    profile=[probabilityA,probabilityC,probabilityG,probabilityT]
    return profile



print(GenerateProfile(["CTCGGGGG","GGCGAGGT","ACCCAAAG","TTTCAGGT","CGTGCAAT"]))
