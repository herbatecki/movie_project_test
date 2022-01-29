from flask import Flask, render_template, url_for, request
import tmdb_client
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type','upcoming')
    movies = tmdb_client.get_movies3(how_many=8,list_type= selected_list)
    return render_template('homepage.html', movies=movies,current_list = selected_list)

"""
@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    movies = tmdb_client.get_movies2(how_many=8, list_type = selected_list)
    return render_template('homepage.html', movies=movies, list_type = selected_list)
"""

"""
@app.route('/')
def homepage():
    # movies = tmdb_client.get_popular_movies()["results"][:12] - tożsamy zapis posiada nową funkcją get_movies w 'tmdb_client'
    movies = tmdb_client.get_movies(how_many=8)
    return render_template('homepage.html', movies=movies)
"""


@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id) # bez tej funkcji nie pojadę, nawet do PUSTEGO szablonu
    cast = tmdb_client.get_single_movie_cast(movie_id)[:12]
    return render_template("movie_details.html" , movie=details, cast=cast)

"""
@app.route('/movie/<movie_id>/credits')
def movie_credits(movie_id):
    credits = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("" , movie=credits) # nie można zrobić osobnego routingu, tak jak tu?
"""

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.context_processor
def get_movie_info():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    def tmdb_popular_title(title):
        return tmdb_client.get_poster_url(title)
    return {"tmdb_popular_title": tmdb_popular_title, "tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)