# Casting Agency
Casting Agency is a company that is responsible for creating movies and managing and assigning actors to those movies. This project implements REST API, authentication & authorization in [Flask](https://flask.palletsprojects.com/en/1.1.x/), role-based control design patterns - securing a REST API using [Auth0](https://auth0.com/), and hosted the same in [Heroku](https://www.heroku.com/).

#### [Check out the API Documentation in GitHub Pages site](https://kavinraju.github.io/Casting-Agency/).

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

### Set up env_file.py locally
Create a env_file.py file and add it in the [environments](https://github.com/kavinraju/Casting-Agency/tree/master/environments) directory. <b>This is required while running the unittest.</b><br>
Add the following code to the env_file.py file:
```python
username_env = 'postgres_db_username'
password_env = 'postgres_db_password'
```

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

Create a database `casting` in PostgreSQL using the following commands.<br>
<b>For Linux:</b>
```bash
createdb casting
```
<b>For Windows:</b>
```bash
create database casting;
```
Run the following commands from same root directory to run the Migration Script to create the required tables:
```bash
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
```
By default, the backend will run on `localhost:5000`

### Run the flask application

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
	"age": 45,
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
      "age": 45,
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
	"title": "Friends",
	"release_date": "2001-05-05 18:51:16",
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
      "release_date": "Sat, 05 May 2001 18:51:16 GMT",
      "title": "Friends"
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
            "age": 45,
            "gender": "Male",
            "id": 1,
            "name": "Vijay"
        },
        {
            "age": 45,
            "gender": "Male",
            "id": 2,
            "name": "Ajith"
        },
        {
            "age": 69,
            "gender": "Male",
            "id": 3,
            "name": "Rajinikanth"
        },
        {
            "age": 65,
            "gender": "Male",
            "id": 4,
            "name": "Kamal Haasan"
        },
        {
            "age": 33,
            "gender": "Female",
            "id": 5,
            "name": "Samantha Akkineni"
        },
        {
            "age": 37,
            "gender": "Female",
            "id": 6,
            "name": "Trisha Krishnan"
        },
        {
            "age": 28,
            "gender": "Female",
            "id": 7,
            "name": "Hansika Motwani"
        },
        {
            "age": 34,
            "gender": "Female",
            "id": 8,
            "name": "Kajal Aggarwal"
        },
        {
            "age": 35,
            "gender": "Male",
            "id": 9,
            "name": "Sivakarthikeyan"
        },
        {
            "age": 54,
            "gender": "Male",
            "id": 10,
            "name": "Vikram"
        },
        {
            "age": 24,
            "gender": "Female",
            "id": 11,
            "name": "Nivetha Thomas"
        },
        {
            "age": 44,
            "gender": "Male",
            "id": 12,
            "name": "Suriya"
        },
        {
            "age": 28,
            "gender": "Female",
            "id": 13,
            "name": "Amy Jackson"
        },
        {
            "age": 52,
            "gender": "Male",
            "id": 14,
            "name": "Akshay Kumar"
        }
    ],
    "success": true,
    "total_actors": 14
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
            "release_date": "Sat, 05 May 2001 18:51:16 GMT",
            "title": "Friends"
        },
        {
            "id": 2,
            "release_date": "Thu, 09 Jan 2020 18:51:16 GMT",
            "title": "Darbar"
        },
        {
            "id": 3,
            "release_date": "Fri, 12 Oct 2012 18:51:16 GMT",
            "title": "Maattrraan"
        },
        {
            "id": 4,
            "release_date": "Sat, 14 Jan 2006 18:51:16 GMT",
            "title": "Aathi"
        },
        {
            "id": 5,
            "release_date": "Sat, 17 Apr 2004 18:51:16 GMT",
            "title": "Ghilli"
        },
        {
            "id": 6,
            "release_date": "Wed, 17 Apr 2013 18:51:16 GMT",
            "title": "Singam II"
        },
        {
            "id": 7,
            "release_date": "Fri, 03 Jul 2015 18:51:16 GMT",
            "title": "Papanasam"
        },
        {
            "id": 8,
            "release_date": "Fri, 03 Jul 2015 18:51:16 GMT",
            "title": "2.0"
        }
    ],
    "success": true,
    "total_movies": 8
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
            "age": 69,
            "gender": "Male",
            "id": 3,
            "name": "Rajinikanth"
        },
        {
            "age": 28,
            "gender": "Female",
            "id": 13,
            "name": "Amy Jackson"
        },
        {
            "age": 52,
            "gender": "Male",
            "id": 14,
            "name": "Akshay Kumar"
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
	"title": "Friends",
	"release_date": "2001-05-05 08:51:16",
	"actors":[1, 12]
}
```

<ul>
<li><b>Sample Response:</b></li>
</ul>

```json
{
  "success": true,
  "total_movies": 8,
  "updated_movie": {
    "id": 1,
    "release_date": "Sat, 05 May 2001 18:51:16 GMT",
    "title": "Friends"
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
  "age": 46,
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
  "total_actors": 14,
  "updated_actor": {
    "age": 46,
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
  "total_movies": 7
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
  "total_actors": 13
}
```

## Tests

In order to run test, navigate to the [root directory](https://github.com/kavinraju/Casting-Agency), run the following commands.<br>
<b>For Linux:</b>
```bash
dropdb casting_test
createdb casting_test
psql casting_test < castingdbexport.psql
python test_app.py
```
<b>For Windows:</b>
```bash
drop database casting_test;
create database casting_test;
psql casting_test < castingdbexport.psql user_name_of_db
python test_app.py
```

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
<b>There are two types of collection files available:</b>
<ol>
	<li><a href="https://github.com/kavinraju/Casting-Agency/blob/deployment/casting-agency-local-endpoints.postman_collection.json">With local endpoints</a></li>
	<li><a href="https://github.com/kavinraju/Casting-Agency/blob/deployment/casting-agency-heroku-endpoints.postman_collection.json">With heroku endpoints</a></li>
</ol>
Import the files into the POSTMAN and test run the endpoints.<br>

#### Tip: How to import the data into heruko db?
Before doing this Reset Database for consistency purpose.
```bash
heroku pg:psql --app application_name_in_heroku < castingdbexport.pgsql
```
After importing the data from [castingdbexport.psql](https://github.com/kavinraju/Casting-Agency/blob/deployment/castingdbexport.pgsql) file, run the <a href="https://github.com/kavinraju/Casting-Agency/blob/deployment/casting-agency-heruko-endpoints.postman_collection.json">collection with heruko endpoints</a> to run all the test successfully.

![casting-agency-heroku-endpoints](https://user-images.githubusercontent.com/24537737/83875022-0ae39580-a754-11ea-8bca-9c160d625eec.PNG)<br>

#### Tip: How to import the data into local postgres db?
<b>For Linux:</b>
```bash
psql casting_test < castingdbexport.psql
```
<b>For Windows:</b>
```bash
psql casting_test < castingdbexport.psql user_name_of_db
or
psql casting_test < castingdbexport.psql -U user_name_of_db
```
After importing the data from [castingdbexport.psql](https://github.com/kavinraju/Casting-Agency/blob/deployment/castingdbexport.pgsql) file, run the <a href="https://github.com/kavinraju/Casting-Agency/blob/deployment/casting-agency-local-endpoints.postman_collection.json">collection with local endpoints</a> to run all the test successfully.

![casting-agency-local-endpoints](https://user-images.githubusercontent.com/24537737/83874848-c1934600-a753-11ea-83bb-dcb793ba3cdb.PNG)

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
