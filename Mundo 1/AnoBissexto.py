ano = int(input("Escolha um ano: "))
if ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é um ano bisexto!")
else:
    print(f"{ano} não é um ano bisexto!")