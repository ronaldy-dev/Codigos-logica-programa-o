#Peça um numero e faça uma contagem regressiva ate zero, exibindo cada numero.

inicio = int(input("Digite um numero para fazer a contagem regressiva dele: "))
for i in range(inicio, -1, -1):
    print(i)
