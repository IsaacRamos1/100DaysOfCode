arquivo = 'quemsoueu_transcricao.fasta'

f = open(arquivo, 'r')
lines = f.readlines()

relist = []

for line in lines:
    if line.find('>') == 0:
        continue
    
    relist.append(line)
    
dados = [0, 0, 0, 0]
i = 0

Lista = []
count = 1

def transcreve(num):
    RNA = ""
    i = 0
    teste = relist[num]
    while i < len(teste):
        if(teste[i] == "G"):
            RNA += "C"
            dados[0] += 1
        elif(teste[i] == "C"):
            RNA += "G"
            dados[1] += 1
        elif(teste[i] == "T"):
            RNA += "A"
            dados[2] += 1
        elif(teste[i] == "A"):
            RNA += "U"
            dados[3] += 1
        i += 1
    return RNA

for j in range(len(relist)):
    Lista.append(transcreve(j))

print(Lista)














