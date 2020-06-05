from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json

from database.models import setup_db, Actor, Movie
from app import app, ErrorMessages
from auth import requires_auth, AuthError

""" POST """

# Create new actors
@app.route('/actor', methods=['POST'])
@requires_auth('create:actor')
def create_actor(payload):
    body = request.get_json()
    if not body:
        abort(422)
    else:
        name = body.get('name', None)
        gender = body.get('gender', None)
        age = body.get('age', None)

        try:
            new_actor = Actor(name=name, age=age, gender=gender)
            new_actor.insert()

            actors = Actor.query.all()
            actors_formated = [actor.format() for actor in actors]

            return jsonify({
                'success': True,
                'added': new_actor.id,
                'actors': actors_formated,
                'total_actors': len(actors_formated)
            })
        except:
            abort(422) # Unprocessable Entity

# Create new movies
@app.route('/movie', methods=['POST'])
@requires_auth('create:movie')
def create_movie(payload):
    body = request.get_json()
    if not body:
        abort(422)
    else:
        title = body.get('title', None)
        release_date = body.get('release_date', None)
        actors = body.get('actors', None)

        try:
            new_movie = Movie(title=title, release_date=release_date)
            
            for actor in actors:
                actor_in_db = Actor.query.filter_by(id=actor).one_or_none()

                if actor_in_db:
                    new_movie.actors.append(actor_in_db)
            
            new_movie.insert()

            movies = Movie.query.all()
            movies_formated = [movie.format() for movie in movies]

            return jsonify({
                'success': True,
                'added': new_movie.id,
                'movies': movies_formated,
                'total_movies': len(movies_formated)
            })
        except:
            abort(422) # Unprocessable Entity

""" GET """

# Get actors of 'movie_id'
@app.route('/movie/<int:movie_id>/actors',methods=['GET'])
@requires_auth('get:movies, get:actors')
def get_actors_of_a_movie(payload, movie_id):
    movie = Movie.query.filter_by(id=movie_id).one_or_none()
    if movie is None:
        abort(404)
    else:
        actors = movie.actors
        actors_formated = [actor.format() for actor in actors]
        return jsonify({
            'success': True,
            'actors': actors_formated
        })

# Get movies
@app.route('/movie', methods=['GET'])
@requires_auth('get:movies')
def get_movies(payload):
    try:
        movies = Movie.query.order_by(Movie.id).all()
        movies_formated = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': movies_formated,
            'total_movies': len(movies)
        })
    except:
        abort(422) # Unprocessable Entity

# Get actors
@app.route('/actor', methods=['GET'])
@requires_auth('get:actors')
def get_actors(payload):
    try:
        actors = Actor.query.order_by(Actor.id).all()
        actors_formated = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': actors_formated,
            'total_actors': len(actors)
        })
    except:
        abort(422) # Unprocessable Entity

""" PATCH """

# Update movie details
@app.route('/movie/<int:movie_id>', methods=['PATCH'])
@requires_auth('update:movie')
def update_movie(payload, movie_id):
    try:
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404)
        else:
            body = request.get_json()
            title = body.get('title', None)
            release_date = body.get('release_date', None)
            actors = body.get('actors', None)


            if title is not None:
                movie.title = title
            if release_date is not None:
                movie.release_date = release_date
            if actors is not None:
                movie.actors = []
                for actor_id in actors:
                    actor_in_db = Actor.query.filter_by(id=actor_id).one_or_none()
                    if actor_in_db:
                        movie.actors.append(actor_in_db)

            movie.update()

            movies = Movie.query.all()

        return jsonify({
            'success': True,
            'updated_movie': movie.format(),
            'total_movies': len(movies)
        })
    except:
        abort(422) # Unprocessable Entity

# Update actor details
@app.route('/actor/<int:actor_id>', methods=['PATCH'])
@requires_auth('update:actor')
def update_actor(payload, actor_id):
    try:
        actor = Actor.query.filter_by(id=actor_id).one_or_none()

        if actor is None:
            abort(404)
        else:
            body = request.get_json()
            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)

            if name is not None:
                actor.name = name
            if age is not None:
                actor.age = age
            if name is not None:
                actor.gender = gender

            actor.update()

            actors = Actor.query.all()

        return jsonify({
            'success': True,
            'updated_actor': actor.format(),
            'total_actors': len(actors)
        })
    except:
        abort(422) # Unprocessable Entity

""" DELETE """

# Delete actor with 'actor_id'
@app.route('/actor/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actor(payload, actor_id):
    try:
        actor = actor = Actor.query.filter_by(id=actor_id).one_or_none()
        if actor is None:
            abort(404)
        else:
            actor.delete()
            actors = Actor.query.all()
        return jsonify({
            'success': True,
            'deleted_actor': actor_id,
            'total_actors': len(actors)
        })
    except:
        abort(422) # Unprocessable Entity

# Delete movie with 'movie_id'
@app.route('/movie/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movie')
def delete_movie(payload, movie_id):
    try:
        movie = movie = Movie.query.filter_by(id=movie_id).one_or_none()
        if movie is None:
            abort(404)
        else:
            movie.delete()
            movies = Movie.query.all()
        return jsonify({
            'success': True,
            'deleted_movie': movie_id,
            'total_movies': len(movies)
        })
    except:
        abort(422) # Unprocessable Entity


@app.route('/')
def index():
    return jsonify({
        'message':'Welcome to Casting Agency API.',
        'Endpoints available': {
            '/actor':'POST, GET',
            '/actor':'PATCH, DELETE',
            '/movie':'POST, GET',
            '/movie':'PATCH, DELETE',
            '/movie/<int:movie_id>/actors': 'GET'
        }
    })

## Error Handling ##

'''
Error handler for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": ErrorMessages.ERROR_422_MESSAGE.value
    }), 422

'''
Error handler for 404
'''
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": ErrorMessages.ERROR_404_MESSAGE.value
    }), 404

'''
Error handler for 405
'''
@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": ErrorMessages.ERROR_405_MESSAGE.value
    }), 405

'''
Error handler for AuthError
'''
@app.errorhandler(AuthError)
def autherror(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error
    }), error.status_code