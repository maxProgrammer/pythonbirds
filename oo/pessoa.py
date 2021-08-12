class Pessoa:

      def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

      def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    heitor = Pessoa(nome ="Heitor")
    max_wilson = Pessoa(heitor, nome="Max")
    print(Pessoa.cumprimentar(max_wilson))
    print(id(max_wilson))
    print(max_wilson.cumprimentar())
    print(max_wilson.nome)
    print(max_wilson.idade)

    for filho in max_wilson.filhos:
        print(filho.nome)

    max_wilson.sobrenome = "Neto"

    print(max_wilson.sobrenome)
    print(max_wilson.__dict__)
    print(heitor.__dict__)

    del max_wilson.filhos

    print(max_wilson.__dict__)
    print(heitor.__dict__)


