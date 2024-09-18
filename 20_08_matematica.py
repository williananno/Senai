#20/08/2024 Professor Gilberto - Aluno: Willian
#Exercicio 1
'''
def adicao(numA, numB):     #Comando para criar uma função.
    return numA+numB

def subtracao(numA, numB):
    return numA-numB

def multriplicacao(numA, numB):
    return numA*numB

def divisao(numA, numB):
    return numA/numB

print("Escolha a opção: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = input("Digite a opção desejada: ")

if opcao == "1":
    numeroA = float(input("Digite o primeiro número: "))
    numeroB = float(input("Digite o segundo número: "))
    resultado = adicao(numeroA,numeroB)

elif opcao =="2":
    numeroA = float(input("Digite o primeiro número: "))
    numeroB = float(input("Digite o segundo número: "))
    resultado = subtracao(numeroA,numeroB)

elif opcao =="3":
    numeroA = float(input("Digite o primeiro número: "))
    numeroB = float(input("Digite o segundo número: "))
    resultado = multriplicacao(numeroA,numeroB)

elif opcao =="4":
    numeroA = float(input("Digite o primeiro número: "))
    numeroB = float(input("Digite o segundo número: "))
    resultado = divisao(numeroA,numeroB)

print(f"O resultado é {resultado:.2f}")

'''

#Exercicio 2 Criptografia.

palavra1 = input("Digite uma palavra para criptografar: ")
palavraCripto = ""
for letra in palavra1:
    numeroDaLetra = ord(letra)
    numeroDaLetra = numeroDaLetra + 1
    letraCodificada = chr(numeroDaLetra)
    palavraCripto = palavraCripto + letraCodificada
print(f"Palavra criptografada:{palavraCripto}")

palavra2 = input("Digite uma palavra para criptografar: ")
palavracripto = ""
for letra in palavra2:
    numeroDaLetra = ord(letra)
    numeroDaLetra = numeroDaLetra + 1
    letraCodificada = chr(numeroDaLetra)
    palavraCripto = palavraCripto + letraCodificada
print(f"Palavra criptografada:{palavraCripto}")

senha    = input("Digite uma senha   para criptografar: ")
palavracripto = ""
for letra in senha:
    numeroDaLetra = ord(letra)
    numeroDaLetra = numeroDaLetra + 1
    letraCodificada = chr(numeroDaLetra)
    palavraCripto = palavraCripto + letraCodificada
print(f"Palavra criptografada:{palavraCripto}")