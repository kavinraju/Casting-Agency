# Casting Agency
Casting Agency is a company that is responsible for creating movies and managing and assigning actors to those movies. This project implements REST API, authentication & authorization in [Flask](https://flask.palletsprojects.com/en/1.1.x/), role-based control design patterns - securing a REST API using [Auth0](https://auth0.com/), and hosted the same in [Heroku](https://www.heroku.com/).

#### This is the Capstone Project created as part of the Full Stack Web Developer Nanodegree program at Udacity.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running the below given command in the same `/Casting-Agency` directory.

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Backend

### Set up Authentication Locally
Run the following commands to set up the environment variables required for authentication. <br>
<b>For Linux:</b>
```bash
export DATABASE_URL=postgresql://username:pass@localhost:5432/casting
export AUTH0_DOMAIN_ENV=casting-agency-fsnd.eu.auth0.com
export ALGORITHMS_ENV=RS256
export API_AUDIENCE_ENV=casting
```
<b>For Windows:</b>
```bash
set DATABASE_URL=postgresql://username:pass@localhost:5432/casting
set AUTH0_DOMAIN_ENV=casting-agency-fsnd.eu.auth0.com
set ALGORITHMS_ENV=RS256
set API_AUDIENCE_ENV=casting
```

### Setting up backend

Before running the flask application run the following commands to set up the environment variables required by flask application.<br>
<b>For Linux:</b>
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run # before running this command make sure you complete authentication setup
```
<b>For Windows:</b>
```bash
set FLASK_APP=app.py
set FLASK_ENV=development
python -m flask run # before running this command make sure you complete authentication setup
```
>> NOTE: Replace the username & pass by your username & password of the postgresql server setup.


## API Reference
### Get Started
- <b>Base URL:</b> This app is hosted at [Heroku](https://www.heroku.com/) and can be run locally.<br>
    <ul>
      <li>Local Base URL is <a href>http://127.0.0.1:5000/<a/></li>
      <li>Heroku Base URL is <a href>https://casting-agency-skr.herokuapp.com/<a/></li>
    </ul>
- <b>Authentication:</b> This version of the application requires [Auth0](https://auth0.com/) authentication.
- <b>Roles and permission</b>: This projects implements 3 roles with various set of permissions to access the endpoints.<br>
  <ul>
    <li><b>Casting Assistant: </b> Can view actors and movies.</li>
    <ul>
      <li><b>get:actors</b> Read the list of actors</li>
      <li><b>get:movies</b> Read the list of movies</li>
      <li><b>get:movie_actors</b> Read the list of actors from the given movie ID.</li>
    </ul><br>
    
    <li><b>Casting Director: </b> All permissions a Casting Assistant has and can add or delete an actor from the database Modify actors or movies.</li>
    <ul>
      <li><b>create:actor</b> Create actor</li>
      <li><b>delete:actor</b> Delete actor</li>
      <li><b>get:actors</b> Read the list of actors</li>
      <li><b>get:movies</b> Read the list of movies</li>
      <li><b>get:movie_actors</b> Read the list of actors from the given movie ID.</li>
      <li><b>update:actor</b> Update the actor details</li>
      <li><b>update:movie</b> Update the movie details</li>
    </ul><br>
     
     <li><b>Executive Producer: </b> All permissions a Casting Director has and can add or delete a movie from the database.</li>
    <ul>
      <li><b>create:actor</b> Create actor</li>
      <li><b>create:movie</b> Create movie</li>
      <li><b>delete:actor</b> Delete actor</li>
      <li><b>delete:movie</b> Delete movie</li>
      <li><b>get:actors</b> Read the list of actors</li>
      <li><b>get:movies</b> Read the list of movies</li>
      <li><b>get:movie_actors</b> Read the list of actors from the given movie ID.</li>
      <li><b>update:actor</b> Update the actor details</li>
      <li><b>update:movie</b> Update the movie details</li>
    </ul>
  </ul>

### Endpoints
Since all the requests to the API requires the `Bearer token` this project was fully tested using [POSTMAN](https://www.postman.com/) and it'recommended too.

#### GET  `/`
<ul>
   <li>Returns
      <ul>
	<li>Endpoints available</li>
	<li>message</li>
       </ul>          
    </li>
    <li>This endpoint is created to let the users know about the available endpoints, and a greeting message. There is a possibility of this endpoint data getting changed at sometime later. This endpoint is set as a redirecting URL after logging in successfully.</li>
</ul>

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "Endpoints available": {
    "/actor": "PATCH, DELETE", 
    "/movie": "PATCH, DELETE", 
    "/movie/<int:movie_id>/actors": "GET"
  }, 
  "message": "Welcome to Casting Agency API."
}
```

#### POST `/actor`
<ul>
  <li><b>Genral:</b></li>
    <ul>
      <li>Requires
        <ul>
            <li>Actor data</li>
            <li>Auth header with the bearer token key</li>
        </ul>
      </li>
      <li>Returns
         <ul>
           <li>list of actors</li>
           <li>created actor id</li>
           <li>success value</li>
           <li>total number of actors</li>
         </ul>          
       </li>
    </ul>
  <li>Both success `TEST 1` and error `TEST 2` Tests are available at <a href="test_app.py">test_app.py</a> file.</li>
</ul>

<ul>
<li><b>Sample Data for the request:</b></li>
</ul>

```json
{
	"name": "Vijay",
	"age": 30,
	"gender": "Male"
}
```

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "actors": [
    {
      "age": 30,
      "gender": "Male",
      "id": 1,
      "name": "Vijay"
    }
  ],
  "added": 1,
  "success": true,
  "total_actors": 1
}
```

#### POST `/movie`
<ul>
  <li><b>Genral:</b></li>
    <ul>
      <li>Requires
        <ul>
            <li>Movie data</li>
            <li>Auth header with the bearer token key</li>
        </ul>
      </li>
      <li>Returns
         <ul>           
           <li>created movie id</li>
           <li>list of movies</li>
           <li>success value</li>
           <li>total number of movies</li>
         </ul>          
       </li>
    </ul>
  <li>Both success `TEST 3` and error `TEST 4` Tests are available at <a href="test_app.py">test_app.py</a> file.</li>
</ul>

<ul>
<li><b>Sample Data for the request:</b></li>
</ul>

```json
{
	"title": "Movie 1",
	"release_date": "2020-05-05 18:51:16",
	"actors":[1]
}
```

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "added": 1,
  "movies": [
    {
      "id": 1,
      "release_date": "Tue, 05 May 2020 18:51:16 GMT",
      "title": "Movie 1"
    }
  ],
  "success": true,
  "total_movies": 1
}
```

