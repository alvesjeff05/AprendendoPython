def validar(nome, idade):
    if nome.strip() == "":
        print("Nome inválido!")
        return False

    if idade <= 0:
        print("Idade inválida!")
        return False

    return True


alunos = []

while True:
    nome = input("Digite o nome ou 'sair': ")
    if nome.lower() == 'sair':
        break
    
    try:
        idade = int(input("Digite a idade: "))
    except ValueError:
        idade = -1

    if validar(nome, idade):
        alunos.append([nome, idade])
        print("Aluno adicionado com sucesso!!")

print("\nLista de Alunos: ")
for i, alunos in enumerate(alunos, start=1):
    nome = alunos[0]
    idade = alunos[1]
    print(f"{i}. Nome: {nome} - Idade: {idade}")