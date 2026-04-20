# Peça números ao usuário um por um. Quando ele digitar 0, pare e mostre a soma total.

soma = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))
    
    if numero == 0:
        break
    
    soma += numero  # somar os números

print("A soma total é:", soma)