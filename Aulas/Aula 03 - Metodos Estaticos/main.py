from datetime import datetime


class Pessoa:

    ano_atual = datetime.now().year

    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def gera_por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        from random import randint
        rand = randint(1, 10)
        return rand
