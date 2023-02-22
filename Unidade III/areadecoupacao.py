print ("Algoritmo de percentual de ocupação de terreno")

#input de medidas da garagem
lGaragem = float (input("Insira a Largura da garagem: "))
pGaragem = float (input("Insira a Profundidade da garagem: "))

#Calculo de área da garagem
areaG = lGaragem * pGaragem
print("A área da garagem é de", areaG,"M²")

#input de medidas do terreno
lTerreno = float (input("Insira a Largura do terreno: "))
pTerreno = float (input("Insira a Profundidade do terreno: "))

#Calculo de área do terreno
areaT = lTerreno * pTerreno
print("A área do terreno é de", areaT,"M²")

#Calculo de percentual de ocupação
pOcupacao = (areaG / areaT) * 100

#input de localização do terreno
zona = input ("Informe a zona de localização: Sul=S, Norte=N, Leste=L e Oeste=O: ")

#Relatórios e mensagens
print ("O imovel está localizado na zona: ",zona)
print ("O percentual de ocupação do Terreno é de:", pOcupacao,"%")

#Sequencia de decisão
if zona == "N" and pOcupacao <= 25:
    print ("Projeto atende à norma de zoneamento do plano diretor")
    
elif zona == "L" or zona == "O" and pOcupacao <= 30:
    print ("Projeto atende à norma de zoneamento do plano diretor")
    
elif zona == "S" and pOcupacao <= 40:
    print ("Projeto atende à norma de zoneamento do plano diretor")
    
else:
    print ("REVISAR MEDIDAS. Projeto NÃO atende a norma de zoneamento do plano diretor")