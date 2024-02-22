from modelo import Filme
from modelo import Serie

filme = Filme('os incríveis', 2010, 90)

serie = Serie('Demon Slayer', 2021, 3)

serie.dar_like()
serie.dar_like()

print(f'Nome: {filme.nome} | Ano: {filme.ano} | Duração: {filme.duracao} | Likes: {filme.likes}')
print(f'Nome: {serie.nome} | Ano: {serie.ano} | Temporadas: {serie.temporadas} | Likes: {serie.likes}')
