#Analise de Dados em Concurso Público CIASC 2009
#Dependências: Python 3
#Desenvolvimento: Gustavo Simas da Silva
#Data 22/08/2017

fh = open("homologainscricaociasc.txt")

count1, count2 = 0,0
nomes = dict()
sobrenomes = dict()

for line in fh:
    linha = line.split()
    if "Téc de Nível Superior II ­Analista de Sistemas" in line:
        count1 = count1 + 1
    if "Téc de Nível Superior III ­Analista de Sistemas" in line:
        count2 = count2 + 1
    if "Téc" in line:
        nomes[linha[0]] = nomes.get(linha[0],0) + 1
        for palavra in linha:
            try:
                float(palavra)
                index = linha.index(palavra)
                surname = linha[index-1]
                sobrenomes[surname] = sobrenomes.get(surname,0) + 1
            except:
                continue

print("\n\nCandidatos Concurso CIASC 2009")
print("Téc de Nível Superior II ­Analista de Sistemas:", count1)
print("Téc de Nível Superior III ­Analista de Sistemas:", count2)
print("Total de Analistas:",count1 + count2)

max_nome = max(nomes, key = lambda i: nomes[i])
min_nome = min(nomes, key = lambda i: nomes[i])
max_sobrenome = max(sobrenomes, key = lambda i: sobrenomes[i])
min_sobrenome = min(sobrenomes, key = lambda i: sobrenomes[i])

print("Nome mais comum:", max_nome)
print("Ocorrências:",nomes[max_nome])
print("Nome menos comum:", min_nome)
print("Sobrenome mais comum:", max_sobrenome)
print("Ocorrências:",sobrenomes[max_sobrenome])
print("Sobrenome menos comum:", min_sobrenome)
print("\n")