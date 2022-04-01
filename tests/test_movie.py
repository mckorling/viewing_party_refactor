import pytest
from viewing_party.movie import Movie

def test_movie_attributes():
    # Arrange/Act
    movie = Movie("Encanto", "children", 5, "Disney+")

    # Assert
    assert movie.title == "Encanto"
    assert movie.genre == "children"
    assert movie.rating == 5
    assert movie.host == "Disney+"

def test_movie_rating_updates():
    # Act
    movie = Movie("Encanto", "children", 5, "Disney+")

    # Arrange
    movie.update_rating(10)

    # Assert
    assert movie.rating == 10
