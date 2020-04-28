mass_table=dict()
with open('integer_mass_table.txt','r') as f:
    for line in f:
        content=line.split(" ")
        mass_table[content[0]]=int(content[1])

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

with open("dataset_4913_1.txt","r") as f:
    peptide=f.readline().split()[0]
    temp=f.readline().split()
spectrum=list(map(int,temp))

print(LinearScoring(peptide,spectrum))

