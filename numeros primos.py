#Peça um numero e diga se ele é primo ou não. Um primo so e divisivel por 1 ou por ele mesmo.
numero = int(input("Digite um numero: "))
primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print("E primo")
else:
    print("Não e primo")





