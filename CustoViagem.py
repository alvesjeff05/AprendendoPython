distancia = float(input("Digite a distância da sua viagem: "))
curta = distancia * 0.50
longa = distancia * 0.45

if distancia <= 200:
    print(f"A sua viagem custará {curta} reais.")
else:
    print(f"A sua viagem custará {longa} reais.")