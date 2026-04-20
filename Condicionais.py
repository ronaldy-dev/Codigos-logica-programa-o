#Condicionais - if elif else
'''
E ae jhonatan, bora dar uma saida hoje ?
Se eu terminar meu trabalho aqui eu consigo.
'''
trabalho_terminado = input('Você terminou o trabalho, S/N ? ')
if trabalho_terminado == "S":
    print("Então bora!")
else:
    print('Tá traqnuilo')




'''syntaxe
if condição:
    #código se verdadeiro
else:
    #código em qualquer outro caso    

'''

'''
Ei, você consegue me ajudar a mover essas caixas lá para fora
hoje a tarde?

Se eu estiver livre, sim. mas se não der, pede meu irmão 
para te ajudar 
'''
estou_livre = input('Você está livre, SIM OU NÃO? ')
if estou_livre == 'SIM':
    print('Ok, bora mano')
else:
    print('Pede meu irmão')

#como lidar com mais que 2 condições?
'''
Eu cheguei atrasado ma aula. Ainda posso entrar?

Se for a primeira ou segunda vez que você chega atrasado, pode
sim.
Mas se for a terceira vez, você será suspenso.
'''
atrasos = int(input('quantas faltas você tem? '))
if atrasos >= 3:
    print('você está suspenso')
elif atrasos == 2:
    print('mais uma falta e será suspenso')
elif atrasos == 1:
    print('mais duas faltas e será suspenso') 
else:
    print('pode entrar')     



#PROBLEMA   
#Crie um programa que recebe dois valores e exibe qual maior entre eles.
'''
1.precisamos saber dos dois valores
2.devo indentificar qual o maior entre eles
3.deve-se informa os dois valores e o maior entre eles
4.exibir na tela o maior valor
5. receber valor 1
receber valor 2
comparar se o primeiro é maior que o segundo 
se for, exibir: 'primeiro valor é maior'
caso não, exibir: 'segundo valor é maior'

'''
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print('Primeiro valor é maior')
else:
    print('segundo valor é maior')    



