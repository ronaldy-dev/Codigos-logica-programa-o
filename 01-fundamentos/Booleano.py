#ACERTAR SENHA 

senha_correta = 1234
usuario_logado = False

senha = int(input("Digite sua senha: "))

if senha == senha_correta:
    usuario_logado = True
    print("Senha correta! Usuário logado.")
else:
    print("Senha incorreta.")


#INGRESSO CINEMA
tem_ingresso = True

ingresso = input("Você tem ingresso? ")
if ingresso == "sim":
    tem_ingresso = True
    print("Entrada permitida")
else:
    tem_ingresso = False
    print("Entrada não permitida.")


#LUZ ACESSA
luz_acesa = False

luz = input("A luz esta acesa? S/N: ")
if luz == "S":
        luz_acesa = True
        print("A luz esta acesa")
else:
     print("A luz esta apagada, ligando ela...")



#MAIOR OU MENOR DE IDADE

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


#PERGUNTA SE GOSTA OU NÃO
gostar_de_programação = True

pergunta = input("Você gosta de programação?: ")
if pergunta == "sim":
    print("Boa! Vamos continuar!")
else:
     print("Vou tentar te ajudar a gostar.")









    

