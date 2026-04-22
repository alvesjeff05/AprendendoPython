class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def onde_esta(ponto):
    match ponto:
        case Ponto(x=0, y=0):
            print("Origem")
        case Ponto(x=0 , y=y):
            print(f"Y = {y}")
        case Ponto(x=x, y=0):
            print(f"X = {x}")
        case Ponto():
            print("Em outro lugar")
        case _:
            print("Não é um ponto")

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

ponto = Ponto(x, y)
onde_esta(ponto)