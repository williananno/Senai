#14/08/2024 Professor Gilberto - Aluno: Willian
#Exercicio 1
'''
numero1 = float (input ("Digite um número: "))
numero2 = float (input ("Digite outro número: "))

print("Resposta: ", numero1 ," +" ,numero2 ," = ",numero1+numero2)
'''

#Exercicio 2
validacao = "S"
while validacao.upper() == "S": # o Upper transforma a letra do usuario em letra Maiscula

    operacao = input("Digite 1- adição, 2- subtração, 3- muliplicação, 4- divisão: ")
    if not operacao.isdigit(): #Senão for um digito (número) ele volta
        continue    
    if int(operacao) >4 or int (operacao)<1:
        continue     #a função continue, retorna pro fluxograma inicio do programa "While"
    

    numero1 = float (input ("Digite um número: "))
    numero2 = float (input ("Digite outro número: "))

    if operacao == "1":
        resposta = numero1+numero2
        simbolo = "+"
    elif operacao == "2":
        resposta = numero1-numero2
        simbolo = "-"
    elif operacao == "3":
        resposta = numero1*numero2
        simbolo = "*"
    else:
        resposta = numero1/numero2
        simbolo = "/"

    print("Resposta: ", numero1 ,simbolo ,numero2 ," = ",resposta)
    validacao = input("Deseja fazer outra conta? <S/N>: ")
    contador = 0
    
    while validacao.upper()!="S" and validacao.upper() != "N":  #Verificação do Sim ou Não, para o usuario digitar a opção Correta
        validacao = input("Opção inválida. Digite S ou N:")
        contador = contador +1
        if contador == 3:
            print ("Você excedeu o limite de tentativas.")
            validacao = "N"