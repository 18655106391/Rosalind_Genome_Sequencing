def Translation(rna,translation_dict):
    protein=""
    for i in range(0,len(rna),3):
        codon=rna[i:i+3]
        aminoacid=translation_dict[codon]
        if aminoacid!="0":
            protein+=aminoacid
    return protein




translation_dict=dict()
with open('RNA_codon_table.txt','r') as f:
    for line in f:
        temp=line.split()
        if len(temp)==2:
            translation_dict[temp[0]]=temp[1]
        else:
            translation_dict[temp[0]]='0'
with open('dataset.txt','r') as f:
    content=f.read().split()
    rna=content[0]
protein=Translation(rna,translation_dict)
print(protein)
with open('answer.txt','w') as f:
    f.write(protein)

