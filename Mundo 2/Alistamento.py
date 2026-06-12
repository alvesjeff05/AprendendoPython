nome = str(input("Digite seu nome: "))
anoNascimento = int(input("Digite sua data de nascimento: "))
idade = 2024 - anoNascimento
tempoAlistamento = idade - 18


if idade < 18:
    print(f"{nome}, você tem {idade} anos. Você ainda é menor de idade e não pode se alistar.")
    print(f"Faltam {abs(tempoAlistamento)} anos para você se alistar.")
elif idade == 18:
    print(f"{nome}, você tem {idade} anos. Você deve se alistar imediatamente!")
else:
    print(f"{nome}, você tem {idade} anos. Você já passou do tempo de se alistar.")
    print(f"Você passou {abs(tempoAlistamento)} anos do prazo de alistamento.")