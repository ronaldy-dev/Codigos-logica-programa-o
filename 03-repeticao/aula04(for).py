#Laços de repetição 

for item in range(3):
    print(item)
'''
for item in colecao:
    #comandos
'''
# Range nunca inclui o último número
for item in range(1,11):
    print(item)
 
for item in range(2,12,2):
    print(item)  

#Lista de nomes 
nomes = ['jão','amanda','rafael','carol']
for nome in nomes:
    print(nome)  


#Laços de repetição e condicionais
idades = [13,25,17,21,78,55]


#Exiba somente os maiores de idade na tela
for idade in idades:
    if idade >= 18:
        print(f'{idade} é maior de idade')
    else:
        print(f'{idade} é menor de idade')  




'''
Exemplo pratico com algoritimo real: validor de senhas

Problemas:
Você trabalha em um sistemas que precisa verificar se todas as senhas digitadas por 
usuarios são válidas.

Para uma senha ser válida, ela deve ter pelo menos 6 caracteres.
'''
#len(variavel) -> quantidade de caracteres
#len(senha) -> 6 ou não
senhas = ["abc", "segura123", "12345", "python123", "oi"]
for senha in senhas:
    if len(senha)>=6:
        print(f'A senha {senha} é valida')
    else:
        print(f'A senha {senha} deve possuir no minimo 6 caracteres')    


      
        