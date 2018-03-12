import fresh_tomatoes
import media

"""Creates six instances of Movie class to represent my favorite movies"""

bad_weddings=media.Movie("Serial (Bad) Weddings",
                      "A Catholic French couple sees their life upside down when their four daughters get married to men of different religion and origins.",
                      "http://www.moviexclusive.com/Files/SBW%20final%20poster%20(11%20Dec).jpg",
                      "https://www.youtube.com/watch?v=IbyLWzBLLf8", "16 April 2014")


proposal=media.Movie('The Proposal', "Margaret Tate (Sandra Bullock) is an executive editor in chief of a book publishing company.",
                   "https://images-na.ssl-images-amazon.com/images/I/41W0Jy-GeKL._SY450_.jpg",
                   "https://www.youtube.com/watch?v=RFL8b1p1ELY", "June 1, 2009")


glee=media.Movie("Glee", "The series focuses on a high school show choir, also known as a glee club",
                 "http://3.bp.blogspot.com/-wGRLb8S3lqw/UM5UxX-Kn0I/AAAAAAACKT0/hk0LfocA_Dc/s1600/glee_poster60.jpg",
                 "https://www.youtube.com/watch?v=8LpwYKLOjY4","May 19, 2009")


ratatouille=media.Movie("Ratatouille", "A rat is a chef in Paris",
                        "http://i.yomyomf.com/wp-content/uploads/2011/10/ratatouille-digital-large.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk","29 June 2007")


ugly_truth=media.Movie('The Ugly Truth','Abby Richter is a morning show TV producer in Sacramento, California.',
                         "http://la-screenwriter.com/wp-content/uploads/2013/07/936full-the-ugly-truth-poster.jpg",
                         "https://www.youtube.com/watch?v=DvsZtGxsvV0","24 July 2009")


tangled=media.Movie("Tangled", "After receiving the healing powers from a magical flower, the baby Princess Rapunzel is kidnapped from the palace in the middle of the night by Mother Gothel.",
                    "https://images-na.ssl-images-amazon.com/images/I/713DcPwGUXL._SY550_.jpg",
                    "https://www.youtube.com/watch?v=50AiA9JKPUA","24 November 2010	")

movies=[bad_weddings,proposal,glee,ratatouille,ugly_truth,tangled] #group all instances in a list.
fresh_tomatoes.open_movies_page(movies) #creates an HTML file which visualizes all of my favorite movies