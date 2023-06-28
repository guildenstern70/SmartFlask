## SmartFlask

A web template project featuring:

- Flask 2
- Bootstrap 5
- Cassandra DB

### Cassandra Setup

Take note of your Cassandra DB secret key and client id. 

Get Cassandra certificates and save them in project's root as 'secure-connect-axscassandradb.zip' file
under root folder (where LICENSE file is).

In order to run this program, you Cassandra DB should have a keyspace named 'smartflaskks' and a table named 'student'.

The CQL code to setup the database is found in the file 'db_setup.cql' in the root folder.


### App Setup

Before running this program you should set a number of environment variables:

| Variable name     | Description          | Example                        |
|-------------------|----------------------|--------------------------------|
| FLASK_SECRET_KEY  | Cassandra Secret Key | [Your Cassandra DB secret key] |
| FLASK_CLIENT_ID   | Cassandra Client ID  | [Your Cassandra DB client id]  |

Install Python packages with:

    pip install -r requirements.txt

This will install Flask and other packages needed to run the app.

### Run Development Environment

You can now run the app by giving this command

    flask --app smartflask run




