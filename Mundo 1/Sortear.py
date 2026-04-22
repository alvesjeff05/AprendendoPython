import random
alunos = []

while True:
    nome = input('Digite os nomes dos alunos: ')
    if nome.lower() == 'sair':
        break
    alunos.append(nome)
escolhido = random.choice(alunos)
random.shuffle(alunos)
print(f'{escolhido} apagará o quadro!')
print(f'E a ordem de apresentação será {alunos}.')