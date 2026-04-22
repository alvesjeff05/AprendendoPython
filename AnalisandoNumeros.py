num = int(input("Informe o número: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f"O número informado foi {num}.")
print(f"A unidade é {unidade}.")
print(f"A dezena é {dezena}.")
print(f"A centena é {centena}.")
print(f"A milhar é {milhar}.")