mass_table=dict()
with open('integer_mass_table.txt','r') as f:
    for line in f:
        content=line.split(" ")
        mass_table[content[0]]=int(content[1])
print(mass_table)

def Linearspectrum(peptide):
    spectrum=[]
    n=len(peptide)
    for subpeptidelength in range(1,n):
        for i in range(n-subpeptidelength+1):
            mass=0
            for j in range(subpeptidelength):
                mass+=mass_table[peptide[(i+j)]]
            spectrum.append(mass)
    spectrum.append(0)
    mass=0
    for i in range(len(peptide)):
        mass+=mass_table[peptide[i]]
    spectrum.append(mass)
    return spectrum

def LinearScoring(peptide,spectrum):
    theoreticalspectrum=Linearspectrum(peptide)
    score=0
    for item in spectrum:
        if item in theoreticalspectrum:
            score+=1
            theoreticalspectrum.remove(item)
    return score


def Trim(leaderboard,spectrum,n):
    scoretuplelist=[]
    for peptide in leaderboard:
        scoretuplelist.append((peptide,LinearScoring(peptide,spectrum)))
    scoretuplelist.sort(key=lambda tup: tup[1],reverse=True)
    trimmedleaderboard=[]
    for i in range(n):
        trimmedleaderboard.append(scoretuplelist[i][0])
    return trimmedleaderboard
   
with open("dataset_4913_3.txt","r") as f:
    content=f.read().split("\n")

leaderboard=content[0].split()
spectrum=list(map(int,content[1].split()))
n=int(content[2])
leaderboard=Trim(leaderboard,spectrum,n)
print(leaderboard)
with open("answer.txt","w") as f:
    for peptide in leaderboard:
        f.write(peptide)
        f.write(" ")
