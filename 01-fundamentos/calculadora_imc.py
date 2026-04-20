#Calcule e exiba o IMC(peso/altura²) e mostre o resultado.
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura*2)
print(f"O IMC é: {imc:.2f}")