nome = str(input('Digite o nome: '))
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso/(altura * altura)

if imc < 18.5:
    print(f'{nome} está com {peso} e {altura}m e está com {imc:.1f} de imc, estando abaixo do peso recomendado.')
elif 18.5 <= imc <= 25:
    print(f'{nome} está com {peso} e {altura}m e está com {imc:.1f} de imc, estando no peso ideal.')
elif 25 <= imc <= 30:
    print(f'{nome} está com {peso} e {altura}m e está com {imc:.1f} de imc, estando com sobrepeso.')
elif 30 <= imc <= 40:
    print(f'{nome} está com {peso} e {altura}m e está com {imc:.1f} de imc, estando com obesidade.')
else:
    print(f'{nome} está com {peso} e {altura}m e está com {imc:.1f} de imc, estando com obesidade mórbida.')