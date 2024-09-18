"""
Crie um programa que simule um jogo de adivinhação. Atribua um valor para uma variável. 
O usuário terá que adivinhar qual é esse número, recebendo dicas se o palpite é maior ou menor
que o número correto. O jogo termina quando o usuário adivinhar corretamente. Comece assim:
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando entre 1 e 20.")
print("Digite 'sair' para encerrar o jogo a qualquer momento.")
numero = 15 # troque esse numero as vezes
while True:
palpite = input ("Qual o seu palpite?: ")
"""
import random

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando entre 1 e 20.")
print("Digite 'sair' para encerrar o jogo a qualquer momento.")
numero = random.randint(1,20)

while True:
    
    palpite_str = input ("Qual o seu palpite?: ") #Essa variável continua como String
    

    if palpite_str == "sair":
        break    
    
    palpite = int(palpite_str)                    #Essa variável converte string para int.
    
    if palpite == numero:
        print("Parabens você acertou!")

    elif numero <= palpite:
        print("O número que informou é maior, o valor correto é abaixo que você informou")

    elif numero >= palpite:
        print("O número que informou é menor, o valor correto é maior que você informou")

    

    