class Pessoa(object):
    
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def idade(self, hoje):
        hd, hm, ha = hoje
        nd, nm, na = self.nascimento
        xd, xm, xa = hd - nd, hm - nm, ha - na
        if xd >= 0 and xm >= 0 and xa >= 0:
            return xa
        else:
            return xa - 1

class User(object):

    seq = 0
    objects = []

    def __init__(self, nome, idade):
        self.id = None
        self.nome = nome
        self.idade = idade

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.objects.append(self)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return '<{}: {} - {} - {}>'.format(self.__class__.__name__, self.id, self.nome, self.idade)

    @classmethod
    def all(cls):
        return cls.objects

if __name__ == '__main__':
    pass