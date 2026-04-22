from enum import Enum
class Cor(Enum):
    VERMELHO = 'vermelho'
    VERDE = 'verde'
    AZUL = 'azul'

cor = Cor(input("Insira sua escolha de '\033[31mvermelho\033[m, '\033[34mazul\033[m' ou '\033[32mverde\033[m': "))

match cor:
    case Cor.VERMELHO:
        print("\033[31mEu vejo vermelho\033[m!")
    case Cor.VERDE:
        print("\033[32mGrama é verde\033[m!")
    case Cor.AZUL:
        print("\033[34mO céu é azul\033[m :)")