class People:
    def __init__(self, nome=None, idade=19):
        self.idade = idade
        self.nome = nome

    def cumprimentar (self):
        return f'ola {id(self)}'


if __name__ == '__main__':
    p = People('Keanu')
    print(People.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)
    print(p.idade)
    