#### GET `/actor`
<ul>
  <li><b>Genral:</b></li>
    <ul>
      <li>Requires
        <ul>
            <li>Auth header with the bearer token key</li>
        </ul>
      </li>
      <li>Returns
         <ul>
           <li>list of actors</li>
           <li>success value</li>
           <li>total number of actors</li>
         </ul>          
       </li>
    </ul>
  <li>Success `TEST 5` Test is available at <a href="test_app.py">test_app.py</a> file.</li>
</ul>

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "actors": [
    {
      "age": 30,
      "gender": "Male",
      "id": 1,
      "name": "Vijay"
    }
  ],
  "success": true,
  "total_actors": 1
}
```

#### GET `/movie`
<ul>
  <li><b>Genral:</b></li>
    <ul>
      <li>Requires
        <ul>
            <li>Auth header with the bearer token key</li>
        </ul>
      </li>
      <li>Returns
         <ul>
           <li>list of movies</li>
           <li>success value</li>
           <li>total number of movies</li>
         </ul>          
       </li>
    </ul>
  <li>Success `TEST 6` Test is available at <a href="test_app.py">test_app.py</a> file.</li>
</ul>

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "movies": [
    {
      "id": 1,
      "release_date": "Tue, 05 May 2020 18:51:16 GMT",
      "title": "Movie 1"
    }
  ],
  "success": true,
  "total_movies": 1
}
```

#### GET `/movie/<int:movie_id>/actors`
<ul>
  <li><b>Genral:</b></li>
    <ul>
      <li>Requires
        <ul>
          <li>Movie ID</li>
          <li>Auth header with the bearer token key</li>
        </ul>
      </li>
      <li>Returns
         <ul>
           <li>list of actors</li>
           <li>success value</li>
         </ul>          
       </li>
    </ul>
  <li>Both success `TEST 7` and error `TEST 8` Tests are available at <a href="test_app.py">test_app.py</a> file.</li>
</ul>

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "actors": [
    {
      "age": 30,
      "gender": "Male",
      "id": 1,
      "name": "Vijay"
    }
  ],
  "success": true
}
```

#### PATCH `/movie/<int:movie_id>`
<ul>
  <li><b>Genral:</b></li>
    <ul>
      <li>Requires
        <ul>
            <li>Movie ID</li>
            <li>Auth header with the bearer token key</li>
        </ul>
      </li>
      <li>Returns
         <ul>           
           <li>success value</li>
           <li>total number of movies</li>
           <li>updated movie data</li>        
         </ul>          
       </li>
    </ul>
  <li>Both success `TEST 9` and error `TEST 10` Tests are available at <a href="test_app.py">test_app.py</a> file.</li>
</ul>

<ul>
<li><b>Sample Data for the request:</b></li>
</ul>

```json
{
	"title": "Movie 2000",
	"release_date": "2020-05-05 08:51:16",
	"actors":[1]
}
```

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "success": true,
  "total_movies": 1,
  "updated_movie": {
    "id": 1,
    "release_date": "Tue, 05 May 2020 08:51:16 GMT",
    "title": "Movie 2000"
  }
}
```

