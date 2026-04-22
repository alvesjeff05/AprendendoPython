reta1 = float(input("Digite o comprimento da reta: "))
reta2 = float(input("Digite o comprimento da reta: "))
reta3 = float(input("Digite o comprimento da reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Suas retas formam um triângulo.")
else:
    print("Suas retas não formam um triângulo.")