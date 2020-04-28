mass_table=dict()
with open('integer_mass_table.txt','r') as f:
    for line in f:
        content=line.split(" ")
        mass_table[content[0]]=int(content[1])

def AllMass(circularpeptide):
    masslist=[]
    n=len(circularpeptide)
    for subpeptidelength in range(1,n):
        for i in range(n):
            mass=0
            for j in range(subpeptidelength):
                mass+=mass_table[circularpeptide[(i+j)%n]]
            masslist.append(mass)
    mass=0
    for i in range(n):
        mass+=mass_table[circularpeptide[i]]
    masslist.append(mass)
    masslist.append(0)
    return masslist

circularpeptide="QLNCHGELGFFITQI"
masslist=AllMass(circularpeptide)
masslist.sort()
with open("answer.txt","w") as f:
    for item in masslist:
        f.write(str(item))
        f.write(" ")

