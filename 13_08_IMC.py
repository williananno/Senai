#13/08/2024 Professor Gilberto - Aluno: Willian

while 1==1:
    peso = float(input ("Digite seu peso; para sair digite 0 : "))
    if peso == 0:
        break
    altura = float(input ("Digite sua altura: "))
    imc = peso / (altura*altura)
    if imc > 40:
        print("Obesidade grau 3")
    elif imc > 35:
        print ("Obsesidade grau 2")
    elif imc > 30:
        print ("Obsesidade grau 1")
    elif imc > 25:
        print ("Sobrepeso")
    elif imc > 18.5:
        print ("Peso Normal")
    else:
        print("Baixo Peso")