"""
Criar classe carro que vai possuir dois atributos compostos
por outras duas classes:
1) Motor
2) Direção

O Motor terá a responsábilidade de controlar a velocidade.
Ele oferece os seguintes atributos.
1) Atributo de dado velocidade
2) Método acelerar que deveŕa incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em 2 unidades

A direção teŕa a responsabilidade de controlar a direção. Ela
oferece os seguintes atributos:
1) valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
2) Método  girar_a_esauerda

    N
O       L
    S

    Exemplo:
    # Testando motor
    >>>motor = Motor()
    >>>motor.velocidade
    0
    >>>motor.acelerar()
    >>>motor.velocidade
    1
    >>>motor.acelerar()
    >>>motor.velocidade
    2
    >>>motor.acelerar()
    >>>motor.velocidade
    3
    >>>motor.frear()
    >>>motor.velocidade
    1
    >>>motor.frear()
    >>>motor.velocidade
    0
    >>> # Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direta()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direta()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direta()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direta()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao,motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquera()
    >>> carro.calcular_direcao()
    Oeste'
"""

NORTE = 'Norte'
LESTE = "Leste"
SUL = "Sul"
OESTE = "Oeste"


class Direcao:
    # d icionários abaixo fazem papel do if,elif, else que seriam usados
    # nas funções girar a direita e girar a esquerda

    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direta(self):
        self.valor == self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor == self.rotacao_a_esquerda_dct[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

# classe carro usa composição
class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.acelerar()

    def freiar(self):
        return self.freiar()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.girar_a_direita()

    def girar_a_esquerda(self):
        return self.girar_a_esquerda()

if __name__ == '__main__':
    pass

