#12/08/2024 Professor Gilberto - Aluno: Willian 
"""
nome = input ("Digite o seu nome: ")
idade = input ("Digite a sua idade: ")
print ("Parabéns", nome, "você tem,", idade, "anos")
"""

""""
#Exercicio, monte um programa que peça a sua idade e crie um contador de 0 até sua idade
idade = int(input("Digite a sua idade: "))
for contador in range (idade+1):
    print (contador)
"""

''''
for letra in "Willian":
    print(letra)
'''

'''
nome = input("Digite um nome: ")
for letra in nome:
    print(letra)
    print("********************")
print(nome[5-1])
'''

''''
while 1==1:       # O simbolo de 2 iguais ==  significa igual
    nome = input("Digite um nome: ")
    if nome == "":
        break
    for letra in nome:
        print(letra)
    print("********************")
'''


sair = "N" 
while sair != "S":   # o simbolo !=  significa que é diferente
    nome = input("Digite um nome: ")
    for letra in nome:
        print(letra)
    print("********************")
    sair = input("Sair do programa (S/N): ").upper()  # o Upper transforma a letra do usuario em letra Maiscula
    



