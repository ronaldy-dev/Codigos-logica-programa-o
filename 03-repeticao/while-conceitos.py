#while

'''
syntaxe
while condição:
    #codigo a ser executado
'''
#criar um programa que permite 3 tentativas, antes de fechar 
tentativas = 0
while tentativas < 3:
    print('tente novamente')
    tentativas = tentativas + 1  
# Quando queremos que uma ação continue acontecendo
#até que criterio seja satisfeito
#só pode logar, se digitar a senha correta  
senha = ''
while senha != '123456':
    senha = input('Digite a senha correta: ')

print('Bem vindo ao sistema')
#Garantir que algo esteja preenchido 
#Só deve continuar, quando o usuario informar o seu nome
nome = ''
while nome == '':
    nome = input('Digte seu nome: ')

print(f'Bem-vindo {nome}')

# Contadores dentro do while
# Ser avisado as 17hrs do por do sol
#contar de hora em hora ate chegar as 17hr
#ao chegar as 17hrs, exibir: "hora de ver o por do sol"
horario = 0 
while horario <= 17:
    print(horario)
    horario = horario + 1

print ('hora de ver o por do sol') 


#Cenario real - gerenciador de login simples
'''
Crie um gerenciador de login simples, com o maximo de 3 tentativas.
(teremos apenas um unico usuario e senha permitido)

ususario - ronaldy
senha - senha123

após e tentaivas, se o usuario estiver errado, exibir: 'aguarde 30 min antes de tentar
novamente

se acertar o usuario e senha antes disso, exibir "login feito com sucesso"
'''
usuario = ''
senha = ''
tentativa = 0

while (usuario != 'ronaldy' or senha != 'senha123') and tentativa <= 3:
    usuario = input('Digite seu usuario: ')
    senha = input('Digite sua senha: ')
    tentativa += 1

if usuario == 'ronaldy' and senha == 'senha123':
    print('Login feito com sucesso')
else:
    print('Favor espere 30min para tentar novamente')        



