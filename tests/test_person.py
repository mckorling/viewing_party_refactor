import pytest
from viewing_party.person import Person
from viewing_party.movie import Movie


def test_person_attributes_set_up():
    # Arrange/Act
    movie = Movie("The Avengers", "action", 4, "Disney+")
    person = Person("Diana", [], [movie], ["Disney+"])

    # Assert
    assert person.name == "Diana"
    assert person.watched == []
    assert person.friends == [movie]
    assert person.subscriptions == ["Disney+"]

def test_adds_movie():
    # Arrange
    movie = Movie("The Avengers", "action", 4, "Disney+")
    person = Person("Diana", [], [], ["Disney+"])

    # Act
    person.add_watched(movie)

    # Assert
    assert movie in person.watched
    assert len(person.watched) == 1

def test_get_num_watched():
    # Arrange
    movie1 = Movie("The Avengers", "action", 4, "Disney+")
    movie2 = Movie("Talladega Nights", "comedy", 4, "Netflix")
    person = Person("Megan", [movie1, movie2], [], ["Netflix"])

    # Act
    result = person.get_num_watched()

    # Assert
    assert result == 2