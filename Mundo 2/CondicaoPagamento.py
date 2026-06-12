cliente = str(input("Digite o nome do cliente: "))
preco = float(input("\nInforme o valor do produto desejado: "))

dinheiro = preco - (preco * 0.10)
cartao = preco - (preco * 0.05)
parcela = 0

print("\n")

print("=" * 40)
print(f'{"TIPOS DE PAGAMENTO":^40}')
print("-" * 40)

print(f'{"1 - À vista":<40}')
print(f'{"2 - À vista cartão":<40}')
print(f'{"3 - Parcelado":<40}')

print("=" * 40)

pagamento = str(input("\nEscolha entre 1, 2 ou 3 para selecionar a forma de pagamento desejada: "))

if pagamento == "1":
    print(f"\n{cliente}, o valor final do seu produto fica em: {dinheiro} reais.")
if pagamento == "2":
    print(f"\n{cliente}, o valor final do seu produto fica em: {cartao} reais.")
if pagamento == "3":
    parcela = int(input("\nInforme a quantidade de parcelas desejadas: "))
    if parcela <= 2:
        print(f"\n{cliente}, o valor do seu produto permanecerá em: {preco} reais.")
    if parcela >= 3:
        print(f"\n{cliente}, o valor final do seu produto terá 20% de acréscimo pela taxa do cartão e ficará em: {preco + (preco * 0.20)}")