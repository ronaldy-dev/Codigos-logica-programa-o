# Medidor de velocidade 

'''
Crie um programa que recebe do usuario um valor que represente a velocidade em uma via cuja 
velocidade máxima permitida é de 80km/h.

Com base nese valor, o programa deve informar se o motorista levou um amulta leve, grave ou gravissima.

Se a velocidade estiver abaixo ou igual a 80 km/h, exiba: 'não houve multa'.
Se estiver até 10 km/h acima, exiba: 'levou multa leve'.
Se estiver entre 11km/h e 20km/h acima, exiba: 'levou multa grave'.
Se estiver acima de 20 km/h, exiba: 'levou multa gravissima'.
'''
velocidade = float(input('Digite a velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('não houve multa')
elif velocidade <= velocidade_maxima + 10:
    print('houve multa leve')
elif velocidade <= velocidade_maxima + 20:
    print('houve multa grave')
else:
     print('houve multa gravissima')

   

  