#### PATCH `/actor/<int:actor_id>`
<ul>
  <li><b>Genral:</b></li>
    <ul>
      <li>Requires
        <ul>
            <li>Actor ID</li>
            <li>Auth header with the bearer token key</li>
        </ul>
      </li>
      <li>Returns
         <ul>           
           <li>success value</li>
           <li>total number of actors</li>
           <li>updated actor data</li>        
         </ul>          
       </li>
    </ul>
  <li>Both success `TEST 11` and error `TEST 12` Tests are available at <a href="test_app.py">test_app.py</a> file.</li>
</ul>

<ul>
<li><b>Sample Data for the request:</b></li>
</ul>

```json
{
  "age": 31,
  "gender": "Male",
  "name": "Vijay S"
}
```

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "success": true,
  "total_actors": 1,
  "updated_actor": {
    "age": 31,
    "gender": "Male",
    "id": 1,
    "name": "Vijay S"
  }
}
```

#### DELETE `/movie/<int:movie_id>`
<ul>
  <li><b>Genral:</b></li>
    <ul>
      <li>Requires
        <ul>
            <li>Movie ID</li>
            <li>Auth header with the bearer token key</li>
        </ul>
      </li>
      <li>Returns
         <ul>           
           <li>deleted movie ID</li>
           <li>success value</li>
           <li>total number of movies</li>
         </ul>          
       </li>
    </ul>
  <li>Both success `TEST 13` and error `TEST 14` Tests are available at <a href="test_app.py">test_app.py</a> file.</li>
</ul>

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "deleted_movie": 1,
  "success": true,
  "total_movies": 0
}
```

#### DELETE `/actor/<int:actor_id>`
<ul>
  <li><b>Genral:</b></li>
    <ul>
      <li>Requires
        <ul>
            <li>Actor ID</li>
            <li>Auth header with the bearer token key</li>
        </ul>
      </li>
      <li>Returns
         <ul>           
           <li>deleted actor ID</li>
           <li>success value</li>
           <li>total number of actors</li>
         </ul>          
       </li>
    </ul>
  <li>Both success `TEST 15` and error `TEST 16` Tests are available at <a href="test_app.py">test_app.py</a> file.</li>
</ul>

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "deleted_actor": 1,
  "success": true,
  "total_actors": 0
}
```

## Tests

### Unittest
This includes the tests for the endpoints without auth header (bearer token key). These tests check if the endpoints are working correctly by creating a test database [casting_test](https://github.com/kavinraju/Casting-Agency/blob/8a1743bc56da28323eb5b344c30de0febb6fddc8/test_app.py#L15) locally. To run this test <br>
- checkout to the [unittest branch](https://github.com/kavinraju/Casting-Agency/tree/unittest)
- check all the `TODOs` provided in the [database/models.py](https://github.com/kavinraju/Casting-Agency/blob/8a1743bc56da28323eb5b344c30de0febb6fddc8/database/models.py#L21), [environments/config.py](https://github.com/kavinraju/Casting-Agency/blob/unittest/environments/config.py) files so that test runs properly. Few lines are commented out for the purpose of production code.

In order to run the [test](test_app.py) of the endpoints, run the following commands.<br>
<b>For Linux:</b>
```bash
python test_app.py
```
<b>For Windows:</b>
```bash
python test_app.py
```
<b>NOTE:</b>
First run the test with the code commented out for the endpoints <b>DELETE `/movie/<int:movie_id>`</b>, <b>DELETE `/actor/<int:actor_id>`</b>. Only while running endpoint test for the `DELETE endpoints` uncomment it. This is because sometimes the test runs parallelly which leads to test failure, as DELETE test run before GET/PATCH test run. It is available in [test_app.py](https://github.com/kavinraju/Casting-Agency/blob/8a1743bc56da28323eb5b344c30de0febb6fddc8/test_app.py#L229) file.

### POSTMAN Test
Export the (Casting Agency.postman_collection.json)[] file and import it to the POSTMAN and test run the endpoints. By default this file consists of local endpoints only. Log into the application if the authorisation token gets expired.
>> Login URL - https://casting-agency-fsnd.eu.auth0.com/authorize?audience=casting&response_type=token&client_id=YTFv82zJIbogLO8PWL61bVh23TrpXC7X&redirect_uri=http://localhost:5000


## Error Handling
Errors are returned as JSON objects in the following format:
```json
{
  "error": 404,
  "message": "Resource not found",
  "success": false
}
```
This API will return three error types when requests fail:
<ul>
  <li><b>400</b> Missing permissions</li>
  <li><b>401</b> Authorization Error (Unauthorized, Token expired)</li>
  <li><b>404</b> Resource not found</li>
  <li><b>405</b> Method not found</li>
  <li><b>422</b> Uprocessable Entity</li>
</ul>

## Code Guidelines
All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

## Authors
- [Kavin Raju S](https://www.linkedin.com/in/kavinraju/).

## Acknowledgements
The awesome [Udacity](https://udacity.com/) Team!
