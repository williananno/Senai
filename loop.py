limite = int(input("Digite um numero: "))
print ("contando...")
x = 2
for contador in range (limite):
    print ("A soma de", contador, " + " , x , "=" , contador+x)
    x = x + 1