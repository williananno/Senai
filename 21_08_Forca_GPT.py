# Solicita a palavra secreta ao usuário
palavraSecreta = input("Digite a palavra secreta: ")

# Cria uma linha de riscos correspondente ao comprimento da palavra secreta
linha = "  ".join(["__" for _ in palavraSecreta])
print(linha)

# Inicializa as variáveis de pontuação e armazenamento de letras
totalErros = 0
totalAcertos = 0
letrasCertas = ""
letrasErradas = ""

# Loop principal do jogo
while True:
    # Solicita uma letra ao usuário
    letra = input("Digite uma letra: ")

    # Verifica se a letra está na palavra secreta
    if letra in palavraSecreta:
        totalAcertos += 1
        letrasCertas += letra
        # Atualiza a linha de riscos com as letras acertadas
        linha = ""
        for i in range(len(palavraSecreta)):
            if palavraSecreta[i] in letrasCertas:
                linha += palavraSecreta[i] + " "
            else:
                linha += "__ "
        print(linha)
    else:
        totalErros += 1
        letrasErradas += letra + " "
        print("A resposta está errada!")

    # Exibe a pontuação e o estado atual do jogo
    print("\nPontuação")
    print(f"- Total de Erros  : {totalErros}")
    print(f"- Letras erradas: {letrasErradas}")
    print(f"- Total de Acertos: {totalAcertos}")
    print(f"- Letras certas: {letrasCertas}")
    print("\n")
    
    # Verifica se o jogador ganhou ou perdeu
    if all(letra in letrasCertas for letra in palavraSecreta):
        print("Você ganhou!!!")
        break
    if totalErros == 6:
        print("Você perdeu!!!")
        break
