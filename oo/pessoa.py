class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributtos_de_classe(cls):
            return f'{cls} - olhos {cls.olhos}'

#sobreescrita de método
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}. Aperto de mão'

# sobreescrita de atributo
class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    heitor = Mutante(nome="Heitor")
    max_wilson = Homem(heitor, nome="Max")
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
    print(Pessoa.olhos)
    print(heitor.olhos)
    print(max_wilson.olhos)
    heitor.olhos = 1
    print("_________________")
    print(Pessoa.olhos)
    print(heitor.olhos)
    print(max_wilson.olhos)
    print("_________________")
    print(Pessoa.olhos)
    print(heitor.olhos)
    print(max_wilson.olhos)
    del heitor.olhos
    print("_________________")
    print(Pessoa.olhos)
    print(heitor.olhos)
    print(max_wilson.olhos)

    pessoa = Pessoa("Anonimo")
    # função isinstace() retorna se uma função é igual a comparação
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    # se o objeto é do tipo de um classe que extende outra clase,
    # o objeto será do tipo pai e avô
    print(isinstance(heitor, Homem))
    print(isinstance(heitor, Homem))
    print(heitor.olhos)
    print(heitor.cumprimentar())
    print(max_wilson.cumprimentar())
