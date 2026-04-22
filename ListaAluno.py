lista = []

while True:
    nome = input("Digite os nomes dos alunos (ou 'sair' para encerrar): ").strip()

    if nome.lower() == 'sair':
        break
    if nome == "":
        print('Um nome é necessário para continuar!')
        continue

    lista.append(nome)

print('Lista de alunos: ')
print(lista)