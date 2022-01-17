import requests
import json
import random


from requests.models import HTTPError
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYjBhNTA1ZjFhODE0MjAwYzE1NTgxZjEyNTRiYzhkNyIsInN1YiI6IjYxNTIyMzVjNjdkY2M5MDA4Y2U3MTJmMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gLDUgiPELKhb2kjwkyq0jYUuJxaIhLtTL-J3AqT2z2M"

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization" : f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_popular_movies(popular):
    return call_tmdb_api(f"movie/{popular}")

# dictionary = get_popular_movies()
# print(dictionary) - te dwa zapisy - żeby zobaczyć wynik terminalu

def get_poster_url(poster_api_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")
    
def get_movies3(how_many, list_type):       
    alfa = get_movies_list(list_type)
    gamma = random.sample(alfa['results'], len(alfa['results']))
    return gamma[:how_many]

def get_single_movie(movie_id):
    return call_tmdb_api(f'movie/{movie_id}')

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"] # a czemu ten dopisek? Tworzymy cały czas jeden plik .json i wybieramy konkretne klucze z wartościami?"""