nome = str(input("Digite seu nome: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f"{nome}, sua média é {media:.1f}. Você está \033[31mREPROVADO\033[m!!!")
elif 5.0 <= media < 6.9:
    print(f"{nome}, sua média é {media:.1f}. Você está de \033[33mRECUPERAÇÃO\033[m!!!")
else:
    print(f"{nome}, sua média é {media:.1f}. Você está \033[32mAPROVADO\033[m!!!")