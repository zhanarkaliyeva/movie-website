import webbrowser

class Movie():
    '''creates a data structure to store my favorite movies
        including movie title, plot summary, poster URL, a YouTube link to the movie trailer
        and a launch date'''
    def __init__(self, movie_title, movie_storyline,poster_image,
                 trailer_youtube,launch_date): #Initialises class instance variables.
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.launch_date=launch_date

    def show_trailer(self):#Plays trailer in the web browser.
        webbrowser.open(self.trailer_youtube_url)

