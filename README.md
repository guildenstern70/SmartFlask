## SmartFlask

A web template project featuring:

- Flask 2
- Bootstrap 5
- Cassandra DB


### Setup

Before running this program you should set a number of environment variables:

| Variable name     | Description          | Example                          |
|-------------------|----------------------|----------------------------------|
| FLASK_SECRET_KEY  | Cassandra Secret Key | 5f352379324c22463451387a0aec5d2f |
| FLASK_CLIENT_ID   | Cassandra Client ID  | 3c33tYJ.JhKNbx1................. |

    

Install Python packages with:

    pip install -r requirements.txt

Get Cassandra certificates and save them in project's root as 'secure-connect-axscassandradb.zip' file
under root folder (where LICENSE file is)



### Run Development Environment

    flask --app smartflask run




