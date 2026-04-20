contador = 10
while contador >= 1:
    print(f"contagem atual: {contador}")
    contador -=1


senha = "rainbow34"
tentativa_senha = ""
while senha != tentativa_senha:
    tentativa_senha = input("digite sua senha: ")
    if tentativa_senha != senha:
        print("senha incorreta!!")
        break
    else:
        print("senha correta")    


numeros = [3, 4, 7, 9, 8, 2, 1] 
for numero in numeros:
    if numero % 2==0:
      print(numero)
      break        













