from operator import pos
from unittest import mock
import requests
import tmdb_client
from unittest.mock import Mock

def test_call_tmdb_api(monkeypatch):
    # lista, która bedzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']
    # id, które będzie zwracać przysłonięte "zapytanie do API"
    mock_single_movie = 123456
    # wywołanie konkretnej listy - "popular"
    mock_popular_movies = str('popular')

    requests_mock = Mock()
    # wynik wywolania zapytania do API zamieniamy na nasze podstawienie testowe
    response = requests_mock.return_value
    # przysłaniamy wynik wywołanie metody .json - do wyboru "mock_movies_list", "mock_single_movie", "mock_popular_movies" dla uniwersalnej funkcji "call_tmdb_api"
    response.json.return_value = mock_popular_movies
    # odwołanie się specjalnym modułem monkeypatch do odpowiedniej funkcji w testowanym właśnie skrypcie wraz z przypisaniem również funkcji od klasy Mock()
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie_id = tmdb_client.get_single_movie('upcoming')
    assert movie_id == mock_popular_movies

def test_get_movie_image_size(monkeypatch):
    # ścieżka konkretnego obrazka z filmu z rozszerzeniem .jpg
    mock_poster_api_path = "abcdefghijklmn.jpg"
    # podany wymiar obrazka
    mock_image_size = "w342"
    # przysłaniamy główny człon adresu url
    base_url_mock = Mock()
    # przypisujemy zmienną, która będzie się podszywać pod człon adresu
    recall_path = base_url_mock.return_value
    # nadajemy swoje wartości do adresu url
    recall_path.return_value = f'https://image.tmdb.org/t/p/{mock_image_size}/{mock_poster_api_path}'
    # przywołujemy funkcje z naszymi parametrami
    monkeypatch.setattr("tmdb_client.get_poster_url", base_url_mock)
    # przywołujemy oryginalną funkcję
    poster_size = tmdb_client.get_poster_url(size='w342',poster_api_path='.jpg')
    # porównujemy
    assert poster_size is recall_path

"""def test_get_single_movie_cast(monkeypatch): #złe
    # id, które będzie zwracać przysłonięte "zapytanie do API"
    mock_single_movie = 1234434

    requests_mock = Mock()
    response = requests_mock.return_value
api_mockt.get_single_movie_cast(movie_id=mock_single_movie)
    assert movie_id == mock_single_movie
"""
"""def test_get_single_movie_cast(monkeypatch): # złe bo dalej wyciąga w w setattr json, którego nie może odczytać ze wzglęfu na konkretny słownik 'cast'
    api_mock = Mock(return_value={'cast':['Actor 1','Actor 2']})
    movie_id = 10
    monkeypatch.setattr("tmdb_client.requests.get", api_mock)
    get_movie_cast = tmdb_client.get_single_movie_cast(movie_id=movie_id)
    assert get_movie_cast is not None"""

def test_get_single_movie_cast(monkeypatch):
    api_mock = Mock(return_value={'cast':['Actor 1','Actor 2']})
    movie_id = 568124
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    get_movie_cast = tmdb_client.get_single_movie_cast(movie_id=movie_id)
    assert get_movie_cast == ['Actor 1','Actor 2']
    # lub assert is not None