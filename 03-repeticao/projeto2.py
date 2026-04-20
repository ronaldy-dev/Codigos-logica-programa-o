# Projeto 2 - Chute um numero
'''
Escreva um programa que, ao iniciar, gere um valor aleatorio de 1 a 10 e permita que
o usuario chute números até acertar o valor gerado.

O programa deve informar se o chute foi maior, menor ou igual ao valor aleatorio gerado no inicio.
'''
import random

valor_aleatorio = random.randint(1, 10)
acertou = False 

print("\n=== CHUTE UM NUMERO DE 1 A 10 ===")

while acertou == False:
    chute =  int(input('Chute um valor: '))
    if chute > valor_aleatorio:
        print('chute mais baixo')
    elif chute < valor_aleatorio:
        print('chute um valor mais alto')
    else:
        print('Você acertou o valor')
        acertou = True
