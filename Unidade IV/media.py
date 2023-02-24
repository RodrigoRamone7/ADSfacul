dados = [[1,2,3],[4,5,6],[7,8,9]]
soma = 0
qtde = 0

for lista in dados:
    soma += sum(lista) # soma os valores dentro da lista
    qtde += len(lista) # conta a quantidade de valores na lista
print(soma)
print(qtde)
media = soma / qtde
print(media)