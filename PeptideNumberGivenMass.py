condition=[]
count=[]

def Count(end,totalmass):
    if totalmass==0:
        return 1
    if totalmass<0:
        return 0
    if [end,totalmass] in condition:
        return count[condition.index([end,totalmass])]
    else:
        value=0
        for i in range(len(masslist)):
            value+=Count(masslist[i],totalmass-end)
        condition.append([end,totalmass])
        count.append(value)
        return value
            
masslist=[]
with open("integer_mass_table.txt","r") as f:
    for line in f:
        content=line.split()
        masslist.append(int(content[1]))
masslist=list(dict.fromkeys(masslist))
print(masslist)
totalmass=1024
answer=0
for i in range(len(masslist)):
    answer+=Count(masslist[i],totalmass)

print(answer)


