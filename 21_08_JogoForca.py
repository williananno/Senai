print("Seja bem vindo ao jogo da Forca!!")
print("Desenvolvido por: Willian Shigueo da Rocha Anno")
print("Copywrite 2024")
print("versão Beta")

palavraSecreta = input("Digite a palavra secreta: ").lower()

linha = ""

'''
for i in range(len(palavraSecreta)):   #len efetua a quantidade de caracteres/letras da palavra!
    linha = linha + "__ "
print(linha)
'''

linha = "  ".join(["__" for __ in palavraSecreta])
print(linha)

totalErros   = 0
totalAcertos = 0
letrasCertas = ""
letrasErradas = ""

while True:
    letra = input("Digite uma letra: ").lower()

    # Verifica se a entrada é válida (uma única letra)
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida. Por favor, digite apenas uma letra.")
        continue

    if letra in letrasCertas or letra in letrasErradas:
        print("Você já tentou essa letra: ")
        continue

    if letra in palavraSecreta:
        totalAcertos = totalAcertos + 1
        letrasCertas = letrasCertas + letra
        linha = " "
        for i in range(len(palavraSecreta)):
            if palavraSecreta[i] in letrasCertas:
                linha = linha + palavraSecreta[i] + " "
            else:
                linha = linha + "__ "
        print(linha)
        linha = ' '                            
    else:
        totalErros = totalErros + 1
        letrasErradas = letrasErradas + letra
        print("A resposta está ??? Erradaaaa!! ")
        
    print("\nPontuação")
    print(f"- Total de Erros  : {totalErros}")
    print(f"- Letras erradas: {letrasErradas}")
    print(f"- Total de Acertos: {totalAcertos}")
    print(f"- Letras certas: {letrasCertas}")
    print("\n")
    '''
    #FALHA
    if totalAcertos == len(palavraSecreta):
        print("Você ganhou!!!")
        break
    #FALHA
    '''
    if all(letra in letrasCertas for letra in palavraSecreta):
        print("Você ganhou!!!")
        break

    if totalErros == 6:
        print("Você perdeu!!!")
        break