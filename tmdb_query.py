import tmdbsimple as tmdb


class QueryTmdb():

    def __init__(self, id):
        self.id = id
        self.title = ""
        self.release_date = ""
        self.description = ""
        self.tag_line = ""

        tmdb.API_KEY = ''#add you api_key here

    def query_movie(self):
        movie = tmdb.Movies(self.id)
        movie_response = movie.info()
        self.title = movie.title
        self.description = movie.overview
        self.release_date = movie.release_date
        self.tag_line = movie.tagline


tangled = QueryTmdb(38757)
tangled.query_movie()

lebowski = QueryTmdb(115)
lebowski.query_movie()

first_contact = QueryTmdb(199)
first_contact.query_movie()

avatar = QueryTmdb(19995)
avatar.query_movie()

bolt = QueryTmdb(13053)
bolt.query_movie()

transformers = QueryTmdb(1858)
transformers.query_movie()
