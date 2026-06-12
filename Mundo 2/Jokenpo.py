from random import randint
from time import sleep

print("-=" * 15)
print("Opções de escolha")
print("-=" * 15)
print("[0] - Pedra")
print("[1] - Papel")
print("[2] - Tesoura")
print("-=" * 15)

itens = ["Pedra", "Papel", "Tesoura"]
jogador = int(input("Escolha uma opção: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POOO!!")
computador = randint(0, 2)

print("-=" * 20)
print(f"O jogador escolheu {itens[jogador]}.")
print(f"O computador escolheu {itens[computador]}.")
print("-=" * 20)

if computador == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCE!")
    elif jogador == 2:
        print("COMPUTADOR VENCE!")
    else:
        print("Jogada inválida!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCE!")
    else:
        print("Jogada inválida!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE!")
    elif jogador == 1:
        print("COMPUTADOR VENCE!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("Jogada inválida!")