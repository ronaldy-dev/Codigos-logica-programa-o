# Projeto 1 - Fatorial de um numero
# Crie um programa que recebe um numero e imprime o seu fatorial.

numero = int(input('Digite o fatorial que deseja calcular: '))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1, numero+1):
        print(f'{fatorial} * {item}')
        fatorial = fatorial * item
        print(f'{fatorial}')
    print(f'o fatorial de {numero} é {fatorial}')
else:
    print('favor informar apenas numeros inteiros positivos')



    
