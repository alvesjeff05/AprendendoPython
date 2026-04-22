import random

num = random.randint(0, 5)
escolha = int(input("Escolha um número entre 0 e 5: "))
if escolha == num:
    print("Você acertou!")
else:
    print("Mais sorte na próxima!")