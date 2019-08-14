class People:
    def cumprimentar (self):
        return f'ola{id(self)}'


if __name__ == '__main__':
    p = People()
    print(People.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
