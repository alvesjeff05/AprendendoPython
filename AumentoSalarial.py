funcionario = str(input("Digite o nome do funcionário: "))
salario = float(input("Digite o salário do funcionário: "))
aumento = 0
salarioAtual = 0
if salario > 1.250:
    aumento = salario * 0.10
    salarioAtual = salario + aumento
    print(f"O salário atual é de {salarioAtual} reais.")
if salario <= 1.250:
    aumento = salario * 0.15
    salarioAtual = salario + aumento
    print(f"O salário atual é de {salarioAtual} reais.")
print(f"O salário de {funcionario} é de {salario} reais e ele teve um aumento de {aumento} reais e o salário atual ficará em {salarioAtual} reais.")