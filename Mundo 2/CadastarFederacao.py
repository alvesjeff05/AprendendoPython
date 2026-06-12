nome = str(input('Digite o nome do atleta: '))
idade = int(input('Digite a idade do atleta: '))

if idade <= 9:
    print(f'{nome} está na categoria MIRIM.')
elif 10 <= idade <= 14:
    print(f'{nome} está na categoria INFANTIL.')
elif 15 <= idade <= 18:
    print(f'{nome} está na categoria JUNIOR.')
elif 19 <= idade <= 20:
    print(f'{nome} está na categoria SÊNIOR.')
else:
    print(f'{nome} está na categoria MASTER.')