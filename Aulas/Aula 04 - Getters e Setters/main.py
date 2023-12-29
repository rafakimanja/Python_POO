
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    @property #getter
    def preco(self):
        return self._preco

    @preco.setter #setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


prod1 = Produto('ULTRABOOST', 800)
print(prod1.nome, prod1.preco)
prod1.desconto(15)
print(prod1.nome, prod1.preco)

prod2 = Produto('Meia', 'R$30')
prod2.desconto(15)
print(prod2.nome, prod2.preco)
