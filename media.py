import webbrowser


# Criada a classe Movie com seus atributos
class Movie():
    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Metodo que exibe o trailer da classe movie no browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
