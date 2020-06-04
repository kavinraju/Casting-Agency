from flask_sqlalchemy import SQLAlchemy
import json
import unittest

from app import app, ErrorMessages
from database.models import setup_db, Movie, Actor

""" keystore consists of all the passwords required for the backend """
from environments.config import password, username, get_data_base_path

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting Agency test case"""

    def setUp(self):
        database_name = 'casting_test'
        database_path = get_data_base_path(username, password, database_name)
        self.app = app
        self.client = self.app.test_client
        self.database_name = database_name
        self.database_path = database_path
        setup_db(self.app, self.database_path)
        
        # UPDATE THE MOVIE ID'S BEFORE RUNNING THE UNIT TEST - these IDs are used for success tests #
        self.movie_id_get = 1
        self.movie_id_edit = 1
        self.movie_id_delete = 1

        # UPDATE THE ACTOR ID'S BEFORE RUNNING THE UNIT TEST - these IDs are used for success tests #
        self.actor_id_get = 1
        self.actor_id_edit = 1
        self.actor_id_delete = 1

        self.new_actor = {
            'name': 'Kavin Raju',
            'gender': 'Male',
            'age': 30
        }

        self.update_actor = {
            'name': 'Kavin Raju S',
            'gender': 'Male',
            'age': 32
        }        

        # UPDATE THE ACTORS IF NECESSARY
        self.new_movie = {
            'title': 'Movie 1',
            'release_date': '2020-05-05 18:51:16',
	        'actors': [self.actor_id_get]
        }

        # UPDATE THE ACTORS IF NECESSARY
        self.update_movie = {
            'title': 'Movie One',
            'release_date': '2020-05-05 18:51:16',
	        'actors': [self.actor_id_get]
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """ Executed after reach test """
        pass

    """
    Written tests for each test for successful operation and for expected errors.
    """

    """ Test for the endpoint 
    POST '/actor'
    """
    ## TEST 1 ##
    # Success Test
    def test_create_actor(self):
        res = self.client().post('/actor', json=self.new_actor)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['added'])
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['total_actors'])

    ## TEST 2 ##
    # Error Test
    def test_405_if_create_actor_not_allowed(self):
        res = self.client().post('/actor/15090', json=self.new_actor)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ErrorMessages.ERROR_405_MESSAGE.value)

    """ Test for the endpoint 
    POST '/movie'
    """
    ## TEST 3 ##
    # Success Test
    def test_create_movie(self):
        res = self.client().post('/movie', json=self.new_movie)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['added'])
        self.assertTrue(len(data['movies']))
        self.assertTrue(data['total_movies'])

    ## TEST 4 ##
    # Error Test
    def test_405_if_create_movie_not_allowed(self):
        res = self.client().post('/movie/15090', json=self.new_actor)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ErrorMessages.ERROR_405_MESSAGE.value)        

    """ Test for the endpoint 
    GET '/actor'
    """
    ## TEST 5 ##
    # Success Test
    def test_get_actor(self):
        res = self.client().get('/actor')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))
        self.assertTrue(data['total_actors'])

    """ Test for the endpoint 
    GET '/movie'
    """
    ## TEST 6 ##
    # Success Test
    def test_get_movie(self):
        res = self.client().get('/movie')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))
        self.assertTrue(data['total_movies'])

    """ Test for the endpoint 
    GET '/movie/<int:movie_id>/actors'
    """
    ## TEST 7 ##
    # Success Test
    def test_get_actors_of_a_movie(self):
        movie_id = self.movie_id_get
        res = self.client().get('/movie/{}/actors'.format(movie_id))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))
    
    ## TEST 8 ##
    # Error Test
    def test_404_actors_for_movie_not_availabe(self):
        movie_id = 15600
        res = self.client().get('/movie/{}/actors'.format(movie_id))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ErrorMessages.ERROR_404_MESSAGE.value)

    """ Test for the endpoint 
    PATCH '/movie/<int:movie_id>'
    """
    ## TEST 9 ##
    # Success Test
    def test_edit_movie(self):
        movie_id = self.movie_id_edit
        res = self.client().patch('/movie/{}'.format(movie_id) , json=self.update_movie)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_movie'])
        self.assertTrue(data['total_movies'])

    ## TEST 10 ##
    # Error Test
    def test_404_edit_movie_not_available(self):
        movie_id = 1090881
        res = self.client().patch('/movie/{}'.format(movie_id) , json=self.update_movie)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ErrorMessages.ERROR_422_MESSAGE.value)

    """ Test for the endpoint 
    PATCH '/actor/<int:actor_id>'
    """
    ## TEST 11 ##
    # Success Test
    def test_edit_actor(self):
        actor_id = self.actor_id_edit
        res = self.client().patch('/actor/{}'.format(actor_id) , json=self.update_actor)
        data = json.loads(res.data)
        print('data: ',data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_actor'])
        self.assertTrue(data['total_actors'])

    ## TEST 12 ##
    # Error Test
    def test_404_edit_actor_not_available(self):
        actor_id = 1090881
        res = self.client().patch('/actor/{}'.format(actor_id) , json=self.update_actor)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ErrorMessages.ERROR_422_MESSAGE.value)

        """ Test for the endpoint 
    DELETE '/movie/<int:movie_id>'
    """
    ## TEST 13 ##
    # Success Test
    def test_delete_movie(self):
        # Update the movie ID to be deleted
        movie_id = self.movie_id_delete
        res = self.client().delete('/movie/{}'.format(movie_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_movie'])

    ## TEST 14 ##
    # Error Test
    def test_404_delete_movie_not_available(self): 
        # Update the movie ID to be deleted
        movie_id = 190873
        res = self.client().delete('/movie/{}'.format(movie_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ErrorMessages.ERROR_422_MESSAGE.value)


    """ Test for the endpoint 
    DELETE '/actor/<int:actor_id>'
    """
    ## TEST 15 ##
    # Success Test
    def test_delete_actor(self):
        # Update the actor ID to be deleted
        actor_id = self.actor_id_delete
        res = self.client().delete('/actor/{}'.format(actor_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_actor'])

    ## TEST 16 ##
    # Error Test
    def test_404_delete_actor_not_available(self):
        # Update the movie ID to be deleted
        actor_id = 190873
        res = self.client().delete('/actor/{}'.format(actor_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ErrorMessages.ERROR_422_MESSAGE.value)


        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()