import time, random

# print("aguarde....")
# time.sleep(3)
# print("Pronto!!")

while True:
    numero_aleatorio = random.randint(1, 50)
    print(numero_aleatorio)
    time.sleep(1)
    if numero_aleatorio % 2 == 0:
        break

