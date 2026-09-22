movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]


# Here is a function that checks whether one movie has an IMDB rating above 5.5.
def is_good_movie(movie):
    return movie["imdb"] > 5.5


# Here is a function that returns movies with an IMDB rating above 5.5.
def good_movies(movie_list):
    return [movie for movie in movie_list if is_good_movie(movie)]


# Here is a function that returns movies from a selected category.
def movies_by_category(movie_list, category):
    return [
        movie
        for movie in movie_list
        if movie["category"].lower() == category.lower()
    ]


# Here is a function that calculates the average IMDB rating.
def average_imdb(movie_list):
    if not movie_list:
        return 0

    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)


# Here is a function that calculates the average IMDB rating for a category.
def average_category_imdb(movie_list, category):
    return average_imdb(movies_by_category(movie_list, category))


if __name__ == "__main__":
    print("Good movie:", is_good_movie(movies[0]))
    print("Good movies:", good_movies(movies))
    print("Romance:", movies_by_category(movies, "Romance"))
    print("Average IMDB:", average_imdb(movies))
    print("Romance average:", average_category_imdb(movies, "Romance"))
