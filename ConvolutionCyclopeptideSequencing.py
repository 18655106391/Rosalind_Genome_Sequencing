def SpectralConvolution(spectrum):
    convolutionresult=[]
    for i in range(len(spectrum)-1):
        for j in range(i,len(spectrum)):
            difference=spectrum[j]-spectrum[i]
            if difference:
                convolutionresult.append(difference)
    return convolutionresult

def FindAlphabet(spectrum,m):
    convolution=SpectralConvolution(spectrum)
    convolution.sort()
    tuplelist=[]
    value=convolution[0]
    count=1
    for i in range(1,len(convolution)):
        if convolution[i]==value:
            count+=1
        else:
            tuplelist.append((value,count))
            value=convolution[i]
            count=1
    tuplelist.sort(key=lambda tup: tup[1],reverse=True)
    alphabetlist=[]
    i=0
    while len(alphabetlist)<m: 
        temp=tuplelist[i][0]  
        if temp>=57 and temp<=200:
            alphabetlist.append(temp)
        i+=1
    i-=1
    while i<len(tuplelist)-1 and tuplelist[i][1]==tuplelist[i+1][1]:
        temp=tuplelist[i][0]
        if temp>=57 and temp<=200:
            alphabetlist.append(temp)
        i+=1
    return alphabetlist

def Cyclospectrum(circularpeptide):
    spectrum=[]
    n=len(circularpeptide)
    for subpeptidelength in range(1,n):
        for i in range(n):
            mass=0
            for j in range(subpeptidelength):
                mass+=circularpeptide[(i+j)%n]
            spectrum.append(mass)
    spectrum.append(sum(circularpeptide))
    spectrum.append(0)
    return spectrum

def Linearspectrum(peptide):
    spectrum=[]
    n=len(peptide)
    for subpeptidelength in range(1,n):
        for i in range(n-subpeptidelength+1):
            mass=0
            for j in range(subpeptidelength):
                mass+=peptide[(i+j)]
            spectrum.append(mass)
    spectrum.append(0)
    spectrum.append(sum(peptide))
    return spectrum

def Expand(peptidetuplelist,spectrum):
    expandedlist=[]
    for item in peptidetuplelist:
        for subsequent in masslist:
            newpeptide=item[0]+[subsequent]
            expandedlist.append((newpeptide,sum(newpeptide),LinearScoring(newpeptide,spectrum)))
    return expandedlist

def CycloScoring(peptide,spectrum):
    theoreticalspectrum=Cyclospectrum(peptide)
    score=0
    for item in spectrum:
        if item in theoreticalspectrum:
            score+=1
            theoreticalspectrum.remove(item)
    return score

def LinearScoring(peptide,spectrum):
    theoreticalspectrum=Linearspectrum(peptide)
    score=0
    for item in spectrum:
        if item in theoreticalspectrum:
            score+=1
            theoreticalspectrum.remove(item)
    return score

def Trim(leaderboard,spectrum,n):
    if len(leaderboard)<=n:
        return leaderboard
    leaderboard.sort(key=lambda tup: tup[2],reverse=True)  
    trimmedleaderboard=leaderboard[:n]
    i=n
    while i<len(leaderboard) and leaderboard[i-1][2]==leaderboard[i][2]:
        trimmedleaderboard.append(leaderboard[i+1])
        i+=1
    return trimmedleaderboard

def Leaderboard(spectrum,n):
    leaderboard=[([],0,1)]
    leaderpeptidestuplelist=[([],1)]
    maxspectrum=max(spectrum)
    while leaderboard:
        leaderboard=Expand(leaderboard,spectrum)
        j=0
        while leaderboard and j<len(leaderboard):
            peptide=leaderboard[j][0]
            peptidemass=leaderboard[j][1]
            if peptidemass==maxspectrum:
                cycloscorepeptide=CycloScoring(peptide,spectrum)
                if cycloscorepeptide>leaderpeptidestuplelist[0][1]:
                    leaderpeptidestuplelist=[()]
                    leaderpeptidestuplelist[0]=(peptide,cycloscorepeptide)
                    j=j+1
                elif cycloscorepeptide==leaderpeptidestuplelist[-1][1]:
                    leaderpeptidestuplelist.append((peptide,cycloscorepeptide))
                    j=j+1
                else:
                    j=j+1
            elif peptidemass>maxspectrum:
                del leaderboard[j]
            else:
                j=j+1
        leaderboard=Trim(leaderboard,spectrum,n)
    return leaderpeptidestuplelist


with open("dataset_104_7.txt","r") as f:
    temp=f.read().split()
m=int(temp[0])
n=int(temp[1])
spectrum=list(map(int,temp[2:]))
spectrum.sort()
masslist=FindAlphabet(spectrum,m)
masslist.sort()
print("The alphabet is:",masslist)
leaderpeptidestuplelist=Leaderboard(spectrum,n)
print(leaderpeptidestuplelist)





