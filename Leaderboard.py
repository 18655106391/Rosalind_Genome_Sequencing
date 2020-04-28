
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
    i=n-1
    while i<len(leaderboard)-1 and leaderboard[i][2]==leaderboard[i+1][2]:
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

with open("Spectrum10.txt","r") as f:
    content=f.read().split()
    spectrum=list(map(int,content))

n=1000
leaderpeptides_scores=Leaderboard(spectrum,n)
peptidelist=[]
for item in leaderpeptides_scores:
    peptidelist.append(item[0])
print(leaderpeptides_scores)


with open("answer.txt","w") as f:
    for peptide in peptidelist:
        for i in range(len(peptide)-1): 
            f.write(str(peptide[i]))
            f.write("-")
        f.write(str(peptide[-1]))
        f.write(" ")


            
    
