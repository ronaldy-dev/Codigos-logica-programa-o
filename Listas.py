#Listas
precos = [20, 50, 100]
print(precos[0]) #acessando por indice

nomes = ['Brazil', 'EUA', 'Mexico']
print(nomes[1]) #acessando por indice

#Encontrar indice automaticamnete
print(nomes.index('EUA'))

# manipular - add novos itens
salarios = [2500, 5000, 7000]
salario_usuario = float(input('Qual é o seu salário: '))
salarios.append(salario_usuario)
print(salarios)

#Problema - Gastos totais com pagamento de salarios.
#dado uma lista de salarios, calcule o total pagoa todos os funcionarios
salarios = [2500, 900, 5000, 7500]
total = 0
for salario in salarios:
    total = total + salario # 2500 -> 2500 + 900 -> 3400 + 5000 -> 8400 + 7500 -> 15900
print(total)