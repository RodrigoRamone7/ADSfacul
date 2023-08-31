frase = input ("Insira a frase a ser contada ")

qtdeLetras = 0

for letra in frase:
    qtdeLetras += 1

print("A frase possui " + str(qtdeLetras) + " letras.")