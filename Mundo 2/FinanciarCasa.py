valorCasa = float(input("Informe o valor da casa desejada: "))
salario = float(input("Informe o salário do comprador: "))
tempoFinanceamento = float(input("Em quantos anos deseja pagar: "))
parcelas = tempoFinanceamento * 12
valorMensal = valorCasa / parcelas

if valorMensal <= salario * 0.30:
    print(f"O empréstimo solicitado foi \033[32mAPROVADO\033[m!!!]")
else:
    print(f"O empréstimo foi \033[31mNEGADO\033[m!!!")