import fresh_tomatoes
import movie


toy_story = movie.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=ZZv1vki4ou4")

# print(toy_story.storyline)

# toy_story.show_trailer()

movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
