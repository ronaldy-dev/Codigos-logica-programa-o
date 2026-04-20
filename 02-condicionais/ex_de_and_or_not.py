idade = int(input("Digite sua idade: "))
ingresso = input("Tem ingresso (S/N) ?: ")
acompanhado = input("Voce esta acompanhado (S/N) ?: ")
if ingresso == "S" and idade >= 18:
    print("Entrada liberada sem restrição")
elif ingresso == "S" and (idade == 16 or idade == 17)and acompanhado == "S":
    print("Entrada permitida, com o acompanhante")
else:
    print("Entrada negada")












