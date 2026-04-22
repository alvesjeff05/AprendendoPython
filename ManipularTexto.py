nome = input("Informe seu nome completo: ")
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
quantidadeLetras = len(nome.replace(" ", ""))
primeiroNome = nome.split()[0]
quantidadePrimeiroNome = len(primeiroNome.replace(" ", ""))


print("Analisando...")
print(f"Seu nome é: {nome}.")
print(f"Seu nome maiúsculo é: {nomeMaiusculo}.")
print(f"Seu nome minúsculo é: {nomeMinusculo}.")
print(f"Seu nome tem {quantidadeLetras} letras.")
print(f"Seu primeiro nome é: {primeiroNome} e possui {quantidadePrimeiroNome} letras.")