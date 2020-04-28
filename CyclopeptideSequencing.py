masslist=[]
with open('integer_mass_table.txt','r') as f:
    for line in f:
        content=line.split(" ")
        masslist.append(int(content[1]))
masslist=list(dict.fromkeys(masslist))

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
            

def Expand(peptide):
    expandedlist=[]
    for subsequent in masslist:
        expandedlist.append(peptide+[subsequent])
    return expandedlist

def CyclopeptideSequencing(spectrum):
    candidatepeptides=[[]]
    finalpeptides=[]
    i=0
    setspectrum=set(spectrum)
    while candidatepeptides:
        peptide=candidatepeptides[0]
        cyclospectrum=Cyclospectrum(peptide)
        linearspectrum=Linearspectrum(peptide)
        if set(linearspectrum).issubset(setspectrum):
            if set(cyclospectrum)==set(spectrum) and peptide not in finalpeptides:
                finalpeptides.append(peptide)
                candidatepeptides.remove(peptide)
            else:
                candidatepeptides=candidatepeptides+Expand(peptide)
                candidatepeptides.remove(peptide)
        else:
            candidatepeptides.remove(peptide)
    return finalpeptides

with open('dataset_100_6.txt','r') as f:
    content=f.read().split()
spectrum=list(map(int,content))

answer=CyclopeptideSequencing(spectrum)
print(answer)

with open('answer.txt','w') as f:
    for peptide in answer:
        for i in range(len(peptide)-1):
            f.write(str(peptide[i]))
            f.write('-')
        f.write(str(peptide[-1]))
        f.write(' ')

