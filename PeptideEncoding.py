codon_table=dict()
with open("RNA_codon_table.txt","r") as f:
    for line in f:
        content=line.split()
        if len(content)==2:
            codon_table[content[0]]=content[1]
        else:
            codon_table[content[0]]="0"
    
def Transcription(gene):
    rna=""
    for base in gene:
        if base!="T":
            rna+=base
        else: 
            rna+="U"
    return rna

def ComplementDna(gene):
    complement=""
    complementary_rule={"A":"T","T":"A","C":"G","G":"C"}
    for base in gene:
        complement=complementary_rule[base]+complement
    return complement

def Translation(rna):
    peptide=""
    for i in range(0,len(rna),3):
        if i+3<=len(rna):
            if codon_table[rna[i:i+3]]!="0":
                peptide+=codon_table[rna[i:i+3]]      
    return peptide

def MatchPeptideDna(peptide,dna):
    matchedsequences=[]
    lengthpeptide=len(peptide)
    for i in range(len(dna)-3*lengthpeptide+1):
        temp=dna[i:i+3*lengthpeptide]
        if Translation(Transcription(temp))==peptide:
            matchedsequences.append(temp)
    return matchedsequences

with open("Bacillus_brevis.txt","r") as f:
    temp=f.read()
    dna=temp.replace("\n","")
    
print(dna)
peptide="VKLFPWFNQY"
answer=MatchPeptideDna(peptide,dna)
complementanswer=MatchPeptideDna(peptide,ComplementDna(dna))
answer+=list(map(ComplementDna,complementanswer))
print(len(answer))

with open("answer.txt","w") as f:
    f.write(str(len(answer)))
    for item in answer:
        f.write(item)
        f.write('\n')
    


