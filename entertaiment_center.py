import media
import fresh_tomatoes

# Criada instancia da classe Movie do filme Matrix
matrix = media.Movie("Matrix",
                     "Não importa o quão difícil seja uma situação, o quão pequenas\
                      sejam suas chances de conseguir sucesso ou o preço a ser\
                      pago pela verdade, ainda assim valerá a pena lutar.",
                     "http://www.whatisthematrix.com/img/matrix.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Criada instancia da classe Movie do filme O Senhor dos Aneis
senhor_dos_aneis = media.Movie("O Senhor dos Aneis",
                               "A história narra o conflito contra o mal que se\
                                alastra pela Terra-média, através da luta \
                                de várias raças.",
                               "http://br.web.img3.acsta.net/c_215_290/medias/nmedia/18/92/91/32/20224832.jpg",  # noqa
                               "https://www.youtube.com/watch?v=IUerKBZHnBs")

# Criada instancia da classe Movie do filme Homen Aranha
spider_man = media.Movie("Homem-Aranha",
                         "A historia de um homen picado por uma aranha que\
                          vira super heroe",
                         "https://pm1.narvii.com/6122/25c286a99381ef79bb8df1dfaee31685390b502b_hq.jpg",  # noqa
                         "https://www.youtube.com/watch?v=-1xN3r77GlU")

# Criada instancia da classe Movie do filme Divergente
divergente = media.Movie("Divergente",
                         "A história introduz a vida de Beatrice Prior, uma \
                         corajosa jovem de 16 anos que ameaça destruir o \
                         sistema implantado na cidade, pois não corresponde\
                         aos padrões estabelecidos pela mesma.",
                         "https://upload.wikimedia.org/wikipedia/pt/thumb/8/8e/Divergent.png/240px-Divergent.png",  # noqa
                         "https://www.youtube.com/watch?v=IioBZ0rJdyI")

# Criada instancia da classe Movie do filme Sem Limites
limitless = media.Movie("Sem Limites",
                        "Com uma droga voce pode utilizar todo o poder do\
                         cerebro  e virar tecnicamente sem limites.",
                        "https://upload.wikimedia.org/wikipedia/pt/1/17/Limitless_Poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=JMU_ksS3fq4")

# Criada instancia da classe Movie do filme Jogos Vorazes
hunger_games = media.Movie("Jogos Vorazes",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# Criada instancia da classe Movie do filme Maze Runner
maze_runner = media.Movie("Maze Runner - Correr o Morrer",
                          "Voce precisa correr por sua vida",
                          "https://upload.wikimedia.org/wikipedia/pt/c/c7/Maze_runner.jpg",  # noqa
                          "https://www.youtube.com/watch?v=uriiz3G8ALw")

# Criada instancia da classe Movie do filme Matrix
transformers = media.Movie("Transformers",
                           "Carros incriveis ou robots poderosos",
                           "https://upload.wikimedia.org/wikipedia/pt/e/ee/Transformers-poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=jZ6Q1B6x3p0")

# Criada instancia da classe Movie do filme 300
os_300 = media.Movie("300",
                     "300 pessoas podem derrotar qualquer exercito",
                     "https://upload.wikimedia.org/wikipedia/pt/1/19/300_poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=mi4xUUJSuro")

# Criada lista de filmes (movies) e adicionadas todas as instancias de filmes
# anteriores
movies = [matrix, senhor_dos_aneis, spider_man, divergente,
          limitless, hunger_games, maze_runner, transformers, os_300]

# utilizado o metodo open_movies_page do arquivo fresh_tomatoes para abrir uma
# pagina web no browser e exibir todos os filmes que estam na lista movies,
# este metodo recebe como parametro a lista movies
fresh_tomatoes.open_movies_page(movies)
