print ("Serviço Militar")

sexo = str (input ("Informe se você é homem ou mulher: "))

if sexo == "homem":
    idade = float (input ("Informe a sua idade: "))
    if idade == 18:
        print ("Você está apto ao serviço militar")
    else:
        print ("Você não está apto ao serviço militar")
        
if sexo == "mulher":
    idade = float (input ("Informe sua idade: "))
    if idade >= 18 and idade < 36:
        print ("Você está apta ao serviço militar")
    else:
        print ("Você não está apta ao serviço militar")

