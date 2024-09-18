#19/08/2024 Professor Gilberto - Aluno: Willian
#Exercicio 1
#Programa para calcular a variação do Dolar.
'''
print("Sistema de Conversão do  Dólar")
print("Desenvolvido por: Willian Shigueo da Rocha Anno")
print("Copywrite 2024")
print("Versão 1.0")

while True:
    valorEmDolar = float(input("Valor do produto em Dólar: US$ "))
    cotacaoDolarHoje = float(input("Digite a cotação de dólar: R$ "))
    
    valorConvertido = (valorEmDolar * cotacaoDolarHoje)

    print(f"O Valor convertido é: R$ {valorConvertido:.2f} reais") # O "f" no começo do print é pra mencionar uma ou + variaveis no conjunto em CHAVES, e o .2f dentro da chaves significa para aperecer 2 casas decimais.
    sair = input("Deseja converter outro valor? <S/N>")
    if sair.upper() == "N":
        break

print("Agradeço pela visita. Volte Sempre")

'''

#Exercicio 2
'''
Mostrar um programa em Python para calcular os juros de uma conta atrasada:

Pedir:
1-) Valor da conta
2-) dias de atraso
3-) Juros por dia

Fórmula:
Valor Corrigido = valorDaConta + (ValorDaConta * diasAtraso * jurosPorDia)
'''
while True:
    valorDaConta = float(input ("Digite o valor da conta: R$ "))
    diasAtraso = int(input("Digite a quantidade de dias atrasado: "))
    jurosPordia = float(input("Informe o Juros por Dia: % "))

    valorCorrigido = valorDaConta + (valorDaConta * diasAtraso * (jurosPordia/100))
    print(f"O novo valor corrigido com o Juros é: R$ {valorCorrigido:.2f} reais ")
    sair = input("Deseja realizar outro calculo? <S/N>")
    if sair.upper() == "N":
        break



