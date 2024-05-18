from django.db import models


class FilmTypeChoices(models.TextChoices):
    MOVIE = "Movie"
    SERIES = "Series"
    ANIMATION = "Animation"
    SHORT_FILM = "Short-film"
    MINI_SERIES = "Mini-Series"


class GenreChoices(models.TextChoices):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    ANIMATION = "Animation"
    BIOGRAPHY = "Biography"
    COMEDY = "Comedy"
    CRIME = "Crime"
    DOCUMENTARY = "Documentary"
    DRAMA = "Drama"
    FAMILY = "Family"
    FANTASY = "Fantasy"
    HISTORY = "History"
    HORROR = "Horror"
    MUSIC = "Music"
    MUSICAL = "Musical"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    SCIENCE_FICTION = "Science Fiction"
    SPORT = "Sport"
    THRILLER = "Thriller"
    WAR = "War"
    WESTERN = "Western"
