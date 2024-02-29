from modelo import Filme, Serie, AvaliaPrograma

filme1 = Filme('Os incriveis', 2005, 90)
serie1 = Serie('Broklyn99', 2020, 8)
avaliacao = AvaliaPrograma()

print(filme1)
print(serie1)

avaliacao.avalia(filme1)

filme1.nome = 'Os incriveis 2'

print(f'Nome: {filme1.nome} - Likes: {filme1._likes}')