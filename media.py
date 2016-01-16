import webbrowser

class Video():
    """
        This class holds base Video data
    """
    def __init__(self, title, synopsis, poster_image_url, trailer_youtube_url, year_released, tag_line):
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.year_released = year_released
        self.tag_line = tag_line


class Movie(Video):
    """
        This class provides moving info
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, synopsis, poster_image_url, trailer_url, year_released, tag_line):
        Video.__init__(self, title, synopsis, poster_image_url, trailer_url, year_released, tag_line)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)