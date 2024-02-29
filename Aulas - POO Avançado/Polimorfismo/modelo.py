
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self._nome} | Ano: {self.ano} | Qtd Likes: {self._likes}'


class Filme(Programa):
     def __init__(self, nome, ano, duracao):
         super().__init__(nome, ano)
         self.duracao = duracao

     def __str__(self):
        return f'{super().__str__()} | Duração: {self.duracao}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{super().__str__()} | Duração: {self.temporadas}'
    


class AvaliaPrograma:
    def __init__(self):
        self.__avaliacoes = 0
    

    def avalia(self, programa):
        
        resp = str(input(f'voce gostou de assistir {programa.nome} ? [S/N]: ')).lower()

        if resp == 's':
            self.__avaliacoes += 1
            programa.dar_like()
            print('resposta gravada')
        else:
            print('resposta gravada')