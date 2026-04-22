num1 = int(input("Escolha um número qualquer: "))
num2 = int(input("Escolha um número qualquer: "))
num3 = int(input("Escolha um número qualquer: "))
maior = 0
menor = 0

if num3 < num1 > num2:
    maior = num1
    print(f"O maior número é: {maior}")
if num1 < num2 > num3:
    maior = num2
    print(f"O maior número é: {maior}")
if num2 < num3 > num1:
    maior = num3
    print(f"O maior número é: {maior}")

if num3 > num1 < num2:
    menor = num1
    print(f"O menor número é: {menor}")
if num1 > num2 < num3:
    menor= num2
    print(f"O menor número é: {menor}")
if num2 > num3 < num1:
    menor = num3
    print(f"O menor número é: {menor}")