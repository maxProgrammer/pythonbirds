class Pessoa:
    # atributos de instancia e objetos são criados
    # através do método especial dunder init

    def __init__(self, nome=None):
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Renzo'
    print(p.nome)
