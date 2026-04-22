velocidade = int(input("Digite a velocidade do carro em km/h: "))
excedente = velocidade - 80
multa = excedente * 7

if velocidade < 80:
    print(f"A velocidade registrada foi de {velocidade} km/h!")
else:
    print(f"A velocidade registrada foi de {velocidade}!")
    print(f"Você terá que pagar {multa} reais pela multa.")